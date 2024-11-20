// Когда html документ готов (прорисован)
$(document).ready(function () {
    // Ловим собыитие клика по кнопке удалить задачу
    $(document).on("click", ".remove-task", function (e) {
        // Блокируем его базовое действие
        e.preventDefault();
        // Получаем id задачу из атрибута data-task-id
        var task_id = $(this).data("task-id");
        // Из атрибута href берем ссылку на контроллер django
        var remove_task = $(this).attr("href");

        // делаем post запрос через ajax не перезагружая страницу
        $.ajax({
            type: "POST",
            url: remove_task,
            data: {
                task_id: task_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // Меняем содержимое задачи на ответ от django (новый отрисованный фрагмент разметки задачи)
                var todoListIdContainer = $("#todo-list-id");
                todoListIdContainer.html(data.task_items_html);
                console.log("data.task_items_html");

            },

            error: function (data) {
                console.log("Ошибка при удалении задачи");
            },
        });
    });

    $(document).on("click", ".task-is-done-update", function (e) {
        // Блокируем его базовое действие
        e.preventDefault();
        // Получаем id задачу из атрибута data-task-id и её состояние
        var task_id = $(this).data("task-id");
        var task_is_done = $(this).data("task-is-done");
        // Из атрибута href берем ссылку на контроллер django
        var update_task = $(this).attr("href");
        // делаем post запрос через ajax не перезагружая страницу
        $.ajax({
            type: "POST",
            url: update_task,
            data: {
                task_id: task_id,
                is_done: task_is_done,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // Меняем содержимое задачи на ответ от django (новый отрисованный фрагмент разметки задачи)
                var todoListIdContainer = $("#todo-list-id");
                todoListIdContainer.html(data.task_items_html);
                // console.log("data.task_items_html");

            },

            error: function (data) {
                console.log("Ошибка при изменении задачи");
                console.log(data);
            },
        });
    });
});