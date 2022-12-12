<?php

require_once '../config/connect.php';

$sql = "DELETE FROM films_sessions;";
mysqli_query($connect, $sql);
$sql = "ALTER TABLE films_sessions AUTO_INCREMENT = 1;";
mysqli_query($connect, $sql);