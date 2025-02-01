document.addEventListener("DOMContentLoaded", function() {
    // Validación de formulario en el login
    const loginForm = document.querySelector('form');
    
    loginForm.addEventListener('submit', function(event) {
        const usuario = document.getElementById('usuario').value;
        const contrasena = document.getElementById('contrasena').value;

        // Validación básica: no vacío
        if (usuario.trim() === '' || contrasena.trim() === '') {
            alert('Por favor, completa ambos campos.');
            event.preventDefault();
        }
    });

    // Si se necesita más interactividad o efectos, puedes agregarlos aquí.
});
