/**
 * Created by server on 16-1-6.
 */

var is_downloading = false;

function alert_if_downloading(){
    if(is_downloading)
    return '文件下载中,您确定要离开当前页面?'
}

window.onbeforeunload = alert_if_downloading;

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

function download_image(){
    if(confirm('是否下载?')){
        is_downloading = true
        $.ajax({
            url:'download',
            async:false,
            type:'get',
            dataType:'text',
            success:function(data, status){
                if(data != ''){
                    var file_name = data
                    var href = '/static/download/'+file_name
                    //can_download = true
                    document.getElementById('download_link').href = href
                    document.getElementById('download_link').download = file_name
                    is_downloading = false
                    return true
                }
                else{
                    alert('获取数据失败!')
                    document.getElementById('download_link').href = ''
                    document.getElementById('download_link').download = ''
                    is_downloading = false
                    return false
                }
            },
            error:function(){
                    alert('获取数据失败!')
                    document.getElementById('download_link').href = ''
                    document.getElementById('download_link').download = ''
                    is_downloading = false
                    return false
            }
        })
    }
    else{
        //alert('获取数据失败!')
        document.getElementById('download_link').href = ''
        document.getElementById('download_link').download = ''
        return false
    }

}



