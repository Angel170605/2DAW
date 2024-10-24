document.getElementById('escudo').addEventListener('click', function() {
    let pos = 0;
    let id = setInterval(frame, 5);
    function frame() {
        if (pos == 350) {
            clearInterval(id);
        } else {
            pos++;
            document.getElementById('escudo').style.left = pos + 'px';
        }
    }
});
