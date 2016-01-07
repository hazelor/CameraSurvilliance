
function switchTab(index, issavebtnshow) {
    $("ul#nav").find('li').each(function () {
        $(this).removeClass();
    })
    $("li#nav_"+index).addClass('active');

    $("ul#tab_con").find('li').each(function () {
        $(this).removeClass();
    })
    $("li#tab_con_"+index).addClass('active');

    if(issavebtnshow == 0)
    {
        $('#save_config_btn').css("display","inline-block");
    }
    else
    {
        $('#save_config_btn').css("display","none");
    }
}

$(function(){
    $("#bright_slider").slider({
        range:"min",
        min:0,
        max:100,
        value:60,
        slide:function(event ,ui){
            $("#bright_value").val(ui.value);
    }
    });

    $("#bright_value").val($("#bright_slider").slider("value"));
});
