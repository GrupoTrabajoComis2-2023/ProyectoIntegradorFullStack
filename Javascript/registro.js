// REGISTRO
const passRegistro = document.getElementById('passRegistro');
const reingresoPassRegistro = document.getElementById('reingresoPassRegistro');
const buttonRegistrarme = document.getElementById('buttonRegistrarme');

const nameRegistro = document.getElementById('nameRegistro');
const lastnameRegistro = document.getElementById('lastnameRegistro');
const emailRegistro = document.getElementById('emailRegistro');



const validacionContrasena = () => {
    if (passRegistro.value !== reingresoPassRegistro.value){
        alert('La contraseñas no coinciden. Ingreselas nuevamente')
    }
};

const camposVacios = () => {
    if (passRegistro.value === "" || reingresoPassRegistro.value === "" || nameRegistro.value === "" || lastnameRegistro.value === "" || emailRegistro.value === ""){
        alert('Campos incompletos. Reingrese los campos nuevamente.')
    } else {
        registroUsuario()
    }
}

const registroUsuario = () => {
    if (passRegistro.value === reingresoPassRegistro.value) {
        alert('Usuario creado correctamente')
        window.location.href = "./index.html"
    } 
};

buttonRegistrarme.addEventListener('click', () => {  
    camposVacios()
    validacionContrasena()
});
