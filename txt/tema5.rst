===
XML
===

Introducción
============

Los lenguajes de marcas como HTML tienen una orientación muy clara: describir páginas web.

En un contexto distinto, muy a menudo ocurre que es muy difícil intercambiar datos entre programas.

XML es un conjunto de tecnologías orientadas a crear nuestros propios lenguajes de marcas. A estos lenguajes de marcas "propios" se les denomina "vocabularios".

Un ejemplo sencillo
===================

.. code-block:: xml

	<clientes>
		<cliente>
			<nombre>AcerSA</nombre>
			<cif>5664332</cif>
		</cliente>
		<cliente>
			<nombre>Mer SL</nombre>
			<cif>5111444</cif>
		</cliente>
	</clientes>
	
	
	
Lo fundamental es que podemos crear nuestros propios "vocabularios" XML.


Construcción de XML
===================

Para crear XML es importante recordar una serie de reglas:

* XML es "case-sensitive", es decir que no es lo mismo mayúsculas que minúsculas y que por tanto no es lo mismo ``<cliente>``, que ``<Cliente>`` que ``<CLIENTE>``.

* Obligatorio: solo un elemento raíz.

* En general, la costumbre es poner todo en minúsculas.

* Solo se puede poner una etiqueta que empiece por letra o _. Es decir, esta etiqueta no funcionará en los programas ``<12Cliente>``.

* Aparte de eso, una etiqueta sí puede contener números, por lo que esta etiqueta sí es válida ``<Cliente12>``.

Validez
=======

Un documento XML puede "estar bien formado" o "ser válido". Se dice que un documento "está bien formado" cuando respeta las reglas XML básicas. Si alguien ha definido las reglas XML para un vocabulario, podremos además decir si el documento es válido o no, lo cual es mejor que simplemente estar bien formado.

Por ejemplo, los siguientes archivos ni siquiera están bien formados.

.. code-block:: xml

	<clientes>
		<cliente>
			<nombre>AcerSA
			<CIF>5666333</CIF>
		</cliente>
	</clientes>
	
En este caso la etiqueta ``<nombre>`` no está cerrada.

.. code-block:: xml

	<clientes>
		<cliente>
			<nombre>AcerSA</nombre>
			<cif>5666333</CIF>
		</cliente>
	</clientes>


En este caso, se ha puesto ``<cif>`` cerrado con ``</CIF>`` (mayúsculas).

.. code-block:: xml

	<clientes>
		<cliente>
			<nombre!>AcerSA</nombre!>
			<CIF>5666333</CIF>
		</cliente>
	</clientes>

Se ha utilizado la admiración, que no es válida.

Atención a este ejemplo:


.. code-block:: xml

	
	<cliente>
		<nombre>AcerSA</nombre>
		<CIF>5666333</CIF>
	</cliente>
	<cliente>
		<nombre>ACME</nombre>
		<CIF>455321</CIF>
	</cliente>
	
En este caso, el problema es que hay más de un elemento raíz.

En general, podemos asumir que un documento puede estar en uno de estos estados que de peor a mejor podríamos indicar así:

1. Mal formado (lo peor)
2. Bien formado.
3. Válido: está bien formado y además nos han dado las reglas para determinar si algo está bien o mal y el documento XML cumple dichas reglas. Este es el mejor caso.

Para determinar si un documento es válido o no, se puede usar el validador del W3C situado en http://validator.w3c.org

Gramáticas
==========

Pensemos en el siguiente problema, un programador crea aplicaciones con documentos que se almacenan así:

.. code-block:: xml

	<clientes>	
		<cliente>
			<nombre>AcerSA</nombre>
			<cif>455321</cif>
		</cliente>
		<cliente>
			<nombre>ACME</nombre>
			<cif>455321</cif>
		</cliente>
	</clientes>

	
Sin embargo, otro programador de la misma empresa lo hace así:



.. code-block:: xml

	<clientes>	
		<cliente>			
			<cif>455321</cif>
			<nombre>AcerSA</nombre>
		</cliente>
		<cliente>
			<cif>455321</cif>
			<nombre>ACME</nombre>
		</cliente>
	</clientes>

Está claro, que ninguno de los dos puede leer los archivos del otro, sería crítico ponerse de acuerdo en lo que se puede hacer, lo que puede aparecer y en qué orden debe hacerlo. Esto se hará mediante las DTD.

DTD significa Declaración de Tipo de Documento, y es un mecanismo para expresar las reglas sobre lo que se va a permitir y lo que no en archivos XML.

Por ejemplo, supongamos el mismo ejemplo ejemplo anterior en el que queremos formalizar lo que puede aparecer en un fichero de clientes. Se debe tener en cuenta que en un DTD se pueden indicar reglas para lo siguiente:

* Se puede indicar si un elemento aparece o no de forma opcional
* Se puede indicar si un elemento debe aparecer de forma obligatoria.
* Se puede indicar si algo aparecer una o muchas veces.
* Se puede indicar si algo aparece cero o muchas veces.


Supongamos que en nuestros ficheros deseamos indicar que el elemento raíz es ``<listaclientes>``. Dentro de ``<listaclientes>`` deseamos permitir uno o más elementos ``<cliente>``. Dentro de ``<cliente>`` todos deberán tener ``<cif>`` y ``<nombre>`` y en ese orden. Dentro de ``<cliente>`` puede aparecer o no un elemento ``<diasentrega>`` para indicar que ese cliente exige un máximo de plazos. Como no todo el mundo usa plazos el ``<diasentrega>`` es optativo.


Por ejemplo, este XML sí es válido:

.. code-block:: xml

	<listaclientes>
		<cliente>
			<cif>5676443</cif>
			<nombre>Mercasa</nombre>
		</cliente>
	</listaclientes>
	
Este también lo es:

.. code-block:: xml

	<listaclientes>
		<cliente>
			<cif>5676443</cif>
			<nombre>Mercasa</nombre>
			<diasentrega>30</diasentrega>
		</cliente>
	</listaclientes>
	
Este también:


.. code-block:: xml

	<listaclientes>
		<cliente>
			<cif>5676443</cif>
			<nombre>Mercasa</nombre>
			<diasentrega>30</diasentrega>
		</cliente>
		<cliente>
			<cif>5121554</cif>
			<nombre>Acer SL</nombre>
		</cliente>
	</listaclientes>

Sin embargo, estos no lo son:

.. code-block:: xml

	<listaclientes>
	</listaclientes>

Este archivo no tenía clientes (y era obligatorio al menos uno)

.. code-block:: xml

	<listaclientes>
		<cliente>
			<cif>5676443</cif>
			<diasentrega>30</diasentrega>
		</cliente>
	</listaclientes>

Este archivo no tiene nombre de cliente.

.. code-block:: xml

	<listaclientes>
		<cliente>
			<nombre>Mercasa</nombre>
			<cif>5676443</cif>
		</cliente>
		<cliente>
			<cif>5121554</cif>
			<nombre>Acer SL</nombre>
		</cliente>
	</listaclientes>

En este archivo no se respeta el orden cif, nombre.

Sintaxis DTD
----------------------------------------------

Una DTD es como un CSS, puede ir en el mismo archivo XML o puede ir en uno separado. Para poder subirlos al validador, meteremos la DTD junto con el XML.


La primera línea de todo XML debe ser esta:

.. code-block:: xml

	<?xml version="1.0"?>
	
	
Al final del XML pondremos los datos propiamente dichos

.. code-block:: xml

	<listaclientes>
		<cliente>
			<nombre>Mercasa</nombre>
			<cif>5676443</cif>
		</cliente>
		<cliente>
			<cif>5121554</cif>
			<nombre>Acer SL</nombre>
		</cliente>
	</listaclientes>

	
La DTD tiene esta estructura

.. code-block:: dtd

	<!DOCTYPE listaclientes [
			<!ELEMENT listaclientes (cliente+)>
			<!ELEMENT cliente (nombre, cif, diasentrega?)>
			<!ELEMENT nombre (#PCDATA)>
			<!ELEMENT cif (#PCDATA)>
			<!ELEMENT diasentrega (#PCDATA)>
			]
		>

Esto significa lo siguiente:

* Se establece el tipo de documento ``listaclientes`` que consta de una serie de elementos (dentro del corchete)
* Un elemento ``listaclientes	`` consta de uno o más clientes. El signo ``+`` significa "uno o más".
* Un cliente tiene un nombre y un cif. También puede tener un elemento ``diasentrega`` que puede o no aparecer (el signo ``?`` significa "0 o 1 veces").
* Un ``nombre`` no tiene más elementos dentro, solo caracteres (``#PCDATA``)
* Un ``CIF`` solo consta de caracteres.
* Un elemento ``diasentrega`` consta solo de caracteres.

La solución completa sería así:


.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>
	<!DOCTYPE listaclientes [
			<!ELEMENT listaclientes (cliente+)>
			<!ELEMENT cliente (nombre, cif, diasentrega?)>
			<!ELEMENT nombre (#PCDATA)>
			<!ELEMENT cif (#PCDATA)>
			<!ELEMENT diasentrega (#PCDATA)>
		]>
	<listaclientes>
		<cliente>
			<nombre>Mercasa</nombre>
			<cif>5676443</cif>
		</cliente>
		<cliente>			
			<nombre>Acer SL</nombre>
			<cif>5121554</cif>
		</cliente>
	</listaclientes>
	
Ejercicio I (DTD)
===================================================
Unos programadores necesitan un formato de fichero para que sus distintos programas intercambien información sobre ventas. El acuerdo al que han llegado es que su XML debería tener esta estructura:

* El elemento raíz será ``<listaventas>``
* Toda ``<listaventas>`` tiene una o más ventas.
* Toda ``<venta>`` tiene los siguientes datos: 

	* Importe.	
	* Comprador.
	* Vendedor.
	* Fecha (optativa).
	* Un codigo de factura.


.. code-block:: xml

	<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE listaventas[
	  <!ELEMENT listaventas (venta+)>
	  <!ELEMENT venta (importe, comprador, vendedor, fecha?, codigofactura)>
	  <!ELEMENT importe (#PCDATA)>
	  <!ELEMENT comprador (#PCDATA)>
	  <!ELEMENT vendedor (#PCDATA)>
	  <!ELEMENT fecha (#PCDATA)>
	  <!ELEMENT codigofactura (#PCDATA)>
	  
	]>

	<listaventas>
	  <venta>
		<importe>1500</importe>
		<comprador>Wile E.Coyote</comprador>
		<vendedor>ACME</vendedor>
		<codigofactura>E17</codigofactura>
	  </venta>
	  <venta>
		<importe>750</importe>
		<comprador>Elmer Fudd</comprador>
		<vendedor>ACME</vendedor>
		<fecha>27-2-2015</fecha>
		<codigofactura>E18</codigofactura>
	  </venta>
	</listaventas>   
	
Ejercicio II (DTD)
===========================================

Crear un XML de ejemplo y la DTD asociada para unos programadores que programan una aplicación de pedidos donde hay una lista de pedidos con 0 o más pedidos. Cada pedido tiene un número de serie, una cantidad y un peso que puede ser opcional.

Solución
----------------------------------------------
Este ejemplo es un documento XML válido.

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>

	<!DOCTYPE listapedidos [
		<!ELEMENT listapedidos (pedido*)>
		<!ELEMENT pedido (numeroserie, cantidad, peso?)>
		<!ELEMENT numeroserie (#PCDATA)>
		<!ELEMENT cantidad (#PCDATA)>
		<!ELEMENT peso (#PCDATA)>
	]>

	<listapedidos>
	</listapedidos>




Este documento **no es válido**

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>

	<!DOCTYPE listapedidos [
		<!ELEMENT listapedidos (pedido*)>
		<!ELEMENT pedido (numeroserie, cantidad, peso?)>
		<!ELEMENT numeroserie (#PCDATA)>
		<!ELEMENT cantidad (#PCDATA)>
		<!ELEMENT peso (#PCDATA)>
	]>

	<listapedidos>
		<pedido>
			<numeroserie>23332244</numeroserie>
		</pedido>
	</listapedidos>
	

Este documento **sí es válido**. Las DTD solo se ocupan de determinar qué elementos hay y en qué orden, pero no se ocupan de lo que hay dentro de los elementos.

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>

	<!DOCTYPE listapedidos [
		<!ELEMENT listapedidos (pedido*)>
		<!ELEMENT pedido (numeroserie, cantidad, peso?)>
		<!ELEMENT numeroserie (#PCDATA)>
		<!ELEMENT cantidad (#PCDATA)>
		<!ELEMENT peso (#PCDATA)>
	]>

	<listapedidos>
		<pedido>
			<numeroserie>23332244</numeroserie>
			<cantidad>ññlñ</cantidad>
		</pedido>
	</listapedidos>

Ejercicio (con atributos)
===========================

Unos programadores necesitan estructurar la información que intercambiarán los ficheros de sus aplicaciones para lo cual han determinado los requisitos siguientes:

* Los ficheros deben tener un elemento ``<listafacturas>``
* Dentro de la lista debe haber una o más facturas.
* Las facturas tienen un atributo ``fecha`` que es optativo.
* Toda factura tiene un ``emisor``, que es un elemento obligatorio y que debe tener un atributo ``cif`` que es obligatorio. Dentro de ``emisor`` debe haber un elemento ``nombre``, que es obligatorio y puede o no haber un elemento ``volumenventas``.
* Toda factura debe tener un elemento ``pagador``, el cual tiene exactamente la misma estructura que ``emisor``.
* Toda factura tiene un elemento ``importe``.

Solución ejercicio con atributos
------------------------------------------------------

La siguiente DTD refleja los requisitos indicados en el enunciado.

.. code-block:: dtd

	<!ELEMENT listafacturas (factura+)>
	<!ELEMENT factura (emisor, pagador, importe)>
	<!ATTLIST factura fecha CDATA #IMPLIED>
	<!ELEMENT emisor (nombre, volumenventas?)>
	<!ELEMENT nombre (#PCDATA)>
	<!ATTLIST emisor cif CDATA #REQUIRED>
	<!ELEMENT volumenventas (#PCDATA)>
	<!ELEMENT pagador (nombre, volumenventas?)>
	<!ATTLIST pagador cif CDATA #REQUIRED>
	<!ELEMENT importe (#PCDATA)>

Y el XML siguiente refleja un posible documento. Puede comprobarse que es válido con respecto a la DTD.

.. code-block:: xml

	<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE listafacturas SYSTEM "ListaFacturas.dtd">
	<listafacturas>
	  <factura fecha="11-2-2015">
		<emisor cif="123">
		  <nombre>ACME</nombre>
		</emisor>
		<pagador cif="234">
		  <nombre>ACME Inc</nombre>
		  <volumenventas>2000</volumenventas>
		</pagador>
		<importe>2500</importe>
	  </factura>
	</listafacturas>


Ejercicio
=========

Un instituto necesita registrar los cursos y alumnos que estudian en él y necesita una DTD para comprobar los documentos XML de los programas que utiliza:

* Tiene que haber un elemento raíz ``listacursos``. Tiene que haber uno o más cursos.
* Un curso tiene uno o más alumnos
* Todo alumno tiene un DNI, un nombre y un apellido, puede que tenga segundo apellido o no.
* Un alumno escoge una lista de asignaturas donde habrá una o más asignaturas. Toda asignatura tiene un nombre, un atributo código y un profesor.
* Un profesor tiene un NRP (Número de Registro Personal), un nombre y un apellido (también puede tener o no un segundo apellido).
	
	
Solución punto 1
----------------------------------------------

La raíz es ``listacursos`` y tiene uno o más cursos

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>

	<!DOCTYPE listacursos [
		<!ELEMENT listacursos (curso+)>
	]>
	
Solución punto 2
----------------------------------------------
Un curso tiene uno o más elementos ``alumno``.

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>

	<!DOCTYPE listacursos [
		<!ELEMENT listacursos (curso+)>
		<!ELEMENT curso (alumno+)>
	]>		

	
Solución punto 3
----------------------------------------------
Todo alumno tiene DNI, nombre y apellido 1, pero puede que tenga el segundo o no

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>

	<!DOCTYPE listacursos [
		<!ELEMENT listacursos (curso+)>
		<!ELEMENT curso (alumno+)>
		<!ELEMENT alumno (dni, nombre, ap1, ap2?)>
	]>	
	
Solución al punto 4
----------------------------------------------
Todo alumno tiene una lista de asignaturas que consta de una o más asignaturas. Ampliamos el elemento alumno:

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>

	<!DOCTYPE listacursos [
		<!ELEMENT listacursos (curso+)>
		<!ELEMENT curso (alumno+)>
		<!ELEMENT alumno (dni, nombre, ap1, ap2?, listaasignaturas)>
		<!ELEMENT listaasignaturas (asignatura+)
	]>
	
	
Solución punto 5
----------------------------------------------
Una posible solución implicaría usar dos elementos ``nombre``. *Está permitido* pero solo si ambos elementos se usan de la misma forma (por ejemplo que usen ``(#PCDATA)``. Para evitar problemas cambiaremos algunos nombres de elementos.

Este punto pedía contemplar que una asignatura tiene un nombre, un código y un profesor.

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>

	<!DOCTYPE listacursos [
		<!ELEMENT listacursos (curso+)>
		<!ELEMENT curso (alumno+)>
		<!ELEMENT alumno (dni, nombre_alumno, ap1, ap2?, listaasignaturas)>
		<!ELEMENT listaasignaturas (asignatura+)>
		<!ELEMENT asignatura (nombre_asig, profesor)>
		<!ATTLIST asignatura codigo CDATA #REQUIRED>
		<!ELEMENT nombre_asig (#PCDATA)>
	]>	
	
	
Solución punto 6
----------------------------------------------
Se indica que un profesor tiene una serie de elementos dentro. Aquí hay un claro ejemplo en el que repetir el elemento ``ap1`` o el ``ap2`` hubiera sido apropiado, ya que los apellidos de alumnos o profesores en realidad no se distinguen en nada.


.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>

	<!DOCTYPE listacursos [
		<!ELEMENT listacursos (curso+)>
		<!ELEMENT curso (alumno+)>
		<!ELEMENT alumno (dni, nombre_alumno, ap1, ap2?, listaasignaturas)>
		<!ELEMENT listaasignaturas (asignatura+)>
		<!ELEMENT asignatura (nombre_asig, profesor)>
		<!ATTLIST asignatura codigo CDATA #REQUIRED>
		<!ELEMENT nombre_asig (#PCDATA)>
		<!ELEMENT profesor (nrp, nombre_prof, ap_prof1, ap_prof2?)>
	]>
	
Solución completa
----------------------------------------------
.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>

	<!DOCTYPE listacursos [
		<!ELEMENT listacursos (curso+)>
		<!ELEMENT curso (alumno+)>
		<!ELEMENT alumno (dni, nombre_alumno, ap1, ap2?, listaasignaturas)>
		<!ELEMENT listaasignaturas (asignatura+)>
		<!ELEMENT asignatura (nombre_asig, profesor)>
		<!ATTLIST asignatura codigo CDATA #REQUIRED>
		<!ELEMENT nombre_asig (#PCDATA)>
		<!ELEMENT profesor (nrp, nombre_prof, ap_prof1, ap_prof2?)>
		
		<!ELEMENT dni (#PCDATA)>
		<!ELEMENT nombre_alumno (#PCDATA)>
		<!ELEMENT ap1 (#PCDATA)>
		<!ELEMENT ap2 (#PCDATA)>
		<!ELEMENT nrp (#PCDATA)>
		<!ELEMENT nombre_prof (#PCDATA)>
		<!ELEMENT ap_prof1 (#PCDATA)>
		<!ELEMENT ap_prof2 (#PCDATA)>
	]>


	<listacursos>
		<curso>
			<alumno>
				<dni>1234567</dni>
				<nombre_alumno>Juan</nombre_alumno>
				<ap1>Sanchez</ap1>
				<listaasignaturas>
					<asignatura>
						<nombre_asig>
						  Lenguajes de marcas
						</nombre_asig>
						<codigo>
						  XML-DAM1
						</codigo>
						<profesor>
							<nrp>
							  03409435898W0303
							</nrp>
							<nombre_prof>
							  Andres
							</nombre_prof>
							<ap_prof1>
							  Ruiz
							</ap_prof1>
						</profesor>
					</asignatura>
				</listaasignaturas>
			</alumno>
		</curso>
	</listacursos>

	
	




Otras características de XML
============================

Atributos
----------------------------------------------

Un atributo XML funciona exactamente igual que un atributo HTML, en concreto un atributo es un trozo de información que acompaña a la etiqueta, en lugar de ir dentro del elemento.

.. code-block:: xml

	<pedido codigo="20C">
		<contenido>
			...
	</pedido>
	
En este caso, la etiqueta ``pedido`` tiene un atributo ``codigo``.

¿Cuando debemos usar atributos y cuando debemos usar elementos? Resulta que el ejemplo anterior también se podría haber permitido hacerlo así:

.. code-block:: xml

	<pedido>
		<codigo>20C</codigo>
		<contenido>
			...
	</pedido>

Hay muchas discusiones sobre qué meter dentro de elemento o atributo. Sin embargo, los expertos coinciden en señalar que en caso de duda es mejor el segundo.

La definición de atributos se hace por medio de una directiva llamada ``ATTLIST``. En concreto si quisieramos permitir un atributo ``código`` en el elemento ``pedido`` se haría algo así.

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>
	<!DOCTYPE pedido[
		<!ELEMENT pedido (contenido)>
		<!ELEMENT contenido (#PCDATA)>
		<!ATTLIST pedido codigo CDATA #REQUIRED>
	]>

	<pedido codigo="20C">
		<contenido>Pedido de cosas</contenido>
	</pedido>
		
En concreto este código pone que el elemento ``pedido`` tiene un atributo ``código`` con datos carácter dentro y que es obligatorio que esté presente (un atributo optativo en vez de ``#REQUIRED`` usará ``#IMPLIED``)

Si probamos esto, también validará porque el atributo es *optativo*

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>
	<!DOCTYPE pedido[
		<!ELEMENT pedido (contenido)>
		<!ELEMENT contenido (#PCDATA)>
		<!ATTLIST pedido codigo CDATA #IMPLIED>
	]>

	<pedido>
		<contenido>Pedido de cosas</contenido>
	</pedido>





Elementos vacíos
----------------------------------------------

En ocasiones, un elemento en especial puede interesarnos que vaya vacío porque simplemente no contiene mucha información de relevancia. Por ejemplo en HTML podemos encontrarnos esto:

.. code-block:: html

	<b>Texto texto...</b>
	<br/>
	
Los elementos vacíos suelen utilizar para indicar pequeñas informaciones que no deseamos meter en atributos y que de todas formas tampoco son de demasiada relevancia.

Un elemento vacío se indica poniendo ``EMPTY`` en lugar de ``#PCDATA``

Por supuesto, estas dos formas de usar un atributo son válidas:

.. code-block:: xml

	<pedido>
		<pagado></pagado>
		<contenido>...</contenido>
	</pedido>
	
.. code-block:: xml

	<pedido>
		<pagado/>
		<contenido>...</contenido>
	</pedido>

	
La definición completa sería así:

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>
	<!DOCTYPE pedido[
		<!ELEMENT pedido (pagado?,contenido)>
		<!ELEMENT pagado EMPTY>
		<!ELEMENT contenido (#PCDATA)>
		<!ATTLIST pedido codigo CDATA #IMPLIED>
	]>

	<pedido>
		<pagado/>
		<contenido>Pedido de cosas</contenido>
	</pedido>
	
	
Alternativas
----------------------------------------------

Hasta ahora hemos indicado elementos donde un elemento puede aparecer o puede no aparecer, pero ¿qué ocurre si deseamos obligar a que aparezca una posibilidad entre varias?


Por ejemplo, supongamos que en un nuestro ejemplo de pedidos deseamos indicar si el pedido se entregó en almacén o a domicilio. A la fuerza todo pedido se entrega de alguna manera, sin embargo queremos exigir que en los XML aparezca una de esas dos alternativas. Los elementos alternativos se indican con la barra vertical ``almacen|domicilio``

Una tentación sería hacer esto (que está **mal**):

.. code-block:: xml

	<!DOCTYPE pedido[
		<!ELEMENT pedido (pagado?, contenido, almacen?,domicilio?)>
		<!ELEMENT pagado EMPTY>
		<!ELEMENT contenido (#PCDATA)>
		<!ELEMENT almacen (#PCDATA)>
		<!ELEMENT domicilio (#PCDATA>
	]>

Está mal porque se permite esto:

.. code-block:: xml

	<pedido>
		<pagado/>
		<contenido>Ordenadores</contenido>
		<almacen>Entregado el 20-2-2011</almacen>
		<domicilio>Entregado el 20-2011</domicilio>
	</pedido>
	
La forma **correcta** es esta:

.. code-block:: xml

	<!DOCTYPE pedido[
		<!ELEMENT pedido (pagado?, contenido, (almacen|domicilio)?>
		<!ELEMENT pagado EMPTY>
		<!ELEMENT contenido (#PCDATA)>
		<!ELEMENT almacen (#PCDATA)>
		<!ELEMENT domicilio (#PCDATA>
	]>
	<pedido>
		<contenido>Ordenadores</contenido>
	</pedido>
	
Ejercicio
===========================================

Un mayorista informático necesita especificar las reglas de los elementos permitidos en las aplicaciones que utiliza en sus empresas, para ello ha indicado los siguientes requisitos:

* Una entrega consta de uno o más lotes.
* Un lote tiene uno o más palés
* Todo palé tiene una serie de elementos: número de cajas, contenido y peso y forma de manipulación.
* El contenido consta de una serie de elementos: nombre del componente, procedencia (puede aparecer 0, 1 o más países), número de serie del componente, peso del componente individual y unidad de peso que puede aparecer o no.

Solución
----------------------------------------------

Observa como en la siguiente DTD se pone ``procedencia?`` y dentro de ella ``pais+``. Esto nos permite que si aparece la procedencia se debe especificar uno o más países. Sin embargo si no queremos que aparezca ningun pais, el XML **no necesita contener un elemento vacío**.

.. code-block:: dtd

	<!ELEMENT entrega (lote+)>
	<!ELEMENT lote (pale+)>
	<!ELEMENT pale (numcajas, contenido, peso, formamanipulacion?)>
	<!ELEMENT numcajas (#PCDATA)>
	<!ELEMENT peso (#PCDATA)>
	<!ELEMENT formamanipulacion (#PCDATA)>
	<!ELEMENT contenido (nombrecomponente, procedencia?, 
				numserie, peso, unidades)>
	<!ELEMENT nombrecomponente (#PCDATA)>
	<!ELEMENT procedencia (pais+)>
	<!ELEMENT pais (#PCDATA)>
	<!ELEMENT numserie (#PCDATA)>
	<!ELEMENT unidades (#PCDATA)>


.. code-block:: xml

	<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE entrega SYSTEM "mayorista.dtd">
	<entrega>
	  <lote>
		<pale>
		  <numcajas>3</numcajas>
		  <contenido>
			<nombrecomponente>Fuentes</nombrecomponente>
			<numserie>3A</numserie>
			<peso>2kg</peso>
			<unidades>50</unidades>
		  </contenido>
		  <peso>100kg</peso>
		  <formamanipulacion>Manual</formamanipulacion>
		</pale>
	  </lote>
	  <lote>
		<pale>
		  <numcajas>2</numcajas>
		  <contenido>
			<nombrecomponente>CPUs</nombrecomponente>
			<procedencia>
			  <pais>China</pais>
			  <pais>Corea del Sur</pais>
			</procedencia>
			<numserie>5B</numserie>
			<peso>100g</peso>
			<unidades>1000</unidades>
		  </contenido>
		  <peso>100kg</peso>
		  <formamanipulacion>Manual</formamanipulacion>
		</pale>
	  </lote>
	</entrega>

Ejercicio: mayorista de libros
======================================
Se desea crear un formato de intercambio de datos para una empresa mayorista de libros con el fin de que sus distintos programas puedan manejar la información interna. El formato de archivo debe tener la siguiente estructura:

* Un archivo tiene una serie de operaciones dentro.
* Las operaciones pueden ser "venta", "compra", o cualquier combinación y secuencia de ellas, pero debe haber al menos una.
* Una venta tiene: 

	* Uno o más títulos vendidos.
	* La cantidad total de libros vendidos.
	* Puede haber un elemento "entregado" que indique si la entrega se ha realizado.
	* Debe haber un elemento importe con un atributo obligatorio llamado "moneda".
	
* Una compra tiene:

	* Uno o más títulos comprados.
	* Nombre de proveedor.
	* Una fecha de compra, que debe desglosarse en elementos día, mes y año

Solución al mayorista de libros
------------------------------------------------------


Ejercicio: fabricante de tractores
===========================================

Un fabricante de tractores desea unificar el formato XML de sus proveedores y para ello ha indicado que necesita que los archivos XML cumplan las siguientes restricciones:

* Un pedido consta de uno o más tractores.
* Un tractor consta de uno o más componentes.
* Un componente tiene los siguientes elementos: nombre del fabricante (atributo obligatorio), fecha de entrega  (si es posible, aunque puede que no aparezca, si aparece el dia es optativo, pero el mes y el año son obligatorios). También se necesita saber del componente si es frágil o no. También debe aparecer un elemento peso del componente y dicho elemento peso tiene un atributo unidad del peso (kilos o gramos), un elemento número de serie y puede que aparezca o no un elemento km_maximos indicando que el componente debe sustituirse tras un cierto número de kilómetros.

Una posible solución sería esta (aunque se puede mejorar en algunos aspectos):

.. code-block:: dtd

	<!ELEMENT pedido (tractor+)>
	<!ELEMENT tractor (componente+)>
	<!ELEMENT componente (fecha?, peso, fragil?, km_maximos?)>
	<!ELEMENT fragil EMPTY>
	<!ELEMENT peso (#PCDATA)>
	<!ELEMENT km_maximos (#PCDATA)>
	<!ATTLIST componente nombre_fabricante CDATA #REQUIRED>
	<!ATTLIST peso unidades CDATA #IMPLIED>
	<!ELEMENT fecha (dia?, mes, anio)>
	<!ELEMENT dia (#PCDATA)>
	<!ELEMENT mes (#PCDATA)>
	<!ELEMENT anio (#PCDATA)>   

Un ejemplo de XML sería este:

.. code-block:: xml

	<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE pedido SYSTEM "tractores.dtd">
	<pedido>
	  <tractor>
		<componente nombre_fabricante="John Deere">
		  <peso unidades="kilos">2.5</peso>
		  <fragil/>
		</componente>
		<componente nombre_fabricante="Agrotrans">
		  <peso unidades="gramos">50</peso>
		</componente>
	  </tractor>
	  <tractor>
		<componente nombre_fabricante="John Deere">
		  <fecha>
			<mes>Enero</mes>
			<anio>2015</anio>
		  </fecha>
		  <peso>150</peso>
		  <fragil/>
		</componente>
		<componente nombre_fabricante="Agrotrans">
		  <peso unidades="gramos">50</peso>
		</componente>
	  </tractor>
	</pedido> 

Ejercicio: repeticiones de opciones
===================================

Se necesita un formato de archivo para intercambiar productos entre almacenes de productos de librería y se desea una DTD que incluya estas restricciones:

* Debe haber un elemento raíz pedido que puede constar de libros, cuadernos y/o lápices. Los tres elementos pueden aparecer repetidos y en cualquier orden. Tambien pueden aparecer por ejemplo 4 libros, 2 lapices y luego 4 lapices de nuevo.
* Todo libro tiene un atributo obligatorio titulo.
* Los elementos cuaderno tiene un atributo optativo num_hojas.
* Todo elemento lápiz debe tener dentro un  elemento obligatorio número.

La solución a la DTD:

.. code-block:: dtd

	<!ELEMENT pedido (libro|cuaderno|lapiz)+>
	<!ELEMENT libro (#PCDATA)>
	<!ATTLIST libro titulo CDATA #REQUIRED>
	<!ELEMENT cuaderno (#PCDATA)>
	<!ATTLIST cuaderno num_hojas CDATA #IMPLIED>
	<!ELEMENT lapiz (numero)>
	<!ELEMENT numero (#PCDATA)>


   

.. code-block:: xml

	<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE pedido SYSTEM "libreria.dtd">
	<pedido>
	  <libro titulo="Java 8"></libro>
	  <cuaderno></cuaderno>
	  <libro titulo="HTML y CSS"/>
	  <libro titulo="SQL para Dummies"/>
	  <cuaderno num_hojas="150"/>
	  <lapiz>
		<numero>2H</numero>
	  </lapiz>
	  <cuaderno num_hojas="250"/>
	  <cuaderno num_hojas="100"/>
	  <lapiz>
		<numero>2B</numero>
	  </lapiz>
	  <lapiz>
		<numero>1HB</numero>
	  </lapiz>
	</pedido>   
Ejercicio
=========

Una multinacional que opera en bolsa necesita un formato de intercambio de datos para que sus programas intercambien información sobre los mercados de acciones.

En general todo archivo constará de un listado de cosas como se detalla a continuación


* En el listado aparecen siempre uno o varios futuros, despues una o varias divisas, despues uno o varios bonos y una o varias letras.

* Todos ellos tienen un atributo precio que es **obligatorio**
* Todos ellos tienen un elemento vacío que indica  de donde es el producto anterior: "Madrid", "Nueva York", "Frankfurt" o "Tokio".
* Las divisas y los bonos tienen un atributo optativo que se usa para indicar si el producto ha sido estable en el pasado o no.
* Un futuro es un valor esperado que tendrá un cierto producto en el futuro. Se debe incluir este producto en forma de elemento. También puede aparecer un elemento mercado que indique el país de procedencia del producto.
* Todo bono tiene un elemento país_de_procedencia para saber a qué estado pertenece. Debe tener tres elementos extra llamados "valor_deseado", "valor_mínimo" y "valor_máximo" para saber los posibles precios.
* Las divisas tienen siempre un nombre pueden incluir uno o más tipos de cambio para otras monedas.
* Las letras tienen siempre un tipo de interés pagadero por un país emisor. El país emisor también debe existir y debe ser siempre de uno de los países cuyas capitales aparecen arriba (es decir "España", "EEUU", "Alemania" y "Japón"



.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>
	<!DOCTYPE listado [
		<!ELEMENT listado (futuro+, divisa+, bono+, letra+)>
		<!ATTLIST futuro precio CDATA #REQUIRED>
		<!ATTLIST divisa precio CDATA #REQUIRED>
		<!ATTLIST bono precio CDATA #REQUIRED>
		<!ATTLIST letra precio CDATA #REQUIRED>
		<!ELEMENT ciudad_procedencia (madrid|nyork|frankfurt|tokio)>
		<!ELEMENT madrid EMPTY>
		<!ELEMENT nyork EMPTY>
		<!ELEMENT frankfurt EMPTY>
		<!ELEMENT tokio EMPTY>
		<!ATTLIST divisa estable CDATA #IMPLIED>
		<!ATTLIST bono estable CDATA #IMPLIED>
		<!ELEMENT futuro (producto, mercado?, ciudad_procedencia)>
		<!ELEMENT producto (#PCDATA)>
		<!ELEMENT mercado (#PCDATA)>
		<!ELEMENT bono (pais_de_procedencia,valor_deseado,
				valor_minimo, valor_maximo, ciudad_procedencia)>
		<!ELEMENT valor_deseado (#PCDATA)>
		<!ELEMENT valor_minimo (#PCDATA)>
		<!ELEMENT valor_maximo (#PCDATA)>
		<!ELEMENT pais_de_procedencia (#PCDATA)>
		<!ELEMENT divisa (nombre_divisa, 
				tipo_de_cambio+, ciudad_procedencia)>
		<!ELEMENT nombre_divisa (#PCDATA)>
		<!ELEMENT tipo_de_cambio (#PCDATA)>
		<!ELEMENT letra (tipo_de_interes, pais_emisor,ciudad_procedencia)>
		<!ELEMENT tipo_de_interes (#PCDATA)>
		<!ELEMENT pais_emisor (espania|eeuu|alemania|japon)>
		<!ELEMENT espania     EMPTY>
		<!ELEMENT eeuu        EMPTY>
		<!ELEMENT alemania    EMPTY>
		<!ELEMENT japon       EMPTY>
	]>


	<listado>
		<futuro precio="11.28">
			<producto>Cafe</producto>
			<mercado>América Latina</mercado>
			<ciudad_procedencia>
				<frankfurt/>
			</ciudad_procedencia>
		</futuro>
		<divisa precio="183">
			<nombre_divisa>Libra esterlina</nombre_divisa>
			<tipo_de_cambio>2.7:1 euros</tipo_de_cambio>
			<tipo_de_cambio>1:0.87 dólares</tipo_de_cambio>
			<ciudad_procedencia>
				<madrid/>
			</ciudad_procedencia>
		</divisa>
		<bono precio="10000" estable="si">
			<pais_de_procedencia>
				Islandia
			</pais_de_procedencia>
			<valor_deseado>9980</valor_deseado>
			<valor_minimo>9950</valor_minimo>
			<valor_maximo>10020</valor_maximo>
			<ciudad_procedencia>
				<tokio/>
			</ciudad_procedencia>
		</bono>
		<letra precio="45020">
			<tipo_de_interes>4.54%</tipo_de_interes>
			<pais_emisor>
				<espania/>
			</pais_emisor>
			<ciudad_procedencia>
				<madrid/>
			</ciudad_procedencia>
		</letra>
	</listado>

	
	
Ejercicio
===========================================

La Seguridad Social necesita un formato de intercambio unificado para distribuir la información personal de los afiliados.

* Todo archivo XML contiene un listado de uno o mas afiliados
* Todo afiliado tiene los siguientes elementos:

	* DNI o NIE
	* Nombre
	* Apellidos
	* Situación laboral: que tiene que ser una y solo una de entre estas posibilidades: "en_paro", "en_activo", "jubilado", "edad_no_laboral"
	* Fecha de nacimiento: que se desglosa en los elementos obligatorios día, mes y anio.
	* Listado de bajas: que indica las situaciones de baja laboral del empleado. Dicho listado consta de una repetición de 0 o más bajas:
	
		* Una baja consta de tres elementos: causa (obligatoria), fecha de inicio (obligatorio) y fecha de final (optativa),
		
	* Listado de prestaciones cobradas: consta de 0 o más elementos prestación, donde se indicará la cantidad percibida (obligatorio), la fecha de inicio (obligatorio) y la fecha de final (obligatorio)

Examen
===========================================

El examen de este tema tendrá lugar el viernes 7 de marzo de 2014.










