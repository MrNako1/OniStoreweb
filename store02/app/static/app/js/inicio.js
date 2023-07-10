$(document).ready(function(){
    $(".error").hide();
    $("#enviar").click(function(){
        var nombre="";
        nombre = $("#nombre").val();
        if (nombre.length != 0 && nombre.includes('@')&& nombre.includes('')){
            $(".error").hide();
        }else{
            $(".error").show();
        }
    });

});

$(document).ready(function(){
    $(".error2").hide();
    $("#enviar").click(function(){
        var contra="";
        contra = $("#contra").val();
        if (contra.length != 6){
            $(".error2").show();
        }else{
            $(".error2").hide();
        }
    });
});
