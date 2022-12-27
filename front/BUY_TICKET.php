<?php 
	if (isset($_POST['username']) && $_POST['username'] && isset($_POST['password']) && $_POST['password']) 
    {
    echo json_encode(array('success' => 1));
	} else 
	{
    echo json_encode(array('success' => 0));
	}
?>