<?php
include "conexion.php";
$conn=$varconexion;

if ($conn->connect_error) {
    die("Fallo la conexion: " . $conn->connect_error);
} 

$sql= "

CREATE TABLE `T_Usuarios` (
  `Nombre` int(11) NOT NULL,
  `Apellido` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `Correo` varchar(250) COLLATE utf8_spanish_ci NOT NULL,
  `Password` varchar(250) COLLATE utf8_spanish_ci NOT NULL,
  `COMPRADOR/VENDEDOR` int(11) NOT NULL DEFAULT 1,
  `Foto` varchar(250) COLLATE utf8_spanish_ci NOT NULL()
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;


INSERT INTO `T_Usuarios` (`Nombre`,`Apellido`, `Correo`, `Password`, `Comprador/Vendedor`, `Foto`) VALUES
('Taylor','Swift', 'swift@email.com', '1taylor.jpg', 1, '2021-08-19 10:40:15'),
('Charlie','Melbourne' , 'kutcher@email.com', '2charlie.jpg', 2, '2021-08-19 10:40:15'),
('Jennifer','Tayer', 'danes@email.com', '3jennifer.jpg', 1, '2021-08-19 10:41:32'),
('Will','Taylor' , 'stiller@email.com', '4will.png', 2, '2021-08-19 10:41:32');


ALTER TABLE `T_Usuarios`
  ADD PRIMARY KEY (`Nombre`);


ALTER TABLE `T_Usuarios`
  MODIFY `Nombre` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
";

if ($conn->multi_query($sql) === TRUE) {
    echo "Tabla Creada.";
} else {
    echo "Error al intentar crear tabla: " . $conn->error;
}

$conn->close();

?>