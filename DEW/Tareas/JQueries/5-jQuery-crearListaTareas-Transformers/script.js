$(document).ready(function() {
    $('#agregar-tarea').on('click', function() {
        const tareaTexto = $('#nueva-tarea').val().trim();
        if (tareaTexto) {
            const tareaHtml = `
                <li>
                    <span>${tareaTexto}</span>
                    <div class="iconos">
                        <button class="editar">Editar</button>
                        <button class="eliminar">Eliminar</button>
                    </div>
                </li>`;
            $('#lista-tareas').append(tareaHtml);
            $('#nueva-tarea').val('');
        } else {
            alert('Por favor, ingresa una misión.');
        }
    });

    $('#lista-tareas').on('click', '.editar', function() {
        const tareaLi = $(this).closest('li');
        const tareaTexto = tareaLi.find('span').text();
        const nuevaTarea = prompt('Editar misión:', tareaTexto);
        if (nuevaTarea) {
            tareaLi.find('span').text(nuevaTarea);
        }
    });

    $('#lista-tareas').on('click', '.eliminar', function() {
        $(this).closest('li').remove();
    });

    $('#lista-tareas').on('click', 'span', function() {
        $(this).parent().toggleClass('completed');
    });

    $('#limpiar-tareas').on('click', function() {
        $('#lista-tareas li.completed').remove();
    });
});