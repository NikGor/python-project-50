document.getElementById("formFile1").addEventListener("change", function () {
  var file = this.files[0];
  var reader = new FileReader();
  reader.onload = function () {
    document.querySelector("textarea[rows='10']").value = reader.result;
  };
  reader.readAsText(file);
});

document.getElementById("formFile2").addEventListener("change", function () {
  var file = this.files[0];
  var reader = new FileReader();
  reader.onload = function () {
    document.querySelectorAll("textarea[rows='10']")[1].value = reader.result;
  };
  reader.readAsText(file);
});


function validateForm() {
  let structure1 = document.forms["compareForm"]["Structure1"].value;
  let structure2 = document.forms["compareForm"]["Structure2"].value;

  if (structure1 == "" || structure2 == "") {
    alert("Please fill in both structures.");
    return false;
  }
}

// Функция для отправки данных на сервер и получения результата
function getDiffResult() {
  // Получаем данные из полей ввода
  const structure1 = $("#structure1").val();
  const structure2 = $("#structure2").val();

  // Получаем выбранный формат вывода
  const outputFormat = $("input[name='outputFormat']:checked").val();

  // Формируем объект для отправки
  const requestData = {
    "Structure1": structure1,
    "Structure2": structure2,
    "outputFormat": outputFormat
  };

  // Отправляем POST-запрос на API
  $.ajax({
    url: "/api/diff",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify(requestData),
    // В случае успешного ответа отображаем результат
    success: function(response) {
      // Заменяем экранированные переносы строк на реальные
      const formattedResult = response.result.replace(/\\n/g, '\n');
      $("#result-pre").text(formattedResult);

      // Показываем контейнер с результатом
      $("#result-container").show();
    },
    error: function(error) {
      // В случае ошибки отображаем сообщение об ошибке
      $("#result-pre").text("Произошла ошибка: " + JSON.stringify(error));

      // Показываем контейнер с результатом
      $("#result-container").show();
    }
  });
}

// Подключаем функцию к какому-либо событию (например, клик по кнопке с id="compareButton")
$("#compareButton").click(getDiffResult);
