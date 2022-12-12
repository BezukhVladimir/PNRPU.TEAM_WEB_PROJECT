<?php

require_once '../config/connect.php';

$path = "../../web_scraper/data_saver/tables/cinemas.csv";
$sql = "INSERT IGNORE `cinemas`(`id`, `name`, `address`) VALUES";

global $cinemas;
$cinemas = [];
$rows = 0;

if (($handle = fopen($path, 'r')) !== FALSE)
{
    while (($data = fgetcsv($handle, 1000, ',')) !== FALSE)
    {
        $rows++;
        $cinemas[] = $data;
    }

    fclose($handle);
}

foreach($cinemas as $cinema)
{
    $rows--;
    $sql .= "(NULL, '$cinema[0]', '$cinema[1]')";

    if ($rows !== 0)
        $sql .= ", ";
    else
        $sql .= ';';
}

mysqli_query($connect, $sql);