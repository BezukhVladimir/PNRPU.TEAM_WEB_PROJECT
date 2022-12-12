<?php

require_once '../config/connect.php';

$sql = "DELETE FROM films;";
mysqli_query($connect, $sql);
$sql = "ALTER TABLE films AUTO_INCREMENT = 1;";
mysqli_query($connect, $sql);