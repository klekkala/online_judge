<?php
$temp = $_GET['id'];
//echo $temp;
$file = fopen("test.txt","w");
echo fwrite($file,$temp);
fclose($file);
exec("python user_profile.py");
?>
