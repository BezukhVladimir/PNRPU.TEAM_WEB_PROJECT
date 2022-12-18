<?php

require_once '../config/connect.php';

$sql = "DELETE FROM clients;";
mysqli_query($connect, $sql);
$sql = "ALTER TABLE clients AUTO_INCREMENT = 1;";
mysqli_query($connect, $sql);