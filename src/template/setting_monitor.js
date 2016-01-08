/**
 * Created by server on 16-1-8.
 */
$("#bright_slider").slider({
        range:"min",
        min:0,
        max:100,
        value:{{brightness}},
        slide:function(event ,ui){
            $("#bright_value").val(ui.value);
    }
    });
    $("#contrast_slider").slider({
        range:"min",
        min:0,
        max:100,
        value:{{contrast}},
        slide:function(event ,ui){
            $("#contrast_value").val(ui.value);
    }
    });
    $("#saturation_slider").slider({
        range:"min",
        min:0,
        max:100,
        value:{{saturation}},
        slide:function(event ,ui){
            $("#saturation_value").val(ui.value);
    }
    });

document.getElementById('resolution').value = {{width}} + ',' + {{height}}
document.getElementById('framerate').value = {{framerate}}
document.getElementById('rotate').value = {{rotate}}
document.getElementById('snapshot_interval').value = {{snapshot_interval}}