<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
$varservername="localhost";
$varusername="sepherot_andrer";
$varpassword="QxS7HbzfXBIb";
$vardbname="sepherot_andrerBD";

//crear conexxion
$varconexion = mysqli_connect($varservername,$varusername,$varpassword,$vardbname);
//revisar conexion
if(!$varconexion){
    die("fallo la conexion".mysqli_connect_error());
}
//devolver
else{
    echo"Conectado!!!";
    return $varconexion;
}
?>