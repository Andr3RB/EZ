<?php

///$varnombre=htmlspecialchars($_POST['nombre']);
///$vartienda=htmlspecialchars($_POST['tienda']);
///$varemail=htmlspecialchars($_POST['c']);
///$varpassword =htmlspecialchars($_POST['p']);
///$varconfirmar=htmlspecialchars($_POST['cp']);
///echo $varnombre,$varemail,$varpassword,$varconfirmar;

 
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);
    include "include/conexion.php";
    $varnombre=$_POST['nombre'];
    $vartienda=$_POST['tienda'];
    $varemail=$_POST['c'];
    $varpassword =$_POST['p'];
    $varSalt=bin2hex(random_bytes(10));
    $varGPepper="ezzey";
    $pass_hash=hash('sha256',$varpassword.$varSalt.$varGPepper);
    $varconfirmar=$_POST['cp'];
    echo $varnombre,$vartienda,$varemail,$varpassword,$varconfirmar;
    $sql = "INSERT INTO T_Usuarios (Nombre,Tienda,Correo,Contrasena,Salt) VALUES('$varnombre','$vartienda','$varemail','$pass_hash','$varSalt')" ;
    $ejecucción=mysqli_query($varconexion,$sql);
    mysqli_close($varconexion);
    

    if (!$ejecucción){

        echo '{
        
        "success": false
        
        }';
        
        echo '<script>alert("Error de ejecucción")</script>';
        
        }else {
        
        echo '{
        
        "success": true
        
        }';
    }


/// mandar variable a funcion insertar avisar si se puede o no 
///conectar tabla de articulos
///articulo y adentro de ella la info , meter o id , marca o cantidad=comprador
///vendedor =misma tabla de los compradores= se debe ligar con la tienda 
////poder buscar comprador , tienda poder registrar
///tabla de tienda y arti conectada
////tabla compradores
?>