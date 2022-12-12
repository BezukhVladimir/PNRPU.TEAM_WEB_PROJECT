<?php

require_once '../config/connect.php';
require_once 'insert_cinemas.php';

foreach($cinemas as $cinema) {
    $path = "../../web_scraper/data_saver/tables/" . $cinema[0] . "_films_sessions.csv";
    $cinema_id = "(SELECT id FROM cinemas WHERE name = '" . $cinema[0] . "' AND address = '" . $cinema[1] . "')";
    $films = [];
    $films_sessions = [];

    $rows = 0;
    if (($handle = fopen($path, 'r')) !== FALSE) {
        while (($data = fgetcsv($handle, 1000, ',')) !== FALSE) {
            $rows++;
            $films[] = $data;
            $data = fgetcsv($handle, 1000, ',');
            $films_sessions[] = $data;
        }

        fclose($handle);
    }

    foreach ($films as $film) {
        $sql = "INSERT IGNORE INTO `films`(`id`, `name`, `year`, `country`, `tags`) VALUES (NULL, '$film[0]', '$film[1]', '$film[2]', '$film[3]')";
        mysqli_query($connect, $sql);
        $film_id = "(SELECT id FROM films WHERE name = '" . $film[0] . "' AND year = '" . $film[1] . "' AND country = '" . $film[2] . "' AND tags = '" . $film[3] ."')";


        foreach ($films_sessions as $sessions) {
            for ($current = 0; $current < count($sessions); $current++) {
                $next = $current + 1;
                $sql = "INSERT IGNORE INTO `films_sessions`(`id`, `cinema_id`, `film_id`, `start_date`, `tickets_number`, `ticket_price`) VALUES (NULL, $cinema_id, $film_id, '$sessions[$current]', '50', '$sessions[$next]')";
                mysqli_query($connect, $sql);
                $current = $next;
            }
        }
    }
}