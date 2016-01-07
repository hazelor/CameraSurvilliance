/**
 * Created by server on 16-1-6.
 */
jQuery(function(){

    $(".Close").click(function(){

        $(".LayBg,.LayBox").hide();
    });
    $(".thumbnail").click(function(){
        $(".LayBg").height(document.body.clientWidth);
        $(".LayImg").html($(this).find(".hidden").html());
        $(".LayBg").show();
        $(".LayBox").fadeIn(300);
    });

})


function page_jump(){
    var url = "/preview?page="+$("#page_jump_num").val();
    window.location.replace(url);
}