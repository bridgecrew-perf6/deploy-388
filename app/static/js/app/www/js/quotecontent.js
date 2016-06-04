define('www/quotecontent', function () {

    seajs.use(['jquery', 'ywj/popup', 'ywj/net', 'ywj/util', 'ywj/tmpl', 'jquery/ui'], function ($, Pop, net, util, tmpl, jui) {
        $(function () {
            $('.show-in-edit').hide();

            $(".rscutico").click(function () {
                var $item = $(this).parent().siblings(".quote-item-list");
                $item.toggle();
                if ($item.is(":hidden")) {
                    $(this).addClass("rsaddico");
                } else {
                    $(this).removeClass("rsaddico");
                }
            });

            //帮助弹层
            $(".quote-help-cont").hover(function () {
                $(this).find(".quo-explain").show();
                $(this).parent(".quote-catalog-name").addClass("quote-help-ztop");
            }, function () {
                $(this).find(".quo-explain").hide();
                $(this).parent(".quote-catalog-name").removeClass("quote-help-ztop");
            });

            //点击修改
            $(".amendbtn").click(function () {
                $('.show-in-edit').toggle();
                $('.show-in-view').toggle().each(function () {
                    var _val_append_name = $(this).attr('val-append-name');
                    var _var_append_selector = $(this).attr('var-append-selector');
                    var html_val = '';
                    var tr = $(this).closest('tr');
                    if (_var_append_selector == 'select') {
                        html_val = $("select[name='" + _val_append_name + "']", tr).find("option:selected").text();
                    }
                    if (_var_append_selector == 'input') {
                        html_val = $("input[name='" + _val_append_name + "']", tr).val();
                    }
                    $(this).html('');
                    $(this).html(html_val);
                });
            });

            //选中删除时进行行变灰色
            $('input.sku_del_chk').change(function () {
                var _this = $(this);
                var $delTr = _this.parents(".room-sku-info");

                var $sku_price = _this.parents('tr').children().children('[data-mode=price]');

                var tr = _this.closest('tr');

                $('select', tr).attr('disabled', !this.checked);
                $('input[type=text]', tr).attr('disabled', !this.checked);
                tr[!this.checked ? 'addClass' : 'removeClass']('row-disabled');

                //重新计算数值
                update_sum();
            });

        });

        //自动计算报价数字的JS
        var __fn__ = function (n, fix_count) {
            fix_count = fix_count === undefined ? 2 : fix_count;
            if (n) {
                n = parseFloat(n);
                n = n.toFixed(fix_count);
            } else {
                n = 0;
            }
            return n;
        };

        if (window.PAGE_READONLY) {
            $(':input').attr('disabled', 'disabled');
            $('.amendbtn').hide();
            $('.g-search-text').attr('disabled', false);
            return;
        }

        var $body = $('body');

        /**
         * 工程量超出检测
         * @param new_quo
         * @param ori_quo
         * @returns {boolean}
         */
        var check_quantity_warn = function (new_quo, ori_quo) {
            return (Math.abs(new_quo - ori_quo) / ori_quo) > 0.1;
        };

        var update_sku_price = function () {
            $('*[data-mode=price]').each(function () {
                var row = $(this).closest('tr');
                var sku_sel = $('*[data-mode=sku-list]', row);
                var sel = sku_sel[0];
                if (sel) {
                    var p = sel.disabled ? 0 : $(sel.options[sel.selectedIndex]).data('price');
                    $(this).html(p);
                }
            });
        };
        var update_sku_sum = function () {
            $('*[data-mode=sku-sum]').each(function () {
                var row = $(this).closest('tr');
                var price = parseFloat($('*[data-mode=price]', row).html());
                var count = parseFloat($('*[data-mode=number]', row).val());
                $(this).html(__fn__(price * count));
            });
        };

        var update_room_sum = function () {
            $('*[data-mode=room-sum]').each(function () {
                var tbl = $(this).closest('table');
                var s = 0;
                $('*[data-mode=sku-sum]', tbl).each(function () {
                    s += parseFloat($(this).html());
                });
                $(this).html(__fn__(s));
            });
        };

        var update_catalog_sum = function () {
            var product_sum = 0;
            $('*[data-mode=catalog-sum]').each(function () {
                var cat = $(this).closest('.quote-catalog');
                var s = 0;
                $('*[data-mode=room-sum]', cat).each(function () {
                    s += parseFloat($(this).html());
                });
                product_sum += s;
                $(this).html(__fn__(s));
            });
            return product_sum;
        };

        var update_total_sum = function (product_sum) {
            //商品总价
            var operating_sum = product_sum * OPERATING_COST_RATIO;
            var tax_sum = (product_sum + operating_sum) * TAX_RATIO;
            var total = product_sum + operating_sum + tax_sum;

            //管理费
            $('#operating_sum').html(__fn__(operating_sum));

            //税金
            $('#tax_sum').html(__fn__(tax_sum));

            //总价
            $('*[data-mode=total-sum]').each(function () {
                $(this).html(__fn__(total - operating_sum - tax_sum, 2));
            });
        };
        /**
         * 更新价格计数
         **/
        var update_sum = function () {

            update_sku_price();

            update_sku_sum();

            update_room_sum();

            var product_sum = update_catalog_sum();

            update_total_sum(product_sum);
        };

        /**
         * 新增产品
         * @todo 还没完成
         * @param sku
         * @param node
         */
        var insert_product = function (sku, node) {
            console.log('insert_product', sku);
            var tbl = node.closest('table');
            var tbody = $('tbody', tbl);
            var room_idx = $('input[rel=room_name_guid]', tbl).val();
            var tpl = tmpl($('#product-tpl').html(), {
                sku: sku,
                room_idx: room_idx
            });
            tbody.prepend(tpl);
        };

        /**
         * 新增房间
         * @todo 还没测试f
         * @param room
         * @param node
         */
        var insert_room = function (room, node) {
            var list_con = $(node).closest('.quote-catalog');
            list_con = $('.quote-col-label', list_con);
            var guid = util.guid();
            var head_html = tmpl($('#room-head-tpl').html(), {
                room: room,
                guid: guid
            });
            var tpl = tmpl($('#room-tpl').html(), {head_html: head_html});
            $(tpl).insertAfter(list_con);
        };

        /**
         * 更新房间
         * @param room
         * @param node
         */
        var update_room = function (room, node) {
            var cell = node.closest('th');
            var guid = $('input[rel=room_name_guid]', cell).val();

            var tpl = tmpl($('#room-head-tpl').html(), {
                room: room,
                guid: guid
            });
            cell.html(tpl);
        };

        /**
         * 添加工程
         * @param category
         * @param node
         */
        var insert_category = function (category, node) {
            var list_con = $(node).closest('.quote-catalog');
            list_con = $('.quote-col-label', list_con);
            var guid = util.guid();
            var head_html = tmpl($('#category-head-tpl').html(), {
                category: category,
                guid: guid
            });
            var tpl = tmpl($('#category-tpl').html(), {head_html: head_html});
            $(tpl).insertAfter(list_con);
        };


        /**
         * 新增工程项目
         * @todo 还没完成
         * @param sku
         * @param node
         */
        var insert_category_item = function (sku, node) {
            console.log('insert category item', sku);
            var tbl = node.closest('table');
            var tbody = $('tbody', tbl);
            var category_id = $('input[rel=category_id]', tbl).val();
            var tpl = tmpl($('#category-item-tpl').html(), {
                sku: sku,
                category_id: category_id
            });
            tbody.prepend(tpl);
        };

        //添加工程
        $body.delegate('*[rel=add-category]', 'click', function (ev) {
            var _this = this;
            var url = net.buildParam(URL_UPDATE_CATEGORY, {ref: 'iframe'});
            var p = new Pop({
                title: '添加工程',
                top: ev.clientY - 100,
                content: {src: url}
            });
            p.listen('onSuccess', function (category) {
                insert_category(category, _this);
            });
            p.show();
            return false;
        });

        //删除工程
        $body.delegate('*[rel=delete-category]', 'click', function () {
            if (confirm('确定要删除该项工程？')) {
                var tbl = $(this).closest('table');
                tbl.animate({opacity: 0}, function () {
                    tbl.remove();
                    update_sum();
                });
            }
            return false;
        });

        //删除工程项目
        $body.delegate('*[rel=delete-category-item]', 'click', function () {
            var tr = $(this).closest('tr');
            tr.animate({opacity: 0}, function () {
                tr.remove();
                update_sum();
            });
        });

        //添加工程项目
        $body.delegate('*[rel=add-category-item]', 'click', function (ev) {
            $this = $(this);
            var category_id = $('input[rel=category_id]', $this.parent()).val();
            var url = net.buildParam(URL_ADD_PRODUCT, {
                ref: 'iframe',
                category_id: category_id
            });
            var p = new Pop({
                title: this.title,
                top: ev.clientY - 100,
                content: {src: url}
            });
            p.listen('onSuccess', function (sku) {
                insert_category_item(sku, $this);
                update_sum();
            });
            p.show();
            return false;
        });

        //sku 改变
        $body.delegate('*[data-mode=sku-list]', 'change', function () {
            update_sum();
        });

        //工程量改变
        $.each(['keydown', 'keyup', 'change'], function (k, ev) {
            $body.delegate('*[data-mode=number]', ev, function () {
                update_sum();
            });
        });

        //微调时触发update sum事件
        $(".spinner").spinner({
            stop: function (event, ui) {
                update_sum();
            }
        });

        //工程量变化提醒
        $body.delegate('*[data-mode=number]', 'change', function () {
            var $this = $(this);
            var ori_quo = $this.data('original-quantity') || 0;
            if (ori_quo && check_quantity_warn(this.value, ori_quo)) {
                if (!confirm('您对于工程量调整的范围过大，是否确认继续')) {
                    $this.val(ori_quo);
                }
            }
        });

        //插入房间
        $body.delegate('*[rel=add-room]', 'click', function (ev) {
            var _this = this;
            var url = net.buildParam(URL_UPDATE_ROOM, {ref: 'iframe'});
            var p = new Pop({
                title: '添加房间',
                top: ev.clientY - 100,
                content: {src: url}
            });
            p.listen('onSuccess', function (room) {
                insert_room(room, _this);
            });
            p.show();
            return false;
        });

        //更新房间
        $body.delegate('*[rel=update-room]', 'click', function (ev) {
            var $this = $(this);
            var cell = $this.parent();
            var guid = $('input[rel=room_name_guid]', cell).val();

            var data = {
                ref: 'iframe',
                room_type_id: $('input[rel=room_type_id_list]', cell).val(),

                room_id: $('input[name=room_id_list\\[' + guid + '\\]]', cell).val(),
                name: $('input[name=room_name_list\\[' + guid + '\\]]', cell).val(),
                wall_area: $('input[name=room_wall_area_list\\[' + guid + '\\]]', cell).val(),
                perimeter: $('input[name=room_perimeter_list\\[' + guid + '\\]]', cell).val(),
                floor_area: $('input[name=room_floor_area_list\\[' + guid + '\\]]', cell).val()
            };

            var url = net.buildParam(URL_UPDATE_ROOM, data);
            var p = new Pop({
                title: '更新房间信息',
                top: ev.clientY - 100,
                content: {src: url}
            });
            p.listen('onSuccess', function (room) {
                update_room(room, $this);
                update_sum();
            });
            p.show();
            return false;
        });

        //删除房间
        $body.delegate('*[rel=delete-room]', 'click', function () {
            if (confirm('确定要删除该项工艺？')) {
                var tbl = $(this).closest('table');
                tbl.animate({opacity: 0}, function () {
                    tbl.remove();
                    update_sum();
                });
            }
            return false;
        });

        //插入产品
        $body.delegate('*[rel=add-room-product]', 'click', function (ev) {
            $this = $(this);
            var room_type_id = $('input[rel=room_type_id_list]', $this.parent()).val();
            var url = net.buildParam(URL_ADD_PRODUCT, {ref: 'iframe', room_type_id: room_type_id});
            var p = new Pop({
                title: this.title,
                top: ev.clientY - 100,
                content: {src: url},
                room_type_id: room_type_id
            });
            p.listen('onSuccess', function (sku) {
                insert_product(sku, $this);
                update_sum();
            });
            p.show();
            return false;
        });

        //删除产品
        $body.delegate('*[rel=delete-product]', 'click', function () {
            var tr = $(this).closest('tr');
            tr.animate({opacity: 0}, function () {
                tr.remove();
                update_sum();
            });
        });
    });
});