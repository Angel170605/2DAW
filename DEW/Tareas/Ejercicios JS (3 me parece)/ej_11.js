class Superman {
    volar() {
        document.getElementById('superman').style.position = 'absolute';
        let pos = 0;
        let id = setInterval(frame, 5);
        function frame() {
            if (pos == 350) {
                clearInterval(id);
            } else {
                pos--;
                document.getElementById('superman').style.bottom = pos + 'px';
            }
        }
    }
}

const superman = new Superman();
document.getElementById('superman').addEventListener('click', function() {
    superman.volar();
});
