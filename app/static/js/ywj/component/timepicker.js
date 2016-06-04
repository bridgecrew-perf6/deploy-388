/**
 * Created by sasumi on 2014/12/2.
 */
define('ywj/timepicker', function (require) {
    require('jquery/ui/timepicker');

    var css = ".ui-timepicker-div .ui-widget-header { margin-bottom: 8px; }\
				.ui-timepicker-div dl { text-align: left; }\
				.ui-timepicker-div dl dt { float: left; clear:left; padding: 0 0 0 5px; }\
				.ui-timepicker-div dl dd { margin: 0 10px 10px 45%; }\
				.ui-timepicker-div td { font-size: 90%; }\
				.ui-tpicker-grid-label { background: none; border: none; margin: 0; padding: 0; }\
				.ui-timepicker-rtl{ direction: rtl; }\
				.ui-timepicker-rtl dl { text-align: right; padding: 0 5px 0 0; }\
				.ui-timepicker-rtl dl dt{ float: right; clear: right; }\
				.ui-timepicker-rtl dl dd { margin: 0 45% 10px 10px; }";
    $(function () {
        $('<style type="text/css">' + css + '</style>').appendTo($('head'));
    });
});