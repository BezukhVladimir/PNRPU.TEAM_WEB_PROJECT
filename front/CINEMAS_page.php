<!DOCTYPE html>

<?php
	include "database.php";

	$result = mysqli_query($connect, "SELECT * FROM `cinemas`");
?>

<html lang="en">
<head>
	<meta charset="UTF-8">
	<link rel='stylesheet' href='style.css'>
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,700;1,300&display=swap" rel="stylesheet">
	<title>Web Project</title>
</head>
<body>
	
<div class="header">
	<div class="container">
		<div class="header-line">
			<div class="header-logo">
				<img src="PNRPU_logo.png" width="100" height="100"alt="">
			</div>

			<div class="navigation">
				<a class="nav-item">КИНОТЕАТРЫ</a>
				<a class="nav-item" href="FILMS_page.php">ФИЛЬМЫ</a>
				<a class="nav-item" href="CLIENTS_page.php">КЛИЕНТЫ</a>
				<a class="nav-item" href="CLIENTS_ORDERS_page.php">ЗАКАЗЫ</a>
				<a class="nav-item" href="FILMS_SESSIONS_page.php">В ПРОКАТЕ</a>
				<a class="nav-item" href="@">О НАС</a>
			</div>

			<div class="cart">
				<a href="@">
					<img src="ticket.png" width="50" height="50" alt="">
				</a>
			</div>
			<div class="button">
				<a href="BUY_TICKET_page.php">Купить билет</a>
			</div>
		</div>

	</div>
	
</div>
	
<div class="container">
	
	<div class="films-items">
		
		<?php 
			while ($items = mysqli_fetch_assoc($result))
			{
				?>
				<films-item>
					<a href="@">
						<div class="films-text">
							<?php 
								echo $items['name']; 
							?>
						</div>
						<div class="films-subtext">
							<?php 
								echo $items['address']; 
							?>
						</div>
					</a>
				</films-item>
				<?php
			}
		?>

	</div>

	<div>

	</div>

</div>

</body>
</html>

