const passRegistro = document.getElementById('passRegistro');
const reingresoPassRegistro = document.getElementById('reingresoPassRegistro');
const buttonRegistrarme = document.getElementById('buttonRegistrarme');


const registroUsuario = () => {
    if (passRegistro.value === reingresoPassRegistro.value) {
        alert('Usuario creado correctamente')
        window.location.href = "../index.html"
    } else {
        alert('Contraseña mal ingresada. Intente nuevamente.')
    }
};

buttonRegistrarme.addEventListener('click', () => {  
    registroUsuario()
});