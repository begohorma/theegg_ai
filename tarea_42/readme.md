# Enunciado

El alumno para superar esta tarea debe:

1.- Diseñar una estructura básica de HTML y verla en el navegador.

2.- Introducir algo de color a la página apoyándose en CSS.

3.- Añádir un video de youtube gracias a la nueva etiqueta video.

4.- Serías capaz de darle al play y al pause del video mediante instrucciones por voz (hablando a la computadora) utilizando javascript? (no obligatorio).

# Solución

En el propio contenido de la página web se dan explicaciones sobre el ejercicio.

## Apartados 1 y 2: Estructura básica Html y CSS

Para practicar los conceptos básicos a aprender no utilizo ninguna template proporcionada por los IDEs y creo todo de manera manual.

Se crear archivo `index.html` con estructura de página básica.

Se especifica que el idioma de la página es español.


Se utiliza directorio css para guardar las hojas de estilo. Se crea el fichero `main.css`.

Para poder aplicar los estilos a la página dentro del `<head>` de index.html se utliza la etiqueta `<link href="css/main.css" rel="stylesheet" type="text/css">` para relacionar ambos archivos.

Además se añade el archivo `normalice.css` y el enlace para su apliación. En el contenido de la página hay un árticulo explicativo sobre éste fichero. 

Para practicar el uso de la etiquetas html y estilos básicos se estructura la pagina en fomra de varios artículos con distintos tipos de listas y otros estilos.


## Apartado 3: Insertar vídeo

Se realizan dos variantes:

*  Enlazar vídeo de Youtube utilizando el enlace proporcionado por Youtube que usa la etiqueta `<iframe>`
*   Enlazar video incluido en la carpeta **video**. Se utiliza la etiqueta `<video>` y varios atributos para configurarlo. 



## Apartado 4: Control del video por voz

Se utilza la etiqueta `<video>` para cagar un vídeo incluido en la carpeta **video**.

Se crea un panel para incluir botones y campos de texto. Se utiliza el archivo `reproductor.css` para definir el estilo de los elementos del panel. El código javascript asociado a las funcionalidades del panel está en el archivo `reproductor.js` dentro de la carpeta **js**

* El primer botón permite comenzar y parar de forma manual la reproducción del video. El evento onclick se asocia a la función `reproducir()` 
* El segundo botón inicia el reconocimiento de voz. Su evento onclick  se asocia a la función `reconocer()`
* El siguiente texto con forma de etiqueta muestra si se está escuchando o no
* El último texto muestra el texto reconcido al escuchar


Para el reconocimiento de voz se utiliza el API Web Speech de Javascript. [https://wicg.github.io/speech-api/](https://wicg.github.io/speech-api/). Esta API no está soportada por todos los navegadores por lo que se recomienda utilizar **Google Chrome** para probar su funcionamiento.

Se reconoce es idioma español y las palabras clave son:

*   **"Reproducir"**: para que se inicie la reproducción del video
*   **"Parar"**: para detener la reproducción del video.


## Ejecución

Descargar del repositorio los archivos de la tarea_42. 

Abrir en **Google Chrome** es archivo `index.html` situado en la carpeta tarea_42.

