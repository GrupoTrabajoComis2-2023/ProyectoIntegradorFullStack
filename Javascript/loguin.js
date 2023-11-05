// LOGUIN

const correoUsuario = document.getElementById('idEmail');
const passUsuario = document.getElementById('idPass');
const btnIngresar = document.getElementById('btnIngresar');


const correoGuardado = "juan@gmail.com"
const passwordGuardado = "juan1234"

const ingresarLoguin = () => {
    if (correoGuardado === correoUsuario.value && passwordGuardado === passUsuario.value) {
        alert('Usuario correcto')
        window.location.href = "./index.html"
    } else {
        alert('Usuario o contraseña erroneo, ingrese nuevamente')
    }
};

btnIngresar.addEventListener('click', () => {  
    ingresarLoguin()
});