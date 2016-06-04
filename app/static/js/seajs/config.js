var FRONTEND_HOST = window.FRONTEND_HOST || '/static/js';

//log patch
if (!window['console']) {
    window['console'] = {
        'info': function () {
        },
        'log': function () {
        },
        'error': function () {
        },
        'warn': function () {
        }
    };
}

seajs.config({
    alias: {
        "jquery": "jquery/jquery-1.8.3.min.js",
        "jquery-1.11.2": "jquery/jquery-1.11.2.min.js",
        "jquerycolor": "jquery/jquerycolor.js",
        "jquery/ui": "jquery/ui/jquery-ui.min.js",
        "jquery/ui/timepicker": "jquery/ui/jquery-ui-timepicker-addon.js",
        "jquery/ui/tooltip": "jquery/ui/jquery-ui-tooltip-addon.js",
        "swiper": "swiper/swiper.min.js",
        "waterfall": "waterfall/waterfall.js",

        "ueditor": FRONTEND_HOST + "/ueditor/ueditor.all.js",
        "ueditor_admin_config": FRONTEND_HOST + "/ueditor/ueditor.admin.js",
        "underscore":FRONTEND_HOST+"/underscore-min.js",
        "is":FRONTEND_HOST+"/is.min.js",
        "json2":FRONTEND_HOST+"/json2.js",
        "store":FRONTEND_HOST+"/store.min.js"
    },

    paths: {
        "ywj": FRONTEND_HOST + "/ywj/component",
        "ywjui": FRONTEND_HOST + "/ywj/ui",
        "jquery/ui": FRONTEND_HOST + "/jquery/ui/jquery-ui.min.js",
        "jquery/ui/timepicker": FRONTEND_HOST + "/jquery/ui/jquery-ui-timepicker-addon.js",
        "jquery/ui/tooltip": FRONTEND_HOST + "/jquery/ui/jquery-ui-tooltip-addon.js"
    },

    //全局使用jquery
    preload: [
        !window.jQuery ? 'jquery' : ''
    ],
    charset: 'utf-8'
});