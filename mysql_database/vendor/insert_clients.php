<?php
require_once '../config/connect.php';
if (isset($_POST["email"])){
    $email = $connect->real_escape_string($_POST["email"]);
    $sql = "INSERT IGNORE INTO `clients` (`id`,`email`) VALUES (NULL, '$email')";
    mysqli_query($connect, $sql);
}