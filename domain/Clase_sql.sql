--sql

--DDL = CREATE, ALTER, DROP, TRUNCATE, RENAME #creacion de estructuras
--DML = SELET, INSERT, UPDATE, DELETE # modificacion de datos
--DCL = GRANT, REVOKE #comandos para garantizar seguridad y privilegios
--TCL = COMMIT, ROLLBACK #define cuando los cambios se guardan permanentemente
----------------------------------------en un scrip lo siguiente, para una tienda.----------
--crear base de datos
CREATE DATABASE tienda;
-- usar/seleccionar base de datos
USE tienda;
--crear las tablas clientes, productos y pedidos

--clientes
CREATE TABLE clientes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(50),
    pais VARCHAR(25)
);

--productos
CREATE TABLE productos(
    id INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL
);
--pedidos
CREATE TABLE pedidos(
    id INT PRIMARY KEY,
    cliente_id INT,
    producto_id INT,
    cantidad INT,
    fecha DATE,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

--SHOW TABLES muestra las tablas que estan creadas
--estructura de una tabla
--DESCRIBE nombre_de_tabla; 
--muestra la estructura y tipos de datos aceptados
--para ver la estructura codigo mas completa usar:
--SHOW CREATE TABLE nombre_de_tabla;
-- para eliminar una tabla:
--DROP TABLE nombre_tabla
-- para preguntar si existe y evitar errores de retorno:
--DROP TABLE IF EXISTS nombre_tabla;
--borrar base de datos:
--DROP DATABASE IF EXISTS nombre_db;
--añadir campos
--ALTER TABLE nombre_tabla ADD COLUMN nombre_campo tipoDeDato(long);
-- modificar un campo
--ALTER TABLE nombre_tabla MODIFY COLUMN nombre_campo tipoDeDato(long);
-- para ordenar hacer lo siguiente, seleccionar una tabla y una columna
--SELECT * FROM productos ORDER BY precio DESC; mayor a menor
--ahora limitamos la cantidad de ordenamientos o retornos:
--SELECT nombre AS producto, precio AS valor_unitario ORDER BY precio DESC LIMIT 10
-- el AS, renombra temporalmente los nombres de la tabla original para mostra en la tabla temporal ordenada
-- la tabla generada por el comando es temporal y visualmente, a no ser que se resguarde como temporary table o algo asi
-- se hara un promedio ahora conta
--SELECT COUNT(*) AS total_productos, AVG(precio) AS precio_promedio FROM productos;
-- la linea anterior selecciona todos las filas de productos, los cuenta, asigna ese resultado asu renombre,
-- luego realiza el recorrido y media arimetica de todos los precios y los renombra
-- agrupemos asumiendo que hay registros 
-- SELECT pais, COUNT(*) AS cantidad_clientes
--FROM clientes GROUP BY pais;
--realizaria totalizadores de cleintes por pais
--realizaremos otro agripamiento
--SELECT productos_id, SUM(cantidad) AS total_vendida
--FROM pedidos
--GROUP BY producto_id
--HAVING total_vendida > 10;

--obtienes por pantalla los productos que han sido vendidos mas de 10 veces

-- obtener los paises distintos de una tabla clientes
--SELECT DISTINCT pais FROM clientes;
-- para trabajar con rangos
--SELECT * FROM productos WHERE precio BETWEEN 500 AND 1500;
--traera toda la fila que este dentro esos rangos de precio
--hacer lo mismo con AN seria lo sigueinte
--SELECT * FROM clientes WHERE pais IN('argentina','chile');
--traeria todos los clientes dentro de esos 2 valores es decir
--todos los argentinos y chilenos.
-- usando comodines % se pueden traer patrones de inicio o x cosa
--SELECT * FROM clientes WHERE nombre LIKE "A%";
--traera los clientes que empiecen con A seguido de ningun o mas caracteres
-- el "_" es otro comodin que reprecenta el primer caracter o el ultimo, 
-- si colocaras _a% traera los nombres que empiecen con silavas con a, y las traeria
-- la mayusculas importan.
--sub consultas..
--SELECT * FROM productos WHERE id IN (
--SELECT producto_id FROM pedidos WHERE cantidad>=3);
-- traera todos los pedidos que superen la cantidad pedida de 3 o igual
-- estamos accediendo o realizando una consulta de una tabla A mediante otra consulta de tabla B
-- para obtener el maximo, minimo promedio se usa MAX,MIN o AVG
--SELECT nombre,precio FROM productos WHERE precio =(SELECT MAX(precio) FROM productos);
-- esto traera el nombre y precio del producto de mayor importe
-- JOIN's son para relacionar y acceder a elementos de 2 tablas relacionadas por claves foraneas
-- INNER JOIN, solo trae lo en comun de ambas
--LEFT join, requiere 2 argumentos y hace lo de arriba pero de una sola
-- RIGHT join viceverza
--ejemplo
--  SELECT pedidos.id AS "n° pedido",
        --clientes.nombre AS cliente,
        --productos.nombre AS producto,
        --pedidos.cantidad,
        --pedidos.fecha
        --FROM pedidos
        --INNER JOIN clientes ON pedidos.cliente_id = cliente.id
        --INNER JOIN productos ON pedidos.producto_id = producto.id;
-- analisis:
-- cuando realizas AS, das un nombre a las columnas de la tabla temporal generada por la consulta
--los demas nombres son de las tablas definidas en BD por lo que no es dificil relacionar
--deben tener campos en comun, en este caso pedidos tiene id's de cliente y producto por lo que
--genero 1 sola tabla mediante el acceso a esta
-- seria analogamente decir que:
-- BUSCAR EN clientes DENTRO DE pedidos.cliente_id EL QUE SEA IGUAL A cliente.id
-- diferencias entre el RIGHT y LEFT sera la predominancia en datos de la columna que se desea recuperar
-- por ejemplo si quieres saber de clientes y relacionar pedidos usa un LEFT JOIN para realizar la comparacion y retencion de daots
-- si decides traer datos de pedidos asociados a los productos usa un RIGHT JOIN sobre ambas tablas
-- ambas traeran datos incluso si no tienen datos asociados (NULL) en caso de no tener pedidos 
-- utilizar uno u otro dependera de cuantos campos clave o foraneas utiliza ademas de la predominancia entre la comparacion de deatos
-- la tabla que le sigua a FROM es izquierda y a JOIN derecha, la predominancia de datos es mas facil de ver de esta forma
    