# Diccionario_The_Egg

---
# Ada-lovelace

Ada Lovelace (1815 - 1852) es conocida como la primera programadora de la historia. Fue una matemática, informática y escritora británica hija del poeta Lord Byron y la matemática Lady Byron. Colaboró con Charles Babage en su máquina analítica. En las notas sobre la máquina escribió el primer algoritmo destinado a ser interpretado por una máquina. Creo el primer programa de ordenador antes de que existieran los ordenadores. Además teorizó que se podría usar la computación para mucho más que los cálculos numéricos.

Como reconocimiento a sus aportaciones a la informática el departamento de defensa de estados unidos llamó ADA a un nuevo lenguaje de programación.

El segundo martes de octubre se celebra el día de Ada Lovelace para reivindicar la presencia de las mujeres en ciencia, tecnología, ingeniería y matemáticas.

---


# Algoritmo

Un algoritmo es un conjunto de instrucciones o reglas definidas y no ambiguas, ordenada y finitas que permite solucionar un problema, realizar un cómputo, procesar datos y llevar a cabo otras tareas o actividades.

---

# Arduino
Es una plataforma de creación de electrónica de código abierto basada en hardware y software libre, lo que permite que cualquier pueda utilizarlos y adaptarlos. Se pueden encontrar varios tipos de placas, accesorios y aplicaciones compatibles creadas por diferentes empresas o desarrolladores. Todas son diferentes, pero utilizando la misma base común.

Ofrece la plataforma Arduino IDE, que es un entorno de programación con el que cualquiera puede crear aplicaciones para las placas Arduino y darles diferentes utilidades.

El proyecto nació en 2003 con el fin de facilitar el acceso y uso de la electrónica y la programación. El resultado es una placa con todos los elementos necesarios para conectar periféricos a las entradas y salidas de un microcontrolador, y que se puede programar tanto en Windows como macOs, y GNU/Linux. Un proyecto que promueve la filosofía "learning by doing"

---

# Arquitectura-cliente-servidor

Esta arquitectura consiste básicamente en un cliente que realiza peticiones a otro programa, el servidor, que le da la respuesta.

Aunque esta idea se puede aplicar a programas que se ejecutan en una sola computadora es más ventajosa en un sistema operativo multiusuario distribuido a través de una red de computadoras. 

En esta arquitectura hay una clara separación de responsabilidades:

Cliente: es un programa o proceso que solicita un servicio y usa la información provista para sus propios objetivos

Servidor: Programa o proceso que ofrece un conjunto de servicios y espera peticiones para ejecutar o dar esos servicios.

---

# Arquitectura-harvard
Es una arquitectura de computadores con pistas de almacenamiento y de señal físicamente separadas para las  instrucciones y para los datos.

El término proviene de la computadora Harvard Mark I basada en relés, que almacenaba las instrucciones sobre cintas perforadas y los datos en interruptores electromecánicos. 

En la actualidad la mayoría de los procesadores implementan una arquitectura Harvard modificada para que se puedan cargar programas desde unidades externas de datos para su posterior ejecución.

Al contrario que en la arquitectura von Neumann, una computadora con la arquitectura Harvard la CPU puede tanto leer una instrucción como realizar un acceso a la memoria de datos al mismo tiempo, incluso sin una memoria caché. Por ello está arquitectura puede ser más rápida para un circuito complejo.
![Diagrama Arquitectura Harvard](Diccionario_The_Egg/arquitecturaHarvard.png)

---

# Bases-de-datos

Una base de datos es un conjunto de datos pertenecientes a un mismo contexto y almacenados sistemáticamente para su posterior uso. Actualmente la mayoría de  las bases de datos están en formato digital. 

Hay programas denominados sistemas gestores de bases de datos (SGBD) que permiten almacenar y posteriormente acceder a los datos de forma rápida y estructurada.

Hay diferentes modelos de bases de datos: jerárquicas, de red, transaccionales, relacionales, multidimensionales, orientadas a objetos, documentales, deductivas.

Un modelo es un "descripción" de un contenedor de datos,así como de los métodos para almacenar y recuperar datos de esos contenedores.

En el mundo empresarial las bases de datos más usadas desde los años 70 fueron las relacionales y los lenguajes de consulta SQL

---

# Bucles

Un bucle en programación es una secuencia que repite varias veces un mismo trozo de código, hasta que la condición asignada al bucle deja de cumplirse. Los bucles más usados son 

- **While**

    Se encuentra en la mayoría de lenguajes de programación. Se encarga de ejecutar un trozo de  código mientras las condición del while sea verdadera. 

    ```python
    while condición hacer
    	instrucciones
    fin while
    ```

    La condición del bucle debe devolver un valor booleano, true o false, si se cumple o no la condición.

- **For**

    Permite indicar de antemano el número máximo de iteraciones, o veces que se repite el código. Está en casi todos los lenguajes de programación y es uno de los que más se usa

    ```python
    for i <- x hasta n a incrementos de s hacer
    	instrucciones
    fin for
    ```

    Elementos del bucle

    **variable de control:** suele usarse la letra i (iterador)

    **incialización de la variable de control:** asigna el valor incial a la variable de control

    **condición de control:** es el valor final que puede tomar la variable de control. Una vez se cumpla el bucle se rompe y deja de repetirse

    **incremento:** el valore en el que se va incrementando la variable de control en cada iteración del bucle

    **cuerpo:** código que se ejecuta en cada iteración

- **Do-while**

    Es igual que el while a diferencia de que la comprobación de la condición se hace al final, después de ejecutar el código. Si se cumple se vuelve a ejecutar el código y sino no.

    ```python
    do
    	instrucciones
    while condición
    ```


---

# Compilador

Traducen el código escrito en un lenguaje de  programación al lenguaje de máquina generando un código binario ejecutable.

Permite traducir todo un programa de una sola vez, haciendo una ejecución más rápida y puede almacenarse para usarse luego sin volver a hacer la traducción.

---

# CSS

CSS (Cascading Style Sheets :  Hojas de estilo en cascada) es un lenguaje de  hojas de estilos utilizado para controlar el aspecto o presentación de los documentos HTML o  basados en XML. 

Es la mejor forma de separar los contenidos de su presentación y es imprescindible para crear páginas web complejas. Mejora la accesibilidad del documento, reduce la complejidad de su almacenamiento y permite visualizar el mismo documento en infinidad de dispositivos diferentes.

Una vez creados los elementos de la web con HTML, se utiliza CSS para definir el aspecto de cada elemento: color, tamaño y tipo de letra del texto, separación horizontal y vertical entre elementos, posición de cada elemento dentro de la página, etc.

---

# Diagrama de Flujo

El diagrama de flujo, flujograma o diagrama de actividades es una manera de representar gráficamente un algoritmo  o un proceso a través de una serie de pasos estructurados y vinculados que permiten su revisión como un todo.

### Símbolos del diagrama de flujo

![Símbolos Diagrama Flujo](Diccionario_The_Egg/Untitled%2016.png)



### Ejemplo diagrama de flujo

![Diagrama de Flujo](Diccionario_The_Egg/Untitled%2017.png)



------



# Editor-de-código

Un editor de código fuente es un editor de texto diseñado específicamente para editar el código fuente de programas informáticos. Puede ser una aplicación individual o estar incluido en un entorno de desarrollo integrado.

Los editores de código fuente tienen características diseñadas exclusivamente para simplificar y acelerar la escritura de código fuente, como resaltado de sintaxis, autocompletar y pareo de llaves. Estos editores también proveen un modo conveniente de ejecutar un compilador, un intérprete, un depurador, o cualquier otro programa que sea relevante en el proceso de desarrollo de software

---

# Github

GitHub es una plataforma de desarrollo colaborativo de software para alojar proyectos utilizando el sistema de control de versiones Git.

Actualmente propiedad de Microsoft.

---

# Hardware
Es la parte física de un ordenador o sistema informático. Está formado por los componentes eléctricos, electrónicos, electromecánicos y mecánicos, tales como circuitos de cables y luz, placas, memorias, discos duros, dispositivos periféricos y cualquier otro material en estado físico que sea necesario para que el equipo funcione.

---

# Html

HTML (Hyper Text Markup Language: Lenguaje de marcas de hipertexto) es un lenguaje de marcado para la elaboración de páginas web. Es la pieza más básica para la construcción de la web y se usa para definir el sentido y estructura del contenido de una página web mediante etiquetas que identifican los elementos de la página: párrafo, título, texto, tabla, lista de elementos, etc.

Hipertexto hace referencia a los enlaces que conectan las páginas web entre sí, ya sea dentro de un mismo sitio web o entre diferentes sitios web. Los vínculos es un aspecto fundamental de la web.

---

# Interprete

También conocido como traductor ya que traduce programas escritos en un lenguaje de programación  al lenguaje máquina de la computadora y se ejecuta a medida que se va traduciendo 

---

# Java

Java es un lenguaje de programación orientado a objetos que posee todas las herramientas necesarias para trabajar en proyectos de Inteligencia Artificial. Las características más destacadas de Java son la transparencia, la mantenibilidad y la portabilidad. Permite codificar algoritmos muy fácilmente y es un lenguaje escalable. Teniendo en cuenta que una IA está basada en gran medida en estos algoritmos, Java es una muy buena opción. Además, dispone de interfaces de datos muy atractivas para mejorar la experiencia del usuario. Si tenemos alguna duda, dispone de una nutrida comunidad de usuarios que pueden ayudarnos.

---

# Javascript

Javascript (JS) es un lenguaje de programación ligero e interpretado, orientado a objetos y con funciones de primera clase (se pueden pasar funciones como argumentos de otras funciones, devolverlas como valores de otras funciones y asignarlas a variables o almacenarlas en estructuras de datos).

Aunque es más conocido como el lenguaje de scripting para páginas web, muchos entornos no relacionados con el navegador también lo usan, tales como node.js, Apache CouchDB y Adobe Acrobat.

Es un lenguaje script multiparadigma, basado en prototipos, dinámico, soporta estilos orientados a objetos, imperativos y declarativos.

No confundir con Java. Ambos tienen semánticas y propósitos  diferentes

---

# Lenguaje-de-alto-nivel

El Lenguaje de alto nivel es aquel que se aproxima más al lenguaje natural humano que al lenguaje binario de las computadoras, el que se conoce como lenguaje de bajo nivel.

Un lenguaje de alto nivel permite al programador escribir las instrucciones de un programa utilizando palabras o expresiones sintácticas muy similares al inglés.

Un lenguaje de alto nivel se caracteriza por expresar los algoritmos de una manera adecuada a la capacidad cognitiva humana, en lugar de a la capacidad ejecutora de las máquinas.Ésta es la razón por la que a estos lenguajes se les considera de alto nivel, porque se pueden utilizar palabras de muy fácil comprensión para el programador.

---

# Lenguaje-de-máquina

Es el más primitivo de los lenguajes y es una colección de dígitos binarios o bits (0 y 1) que la computadora lee e interpreta y son los únicos idiomas que las computadoras entienden.

---

# Lenguaje-de-programación

Es un lenguaje formal que, mediante una serie de instrucciones, le permite a un programador escribir un conjunto de órdenes, acciones consecutivas, datos y algoritmos para crear programas que controlen el comportamiento físico y lógico de una máquina.

Existen muchísimos lenguajes de programación y cada uno se enfoca a distintos usos. Se elige el lenguaje de programación a utilizar en función de lo que se quiera hacer  con él.

---

# Ley de Moore

La ley de Moore expresa que aproximadamente cada dos años se duplica el número de transistores en un microprocesador

La ley de Moore no es una ley en el sentido científico, sino más bien una observación, y ha sentado las bases de grandes saltos de progreso.

En 2010, la International Technology Roadmap for Semiconductors predijo que este crecimiento se ralentizaría en 2013, y en 2015 Gordon Moore volvió a predecir que la tasa alcanzaría la saturación en la próxima década. El estancamiento de la Ley de Moore es una consecuencia del límite físico de la tecnología actual. Al aumentar la densidad de transistores aumenta el calor generado para un mismo volumen. Por lo tanto no es posible extraer el calor suficientemente rápido sin riesgo a sobrecalentar y dañar el microprocesador.

La consecuencia directa de la ley de Moore es que los precios bajan al mismo tiempo que las prestaciones suben: la computadora que hoy vale 3000 dólares costará la mitad al año siguiente y estará obsoleta en dos años. En 26 años el número de transistores en un chip se ha incrementado 3200 veces.

---

# Lisp

Desde su nacimineto en 1958 de la mano de John McCarthy, Lisp no ha dejado de crecer. De hecho, su creador trabajó en el MTI junto a Marvin Minsky, uno de los padres de la Inteligencia Artificial. Lisp trabaja con expresiones simbólicas y prototipado, herramientas útiles en el campo del Machine Learning. Además, se utiliza en proyectos como CYC, cuyo objetivo es permitir a las aplicaciones basadas en IA ejecutar razonamientos similares a los humanos.

---

# NoSQL

En informática, NoSQL (a veces llamado "no solo SQL") es una amplia clase de sistemas de gestión de bases de datos que difieren del modelo clásico de SGBDR (Sistema de Gestión de Bases de Datos Relacionales) en aspectos importantes, siendo el más destacado que no usan SQL como lenguaje principal de consultas.

Los datos almacenados no requieren estructuras fijas como tablas, normalmente no soportan operaciones JOIN, ni garantizan completamente ACID (atomicidad, consistencia, aislamiento y durabilidad) y habitualmente escalan bien horizontalmente. Los sistemas NoSQL se denominan a veces "no solo SQL" para subrayar el hecho de que también pueden soportar lenguajes de consulta de tipo SQL.

---

# Periférico
En informática periférico es la denominación genérica de cualquier aparato o dispositivo  auxiliar e independiente que se conecta a la CPU de una computadora y se comunica con ella. Ejemplos: teclado, ratón, monitor, altavoces, auriculares, hubs, impresoras, ... 

---

# Programación

Indicar a un ordenador mediante código que quieres que haga. Se trata de resolver problemas, descomponiéndolos en instrucciones que un ordenador es capaz de realizar.

---

# Puertas lógicas

[https://es.wikipedia.org/wiki/Puerta_lógica](https://es.wikipedia.org/wiki/Puerta_l%C3%B3gica)

Una puerta lógica, o compuerta lógica, es un dispositivo electrónico con una función booleana u otras funciones como sumar o restar, incluyen o excluyen según sus propiedades lógicas. Son circuitos de conmutación integrados en un chip

Son las unidades mínimas de diseño lógico. Las piezas básicas con las que se diseñan circuitos más complejos

### **Puerta AND**


![Diccionario_The_Egg/Untitled.png](Diccionario_The_Egg/Untitled.png)

Implementa el producto lógico.

El producto lógico de las variables A y B se indica como AB, y se lee A y B o simplemente A por B.

El número mínimo de entradas es 2, pero puede ampliarse

![Diccionario_The_Egg/Untitled%201.png](Diccionario_The_Egg/Untitled%201.png)

desde el punto de vista de la aritmética módulo 2, la compuerta AND implementa el producto módulo 2.

### **Puerta OR**

Implementa la operación de suma lógica

![Diccionario_The_Egg/Untitled%202.png](Diccionario_The_Egg/Untitled%202.png)

![Diccionario_The_Egg/Untitled%203.png](Diccionario_The_Egg/Untitled%203.png)

Se puede definir la puerta OR como aquella que proporciona a su salida un 1 lógico si al menos una de sus entradas está a 1.

### **Puerta OR-exclusiva (XOR)**

La puerta lógica OR-exclusiva, más conocida por su nombre en inglés XOR, realiza la función booleana A'B+AB'. Su símbolo es un signo más "+" inscrito en un círculo.

![Diccionario_The_Egg/Untitled%204.png](Diccionario_The_Egg/Untitled%204.png)

![Diccionario_The_Egg/Untitled%205.png](Diccionario_The_Egg/Untitled%205.png)

Se puede definir esta puerta como aquella que da por resultado uno, cuando los valores en las entradas son distintos.

Si la puerta tuviese tres o más entradas, la XOR tomaría la función de suma de paridad, cuenta el número de unos a la entrada y si son un número impar, pone un 1 a la salida, para que el número de unos pase a ser par. Esto es así porque la operación XOR es  asociativa

![Diccionario_The_Egg/Untitled%206.png](Diccionario_The_Egg/Untitled%206.png)

La puerta XOR implementa la suma módulo 2, pero mucho más simple de ver, la salida tendrá un 1 siempre que el número de entradas a 1 sea impar.

### **Puerta NO (NOT)**

![Diccionario_The_Egg/Untitled%207.png](Diccionario_The_Egg/Untitled%207.png)

La puerta lógica NO (NOT en inglés) realiza la función booleana de inversión o negación de una variable lógica.

Una variable lógica (A) a la cual se le aplica la negación se pronuncia como "no A" o "A negada".

![Diccionario_The_Egg/Untitled%208.png](Diccionario_The_Egg/Untitled%208.png)

Se puede definir como una puerta que proporciona el estado inverso del que esté en su entrada.

### Puerta NO-Y (NAND)

![Diccionario_The_Egg/Untitled%209.png](Diccionario_The_Egg/Untitled%209.png)

La puerta lógica NO-Y, más conocida por su nombre en inglés NAND, realiza la operación de producto lógico negado.

![Diccionario_The_Egg/Untitled%2010.png](Diccionario_The_Egg/Untitled%2010.png)

Se puede definir la puerta NO-Y como aquella que proporciona a su salida un 0 lógico únicamente cuando todas sus entradas están en 1.

### Puerta NO-O (NOR)

![Diccionario_The_Egg/Untitled%2011.png](Diccionario_The_Egg/Untitled%2011.png)

La puerta lógica NO-O, más conocida por su nombre en ingles, NOR realiza la operación de suma lógica negada

![Diccionario_The_Egg/Untitled%2012.png](Diccionario_The_Egg/Untitled%2012.png)

Se puede definir la puerta NO-O como aquella que proporciona a su salida un 1 lógico sólo cuando todas sus entradas están a 0. La puerta lógica NOR constituye un conjunto completo de operadores.

### Puerta NOR-exclusiva (XNOR)

![Diccionario_The_Egg/Untitled%2013.png](Diccionario_The_Egg/Untitled%2013.png)

La puerta NO-exclusica, XNOR, es el complemento de la puerta OR exclusiva, siendo su función booleana AB + A'B'. 

![Diccionario_The_Egg/Untitled%2014.png](Diccionario_The_Egg/Untitled%2014.png)

![Diccionario_The_Egg/Untitled%2015.png](Diccionario_The_Egg/Untitled%2015.png)

Esta puerta al ser el complemento de la puerta OR exclusiva (XOR), sus resultados son uno (1) cuando sus entradas, para el caso de 2, son iguales, ya sean con valor 0 o valor 1 (0 y 0, ó 1 y 1). Para más de 2 entradas, si el número de unos de entradas es par, la salida es 1 y si es impar, la salida es 0. Si todas las entradas son 0, la salida es 1, como puede comprobarse en la tabla de verdad de tres entradas.

La puerta lógica XNOR se identifica como función par, en tanto que la puerta lógica XOR se identifica como función impar.

---

# Php

PHP (acrónimo recursivo de PHP: Hypertext Preprocessor) es un lenguaje de código abierto muy popular especialmente adecuado para el desarrollo web y que puede ser incrustado en HTML, por lo que en un mismo archivo se puede combinar código PHP con código HTML siguiendo ciertas reglas. Se utiliza para crear páginas dinámicas

A diferencia de javascript el código PHP se ejecuta en el lado del servidor donde se genera el HTML que se devuelve a la parte cliente

---

# Python

Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código.2 Se trata de un lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional. Es un lenguaje interpretado, dinámico y multiplataforma.

Python es uno de los lenguajes más utilizados para configurar IA. Su simplicidad y las filosofías DRY (Don’t Repeat Yourself) y RAD (Rapid Application Development) en las que se basa lo convierten en un candidato ideal. Puede utilizarse tanto para estructurar datos como para generar algoritmos de IA. Además, dispone de un catálogo de librerías muy extenso que permite hacer realidad cualquier tipo de proyecto. Ningún soporte se resiste a Python, puesto que sirve para trabajar en aplicaciones de todo tipo, sean mobile, web, data science o IA.

---

# R

R dispone de paquetes de programación muy numerosos. Algunos de ellos se utilizan en el ámbito del Machine Learning, como RODBC. Para garantizar la funcionalidad de la IA, implementan algoritmos de aprendizaje automático. Se trata de uno de los mejores lenguajes para analizar y tratar con datos. Por ello, es posible crear buenas IA con finalidades estadísticas.

Se trata de uno de los lenguajes de programación más utilizados en investigación científica, siendo además muy popular en los campos de aprendizaje automático (machine learning), minería de datos, investigación biomédica, bioinformática y matemáticas financieras. A esto contribuye la posibilidad de cargar diferentes bibliotecas o paquetes con funcionalidades de cálculo y graficación.

---

# Raspberry pi

Es un ordenador del tamaño de una tarjeta de crédito que se conecta a la TV o un monitor, un teclado y un ratón. Se puede utilizar para aprender a programar o para construir proyectos electrónicos, y para muchas de las cosas que hacen los PCs de escritorio como hojas de cálculo, procesamiento de textos, navegar internet y jugar videojuegos. Además reproduce video de alta definición. 

Es un ordenador completo con la excepción de que no incluye el cable de alimentación, la caja ni el disco duro, para el que se utiliza una tarjeta de memoria SD. Los periféricos pueden conectarse vía USB
La Raspeberry Pi Foundation mantiene el control de la plataforma de hardware, pero su sistema operativo es de código abierto. El SO oficial es una versión adaptada de la distribución Debian llamada Raspbian, pero también se pueden instalar otros sistemas operativos

### Raspberry Pi vs Arduino

El control del hardware es la principal diferencia con Arduino. La Raspberry Pi fue diseñada como un ordenador en sí, por lo que tiene más potencia que las placas Arduino. Además tiene conectividad WiFI y ethernet integradas en la placa. En Arduino se puede añadir conectividad ethernet añadiendo una placa de expansión, gastando parte de sus puertos e incrementando el precio total

En relación al software, una Arduino ejecuta inmediatamente la tarea para la que se le ha programado, mientras que la raspberry pi requiere un SO completo, por lo que su inicio es más lento

Existen placas como Arduberry  que permiten conectar shields Arduino a una Raspberry Pi

---

# Repositorio-de-control-de-versiones

Los sistemas de control de versiones son una categoría de herramientas de software que ayudan a un equipo de software a gestionar los cambios en el código fuente a lo largo del tiempo. El software de control de versiones realiza un seguimiento de todas las modificaciones en el código en un tipo especial de base de datos

El repositorio es el lugar en el que se almacenan los datos actualizados e históricos de cambios.

---

# Sistema-operativo
Es el software principal o conjunto de programas de un sistema informático que gestiona los recursos de hardware y provee servicios a los programas de aplicación, ejecutándose en modo privilegiado respecto al resto del software, sin permitir que un programa cualquiera realice cambios de importancia sobre él que puedan comprometer su funcionamiento.

### Componentes

El SO tiene 3 componentes esenciales que permiten la interacción con el hardware:

- Sistema de archivos
- Interpretación de comandos:  permite que usuario de ordenes
- Núcleo: funciones básicas como la comunicación, entrasa y salida de datos, gestión de procesos y la memoria,...

### Funciones

- Gestionar la memoria de acceso aleatoria y ejecutr las aplicaciones, designando los recursos necesarios
- Administrar la CPU
- Direccionar las entradas y salidas de datos, a través de drivers, a los periféricos de entrada o salida
- Administrar la información para el buen funcionamiento del PC
- Dirigir las autorizaciones de uso de los usuarios
- Administrar los archivos

### Ejemplos

- Microsoft Windows
- MS-DOS
- UNIX
- Linux
- MacOS
- Ubuntu
- Android
- iOS

---

# Software
Es un término informático que hace referencia a un programa o conjunto de programas, así como datos, procedimientos y pautas que permiten realizar distintas tareas en un sistema informático.

Comúnmente se utiliza este término para referirse de una forma genérica a los programas de un dispositivo informático, sin embargo, software abarca todo aquello que es intangible en un sistema computacional.

### Tipos

De forma genérica en función del uso o utilidad:

- Software del sistema: Programa responsable de la ejecución de todas las aplicaciones necesarias para que un sistema opere correctamente. Además del sistema operativo incluye entre otros herramientas de optimización, controladores de dispositivos y servidores
- Software de programación: herramientas para desarrollar nuevo software.
- Software de aplicación: programas diseñados para facilitar tareas específicas
- Software malicioso o malintencionado

---

# SQL

SQL (por sus siglas en inglés Structured Query Language; en español lenguaje de consulta estructurada) es un lenguaje de dominio específico utilizado en programación, diseñado para administrar, y recuperar información de sistemas de gestión de bases de datos relacionales.1 Una de sus principales características es el manejo del álgebra y el cálculo relacional para efectuar consultas con el fin de recuperar, de forma sencilla, información de bases de datos, así como realizar cambios en ellas. Consiste en un lenguaje de definición de datos, un lenguaje de manipulación de datos y un lenguaje de control de datos

---

# Transistor

Desarrollados por John Bardeen, Walter Brattain y William Shockey en los laboratorios Bell el 23 de Diciembre de 1947, los transistores significan en realidad «transfer resistance» por sus propiedades. Se trata de un elemento eléctrico fabricado con semiconductores que es capaz de alterar el flujo de corriente para dejar pasarla o no, representando los unos y los ceros del sistema binario.

La mayoría de transistores incluye tres puntos de conexión (también llamados terminales), que pueden conectarse a otros transistores o componentes eléctricos. Al modificar la intensidad de corriente que circula entre el primer y segundo terminal de un transistor, la corriente entre el segundo y el tercero cambia, permitiendo que el transistor actúe como un interruptor de encendido y apagado. Esto es lo que se conoce como «puertas lógicas».

Dado que los ordenadores trabajan en sistema binario, estos estados de «encendido» y «apagado» de los transistores sirven para representar los unos y los ceros del sistema binario.

Así, en un procesador o GPU se introducen millones de transistores de tamaño diminuto unidos entre sí, que trabajando en conjunto permiten que el procesador pueda realizar millones de operaciones cada ciclo de reloj. Conceptualmente, un procesador no es mas que una enorme fábrica con millones de interruptores.

---

# Turing

**Alan Turing**. Uno de los padres de la ciencia de la computación y precursor de la informática moderna.

**Máquina de Turing**: máquina capaz de resolver cualquier problema matemático que pudiera representarse mediante un algoritmo. Son el objeto central de estudio en la "Teoría de la computación".

T**esis Church-Turing**: cualquier modelo computacional existente tiene las mismas capacidades algorítmicas, o un subconjunto, de las que tiene una máquina de Turing.

En la segunda guerra mundial trabajo en **descifrar los códigos de Enigma** construyendo la máquina Bombe.

**Test de Turing:** método para determinar si una máquina puede pensar. Humano chatea con una máquina haciendo preguntas y tiene que concluir si se trataba de una persona o un máquina.

# Von-neumann
**John von Neuman** fue un matemático húngaro-estadounidense, que realizó contribuciones fundamentales en física cuántica, análisis funcional,  teoría de conjuntos, teoría de juegos, ciencias de la computación, economía, análisis numérico, cibernética, hidrodinámica, estadística y muchos otros campos. Se le considera uno de los matemáticos más importantes del siglo XX.

**Arquitectura Von Neuman**, también conocida como modelo de von Neuman o arquitectura Princeton, es una arquitectura de computadoras basada en la descrita en 1945 por John von Neuman y otros. Describe una arquitectura de diseño para un computador digital electrónico con partes que constan de una unidad de procesamiento que contiene una unidad aritmético lógica y registros de procesador, una unidad de control que contiene un registro de instrucciones y un contador de  programa, una memoria para almacenar tanto datos como instrucciones, almacenamiento masivo externo y mecanismos de entrada y salida. En esta arquitectura no pueden darse simultáneamente una búsqueda de instrucciones y una operación de datos, ya que comparten un bus en común. Esto se conoce como el **cuello de botella Von Neuman** y muchas veces limita el rendimiento del sistema.

![Diagrama de la arquitectura von Neuman](Diccionario_The_Egg/arquitecturaVonNeuman.png)

El diseño de la arquitectura von Neuman es más simple que la *arquitectura Harvard* más moderna, que también es un sistema de programa almacenado, pero tiene un conjunto dedicado de direcciones y buses de datos para leer datos desde memoria y escribir datos en la misma, y otro conjunto de direcciones y buses de datos para ir a buscar instrucciones.

En la gran mayoría de computadoras modernas, se utiliza la misma memoria tanto para los datos como para las instrucciones de programa, y la distinción entre von Neuman vs Harvard se aplica a la arquitectura de memoria caché, pero no  a la memoria principal.

---
