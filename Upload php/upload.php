<?php

use Aws\s3\Exception\bucketException;

require 'app/start.php';

if(isset($_FILES['file'])){

	$file = $_FILES['file'];

	// File Details
	$name = $file['name'];
	$tmp_name = $file['tmp_name'];

	$extension = explode('.',$name);
	$extension = strtolower(end($extension));
	var_dump($extension);

	//Temp details
	$key = md5(uniqid());
	$tmp_file_name = "{$key}.{$extension}";
	$tmp_file_path = "files/{tmp_file_name}";

	// Moving the file
	move_uploaded_file($tmp_name, $tmp_file_path);

	try{

		$s3->putObject([
			'Bucket' => $config['s3']['bucket'],
			'Key' => "*************folder in aws********/{$name}",
			'Body' => fopen($tmp_file_path, 'r'),
			'ACL' => 'public-read'
		]); 

		//remove the file
		unlink($tmp_file_path);

	} catch(bucketException $e){
		die("Error uploading file");
	}
}

?>

<!DOCTYPE html>
<html lang = "en">
	<head>
		<title> Upload </title>
	</head>
	<body>
		<form action="upload.php" method="post" enctype="multipart/form-data">
			<input type="file" name="file">
			<input type="submit" value="Upload">
		</form>
	</body>
</html>