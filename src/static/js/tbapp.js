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

function download_image(){
    if(confirm('是否下载?')){
        $.ajax({
            url:'download',
            async:false,
            type:'get',
            dataType:'text',
            success:function(data, status){
                if(data != ''){
                    file_name = data
                    href = '/static/download/'+file_name
                    //can_download = true
                    document.getElementById('download_link').href = href
                    document.getElementById('download_link').download = file_name
                    return true
                }
                else{
                    alert('获取数据失败!')
                    document.getElementById('download_link').href = ''
                    document.getElementById('download_link').download = ''
                    return false
                }
            },
            error:function(){
                    alert('获取数据失败!')
                    document.getElementById('download_link').href = ''
                    document.getElementById('download_link').download = ''
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



