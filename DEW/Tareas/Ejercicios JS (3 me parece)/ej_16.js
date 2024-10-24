function verificarPassword() {
    let password = document.getElementById('password').value;
    if (password === 'Vengadores') {
        document.getElementById('mensaje').innerText = 'Assemble!';
    }
}
