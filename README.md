# gesto-inventario-listas
Programa de consola en Python para administrar inventarios usando listas paralelas
Objetivo del Proyecto
El objetivo de este proyecto es implementar una aplicación de consola en Python para gestionar el inventario de una pequeña tienda (nombres de productos y sus cantidades disponibles). La solución está desarrollada aplicando conceptos fundamentales de lógica de programación como el uso de listas paralelas, ciclos, condicionales, funciones modulares y control de errores por entrada del usuario.
Requisitos para Ejecutar el Programa
•	Python 3.6 o superior instalado en el sistema.
•	No se requieren librerías ni dependencias externas (utiliza exclusivamente la librería estándar de Python).
Cómo ejecutar el programa
1.	Clonar el repositorio o descargar el archivo main.py.
2.	Abrir la terminal o consola de comandos en la carpeta donde se encuentra el archivo.
3.	Ejecutar el siguiente comando:
Python main.py
Instrucciones de Uso
Al ejecutar el programa, se desplegará un menú interactivo numerado del 1 al 8:
1.	Registrar un producto: Ingrese el nombre y la cantidad inicial del producto. Si el producto ya existe en el sistema, se le preguntará si desea adicionar unidades a la cantidad actual.
2.	Mostrar inventario completo: Muestra en pantalla el listado numerado de todos los productos junto con sus cantidades.
3.	Buscar un producto: Permite ingresar el nombre de un producto para verificar si se encuentra registrado y consultar su disponibilidad.
4.	Modificar cantidad de un producto: Permite establecer una nueva cantidad fija para un producto existente.
5.	Eliminar un producto: Elimina del registro tanto el nombre del producto como su cantidad correspondiente de forma limpia.
6.	Mostrar cantidad de productos diferentes: Muestra el conteo total de ítems distintos en el inventario.
7.	Mostrar producto con mayor cantidad: Identifica e informa cuál es el producto que posee más stock registrado.
1.	Salir: Finaliza la ejecución del programa.
Funciones Implementadas
•	registrar_producto(): Solicita el nombre y la cantidad disponible. Verifica si el producto ya existe (ignorando diferencias entre mayúsculas y minúsculas). Si existe, permite sumar inventario adicional; de lo contrario, lo agrega como un ítem nuevo mediante .append().
•	mostrar_inventario(): Recorre mediante un ciclo for las listas sincronizadas e imprime los productos en formato ordenado (1. Nombre - Cantidad unidades).
•	buscar_producto(): Realiza una búsqueda por coincidencia de texto dentro de la lista de productos y muestra la cantidad correspondiente si es hallado.
•	modificar_cantidad(): Ubica la posición del producto especificado y actualiza el valor almacenado en la lista cantidades.
•	eliminar_producto(): Remueve simultáneamente el elemento de ambas listas utilizando .pop(posicion) para mantener la sincronización y la integridad de los datos.
•	resumen_inventario(): Genera estadísticas sobre el inventario, calculando el total de productos únicos y hallando el de mayor disponibilidad mediante max() e index().
•	menu(): Controla la navegación del usuario mediante un bucle while True e interactúa con el usuario gestionando las entradas válidas e inválidas.
Sincronización de Listas Paralelas
El programa utiliza dos listas independientes (productos y cantidades). La coherencia de los datos se garantiza mediante el uso de índices compartidos: la información almacenada en productos[i] corresponde directamente con la cantidad almacenada en cantidades[i]. Cualquier operación de adición o eliminación se ejecuta siempre en ambas listas al mismo tiempo para preservar la paridad
