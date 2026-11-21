CREATE DATABASE soda;
USE soda;

CREATE TABLE proveedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    telefono VARCHAR(100),
    correo VARCHAR(100),
    direccion VARCHAR(200)
);

INSERT INTO proveedores (nombre, telefono, correo, direccion) VALUES ('Dos Pinos', '24372000', 'ventas@dospinos.com', 'Alajuela');
INSERT INTO proveedores (nombre, telefono, correo, direccion) VALUES ('Panaderia La Central', '22334455', 'lacentral@gmail.com', 'San Jose centro');
INSERT INTO proveedores (nombre, telefono, correo, direccion) VALUES ('Verduras Don Carlos', '88776655', 'doncarlos@hotmail.com', 'Feria de Heredia');
