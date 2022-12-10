<?php

$db = new PDO("mysql:host=127.0.0.1; dbname=cinemas_movies_db", "root", "");

if ($query = $db->query("SELECT * FROM cinemas_movies_db")) {
echo "<pre>";
	print_r($query->fetchAll(PDO::FETCH_ASSOC));
echo "</pre>";
} else {
	print_r($db->errorInfo());
}
?>