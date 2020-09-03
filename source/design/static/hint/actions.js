const hint = $('#hint');
// noinspection JSUnusedGlobalSymbols,JSUnusedLocalSymbols
$('[data-hint]').on({
    mouseenter: function(){
        hint.text($(this).data('hint')).show();
    },
    mouseleave: function(){
        hint.hide();
    },
    mousemove: function(e){
        hint.css({top: e.pageY, left: e.pageX});
    },
    mousedown: function (e) {
        hint.text("Copied").show();
    }
});
