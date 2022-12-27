$(document).ready(function() {
    $('#registration_button').submit(function(e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: 'BUY_TICKET.php',
            data: $(this).serialize(),
            success: function(response)
            {
                var jsonData = JSON.parse(response);
                if (jsonData.success == "1")
                {
                    location.href = 'index.php';
                }
                else
                {
                    alert('Неверные данные!');
                }
           }
       });
     });
});