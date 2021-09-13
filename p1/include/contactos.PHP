<?php

function contactosALL(){
    include "conexion.php";
    $sql ="SELECT Nombre,Apellido, Correo, Pass, Comprador/Vendedor FROM T_Usuarios ";
    $result= mysqli_query($varconexion,$sql);
    mysqli_close($varconexion);
    return $result;
}

///funcion de insertar datos


?>