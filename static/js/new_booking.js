$(document).ready(function () {
    $("#id_booked_artist, #id_date, #id_time, #submit-booking").hide();
    $("#id_booked_style").change(function () {
        $("#id_date").hide();
        $("#id_time").hide();
        let selectedValue = $(this).val();
        if (selectedValue == 0){
            $("#id_booked_artist, #id_date, #id_time, #submit-booking").hide();
        }
        $.ajax({
            url: '/bookings/booking-options/',
            method: 'GET',
            data: {
                field_name: "#id_booked_style",
                selected_value: selectedValue},
            success: function (data) {
                $("#id_booked_artist").empty();
                for (let i = 0; i < data.options.length; i++) {
                    $("#id_booked_artist").append(data.options[i]);
                    if (selectedValue != 0){
                        $("#id_booked_artist").show();
                    }
                }
            }
        });
    });
    $("#id_booked_artist").change(function () {
        $("#id_date").val('');
        $("#id_time, #submit-booking").hide();
        let selectedValue = $(this).val();
        if (selectedValue == 0){
            $("#id_date, #id_time, #submit-booking").hide();
        }
        $.ajax({
            url: '/bookings/booking-options/',
            method: 'GET',
            data: {
                field_name: "#id_booked_artist",
                selected_value: selectedValue},
            success: function (data) {
                if (selectedValue != 0){
                    $("#id_date").show();
                }
            }
    });
    });
    $("#id_date").change(function () {
        $("#id_time, #submit-booking").hide();
        let selectedValue = $(this).val();
        $.ajax({
            url: '/bookings/booking-options/',
            method: 'GET',
            data: {
                field_name: "#id_date",
                selected_value: selectedValue},
                success: function (data) {
                    $("#id_time").empty();
                for (let i = 0; i < data.options.length; i++) {
                    $("#id_time").append(data.options[i]);
                    $("#id_time").show();
                }
            }
        });
    });
    $("#id_time").change(function () {
                    $("#submit-booking").show();
                });
});