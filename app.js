

// const buttonRegistrarme = document.getElementById('buttonRegistrarme');
const nameRegistro = document.getElementById('nameRegistro');
const lastnameRegistro = document.getElementById('lastnameRegistro');
const emailRegistro = document.getElementById('emailRegistro');
// const passRegistro = document.getElementById('passRegistro');

const usuarioIngresado = document.getElementById('usuarioIngresado');

const nameContacto = document.getElementById('nameContacto');
const lastnameContacto = document.getElementById('lastnameContacto');
const emailContacto = document.getElementById('emailContacto');
const textareaContacto = document.getElementById('textareaContacto');
const btnFormulario = document.getElementById('btnFormulario');



let nameGuardado = sessionStorage.getItem('nameGuardado');
let lastnameGuardado = sessionStorage.getItem('lastnameGuardado');
let emailGuardado = sessionStorage.getItem('emailGuardado');
let passGuardado = sessionStorage.getItem('passGuardado');


// Guardando registro de usuario en local storage
// buttonRegistrarme.addEventListener('click', () => {    
//     sessionStorage.setItem('nameGuardado', nameRegistro.value);
//     sessionStorage.setItem('lastnameGuardado', lastnameRegistro.value);
//     sessionStorage.setItem('emailGuardado', emailRegistro.value);
//     sessionStorage.setItem('passGuardado', passRegistro.value);
// });


// // Ingresar usuario
// const iniciarSesion = () => {
//     if (correoUsuario === emailGuardado && passUsuario === passGuardado) {
//         alert('felicitaciones, usuario correcto')
//     } else {
//         alert('usuario o contraseña incorrecto')
//     }
// };

// ingresarButton.addEventListener('click', () => {    
//     alert('usuario ingresado')
//     iniciarSesion()
// });

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

// REGISTRO
// 2- Registro de Usuario. Mediante javascript se debe validar
// que la contraseña y el reingreso de la contraseña sean
// iguales. Si la validación tanto del formulario (html) como
// javascript pasa, entonces navegar a la página de login o
// inicio de sesión.
// const passRegistro = document.getElementById('passRegistro');
// const reingresoPassRegistro = document.getElementById('reingresoPassRegistro');
// const buttonRegistrarme = document.getElementById('buttonRegistrarme');

// const passRegistrado = passRegistro.value
// const reingresoPassRegistrado = reingresoPassRegistro.value

// const registroUsuario = () => {
//     if (passRegistrado === reingresoPassRegistrado) {
//         alert('Usuario creado correctamente')
//         window.location.href = "./index.html"
//     } else {
//         alert('Contraseña mal ingresada. Intente nuevamente.')
//     }
// };

// buttonRegistrarme.addEventListener('click', () => {  
//     registroUsuario()
//     console.log(passRegistrado)
//     console.log(reingresoPassRegistrado)
// });

// Validación formulario de contacto
// const btnEnviar = document.getElementById('btn-enviar');

// const validarFormContacto = (e) => {
//   e.preventDefault();
// //   const nombreDeUsuario = document.getElementById('usuario');
// //   const direcciónEmail = document.getElementById('email');
//   if (nameContacto.value === "") {
//     alert("Por favor, escribe tu nombre.");
//     nameContacto.focus();
//     return false;
//   }

//   if (lastnameContacto.value === "") {
//     alert("Por favor, escribe tu apellido.");
//     lastnameContacto.focus();
//     return false;
//   }
    
//   if (emailContacto.value === "") {
//     alert("Por favor, escribe tu correo electrónico.");
//     emailContacto.focus();
//     return false;
//   }

//   if (textareaContacto.value === "") {
//     alert("Por favor, escribe un mensaje.");
//     textareaContacto.focus();
//     return false;
//   }

//   if (!emailVálido(emailContacto.value)) {
//     alert("Por favor, escribe un correo electrónico válido");
//     emailContacto.focus();
//     return false;
//   }
  
//   return true; //Se pueden enviar los datos del formulario al servidor
// }

// const emailVálido = emailContacto => {
//   return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailContacto);
// }

// // btnFormulario.addEventListener('click', validarFormContacto);
// btnFormulario.addEventListener('click', () => {    
//     alert('validacion')
//     validarFormContacto()
// });


  

// Formularios login y registro con sus respectivas validaciones y
// mensajes personalizados al usuario. Ej. validar por tipos de inputs
// (text, number, email, date, select, segun lo que se requiera), agregar
// maxlenght y minlenght en los campos nombres, apellido, si solicitan
// DNI, usar MIN=1000000 MAX=99999999, por ejemplo.