<?php

require_once '../config/connect.php';

$sql = "DELETE FROM cinemas;";
mysqli_query($connect, $sql);
$sql = "ALTER TABLE cinemas AUTO_INCREMENT = 1;";
mysqli_query($connect, $sql);