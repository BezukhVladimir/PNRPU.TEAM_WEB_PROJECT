<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);

global $connect;
$connect = mysqli_connect('localhost','WEB_PROJECT_2022','VT898sj6QG7V','web_project_2022');

if (!$connect) {
    die("Error connect to database!");
}