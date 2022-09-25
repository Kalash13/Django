
$.validator.addMethod("terminarPor", function(value, element, parametro){

    if(value.endswith(parametro)){
        return true;
    }

    return false;
}, "Debe terminar por {0}")



$("#formulario_contacto").validate({
    rules: {
        nombre: {
            requiered: true,
            minlength: 3,
            maxlength: 30
        },
        correo: {
            requiered: true,
            email: true,
            terminarPor: "duocuc.cl"
        },
        celular: {
            requiered: true,
            minlength: 8,
            maxlength: 11
        },
        mensaje: {
            requiered: true,
            minlength: 3,
            maxlength: 300
        }
    }
})


$("#enviar").click(function() {
    if($("#formulario_contacto").valid() == false) {
        return;
    }
    let nombre = $("#nombre").val()
    let correo = $("#correo").val()
    let celular = $("#celular").val()
    let mensaje = $("#mensaje").val()

    alert("enviado")
})