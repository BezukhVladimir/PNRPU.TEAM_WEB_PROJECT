<?php

require_once '../config/connect.php';

$sql = "DELETE FROM clients_orders;";
mysqli_query($connect, $sql);
$sql = "ALTER TABLE clients_orders AUTO_INCREMENT = 1;";
mysqli_query($connect, $sql);