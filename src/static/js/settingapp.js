
var is_deleting = false;

function alert_if_deleting(){
    if(is_deleting)
    return '历史数据清除中,您确定要离开当前页面?'
}

window.onbeforeunload = alert_if_deleting;

function switchTab(index, issavebtnshow) {
    $("ul#nav").find('li').each(function () {
        $(this).removeClass('active');
    })
    $("li#nav_"+index).addClass('active');

    $("ul#tab_con").find('li').each(function () {
        $(this).removeClass('active');
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
    document.getElementById('is_success').style.display='none'
}

$(function(){


    $("#bright_value").val($("#bright_slider").slider("value"));
    $("#bright_value").change(function(){
        $("#bright_slider").slider({"value":$("#bright_value").val()});
    });


    $("#contrast_value").val($("#contrast_slider").slider("value"));
    $("#contrast_value").change(function(){
        $("#contrast_slider").slider({"value":$("#contrast_value").val()});
    });

    $("#saturation_value").val($("#saturation_slider").slider("value"));
    $("#saturation_value").change(function(){
        $("#saturation_slider").slider({"value":$("#saturation_value").val()});
    });
    //$("#sharpness_slider").slider({
    //    range:"min",
    //    min:0,
    //    max:100,
    //    value:60,
    //    slide:function(event ,ui){
    //        $("#sharpness_value").val(ui.value);
    //}
    //});
    //
    //$("#sharpness_value").val($("#sharpness_slider").slider("value"));
});

function save_monitor_config(){
    if($('#tab_con_1').attr('class') == 'active'){
        //alert('tab_con_1')
        $.ajax({
            url:'save_monitor_config',
            type:'get',
            dateType:'text',
            data:{
                'type':'video',
                'resolution':document.getElementById('resolution').value,
                'framerate':document.getElementById('framerate').value,
                'rotate':document.getElementById('rotate').value,
                'brightness':document.getElementById('bright_value').value,
                'contrast':document.getElementById('contrast_value').value,
                'saturation':document.getElementById('saturation_value').value,
            },
            success:function(){
                document.getElementById('is_success').innerHTML='保存成功'
                document.getElementById('is_success').style.display='inline'

            },
            error:function(){
                document.getElementById('is_success').innerHTML='保存失败'
                document.getElementById('is_success').style.display='inline'
            },
        })
    }
    else{
        $.ajax({
            url:'save_monitor_config',
            type:'get',
            dateType:'text',
            data:{
                'type':'image',
                'snapshot_interval':document.getElementById('snapshot_interval').value,
            },
            success:function(){
                document.getElementById('is_success').innerHTML='保存成功'
                document.getElementById('is_success').style.display='inline'

            },
            error:function(){
                document.getElementById('is_success').innerHTML='保存失败'
                document.getElementById('is_success').style.display='inline'
            },
        })
    }

}

function save_basic_config(){
    if($('#tab_con_1').attr('class') == 'active'){
        $.ajax({
            url:'save_basic_config',
            type:'get',
            dateType:'text',
            data:{
                'type':'device_info',
                'device_name':document.getElementById('device_name').value,
                'device_id':document.getElementById('device_id').value,
            },
            success:function(){
                document.getElementById('is_success').innerHTML='保存成功'
                document.getElementById('is_success').style.display='inline'
            },
            error:function(){
                document.getElementById('is_success').innerHTML='保存失败'
                document.getElementById('is_success').style.display='inline'
            }
        })
    }
    else{
        //$.ajax({
        //    url:'save_basic_config',
        //    type:'get',
        //    dateType:'text',
        //    data:{
        //        'type':'image',
        //        'snapshot_interval':document.getElementById('snapshot_interval').value,
        //    },
        //    success:function(data, status){
        //      if(data == "0"){
        //          document.getElementById('is_success').style.display='inline'
        //      }
        //
        //      else{
        //          document.getElementById('is_success').style.display='inline'
        //          document.getElementById('is_success').innerHTML='保存失败'
        //      }
        //
        //    }
        //})
    }
}

function clear_data(){
    is_deleting = true
    $.ajax({
        url:'clear',
        type:'get',
        dateType:'text',
        success:function(){
            is_deleting = false
            alert('数据清除成功!')
        },
        error:function(){
            is_deleting = false
            alert('数据清除失败!')
        }
    })
}

function device_reboot(){
    $.ajax({
        url:'reboot',
        type:'get',
        dateType:'text',
        error:function(){
            alert('重启失败')
        },
    })
}

