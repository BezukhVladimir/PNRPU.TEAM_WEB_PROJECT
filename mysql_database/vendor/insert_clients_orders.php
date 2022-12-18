<?php
require_once '../config/connect.php';
if (isset($_POST["email"]) && isset($_POST["cinemaname"]) && isset($_POST["filmname"]) && isset($_POST["email"]) &&
    isset($_POST["startdate"]) && isset($_POST["price"]) && isset($_POST["count"])){

    $email = $connect->real_escape_string($_POST["email"]);
    $film_name = $connect->real_escape_string($_POST["filmname"]);
    $cinema_name = $connect->real_escape_string($_POST["cinemaname"]);

    $tickets_purnashed = $connect->real_escape_string($_POST["count"]);

    $ticket_price = $connect->real_escape_string($_POST["price"]);
    $start_date = $connect->real_escape_string($_POST["startdate"]);
    //echo "start date". $start_date . "\n" ;
    $query1 = mysqli_query($connect,"SELECT id FROM `clients` WHERE `email` = '$email'");
    $client_id = mysqli_fetch_row($query1);
    //echo "client id" . $client_id[0] . "\n";
    $query2 = mysqli_query($connect,"SELECT id FROM `films` WHERE `name` = '$film_name'");
    $film_id =  mysqli_fetch_row($query2);
    //echo "film id". $film_id[0] . "\n";
    $query3 = mysqli_query($connect,"SELECT id FROM `cinemas` WHERE `name` = '$cinema_name'");
    $cinema_id =  mysqli_fetch_row($query3);
    //echo "cinema id" . $cinema_id[0] . "\n";
    $expended = $tickets_purnashed * $ticket_price;

    $query4 = mysqli_query($connect,"SELECT id FROM `films_sessions` WHERE cinema_id = $cinema_id[0] AND film_id = $film_id[0] AND start_date = '$start_date' AND ticket_price = $ticket_price;");
    $film_session_id = mysqli_fetch_row($query4);
    $query = mysqli_query($connect,"SELECT tickets_number FROM `films_sessions` WHERE id = $film_session_id[0]");
    $tickets = mysqli_fetch_row($query);
    $realtickets = $tickets[0] - $tickets_purnashed;
    // "tickets" . $realtickets . "\n";

    //echo "film sesssion id ". $film_session_id[0] . "\n";
    $sql = "INSERT IGNORE INTO `clients_orders` (`id`, `client_id`, `film_session_id`, `source`, `tickets_purchased`, `expended`) VALUES (NULL, $client_id[0], $film_session_id[0],'Mainpage', $tickets_purnashed, $expended);";
    mysqli_query($connect, $sql);
    mysqli_query($connect,"UPDATE `films_sessions` SET `tickets_number` = $realtickets WHERE `films_sessions`.`id` = $film_session_id[0]");

}