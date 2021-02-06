//var escuchar = document.getElementById("escuchar");
//var status =document.getElementById("txtStatus");
//var  result = document.getElementById("txtResult");

//asociar el video a la variable media
var media = document.getElementById("media");


var recognition;
var recognizing = false;
//comprobar que el API esté soportada por el navegador
if (!('webkitSpeechRecognition' in window)) {
    alert("¡API no soportada!");
} else {
    //Crear objeto SpeechRecognition y configurarlo para español
    recognition = new webkitSpeechRecognition();
    recognition.lang = "es";
    recognition.continuous = true;
    recognition.interimResults = true;

    recognition.onstart = function() {
        //indicar que se está escuchando y limpiar el texto reconocido
        recognizing = true;
        document.getElementById("txtStatus").value = "escuchando";
        document.getElementById("txtResult").value = " ";
    }
    recognition.onresult = function(event) {

        //una vez  obtenido un reconocimiento mostrarlo y ejecutar la acción correspondiente
        for (var i = event.resultIndex; i < event.results.length; i++) {
            if(event.results[i].isFinal){
                var result = document.getElementById("txtResult");
                media = document.getElementById("media");
                result.value = event.results[i][0].transcript;
                str = result.value.trim();
                if(str == 'reproducir'){
                    media.play();

                }else{
                    if(str == 'parar'){
                        media.pause();

                    }
                    else{
                        //alert("otra cosa");
                    }
                }

            }


        }

    }
    recognition.onerror = function(event) {
        //mostrar el mensaje si se produce algún error
        document.getElementById("txtResult").value = event.error.value;
    }
    recognition.onend = function() {
        //Cuando termine el reconociiento actualizar los controles.
        recognizing = false;
        document.getElementById("txtStatus").value = " ";
        document.getElementById("txtResult").value = " ";
        document.getElementById("escuchar").value="Comenzar reconocimiento voz";


    }

}

function reconocer() {

    if (recognizing == false) {
        recognition.start();
        recognizing = true;
        document.getElementById("escuchar").value="Parar reconocimiento voz";
    } else {
        recognition.stop();
        recognizing = false;
        document.getElementById("escuchar").value="Comenzar reconocimiento voz";
    }
}

function reproducir(){
    media = document.getElementById("media");
    btnreproducir =document.getElementById("btnReproducir");
    if(!media.paused && !media.ended){
        media.pause();
        btnreproducir.value = ">";
    }else {
        media.play();
        btnreproducir.value ="||";
    }
}

/*
function iniciar()
{
    //Obtener enlace a los elemntos de la web
    var video = document.getElementById("video");
    var reproducir = document.getElementById("btnReproducir");
    var status =document.getElementById("txtStatus");
    var  result = document.getElementById("txtResult");
    var escuchar = document.getElementById("btnEscucharOn");
    var noEscuchar = document.getElementById("btnEscucharOff");

    //Definir una instancia de speech recognition si la API está soportada por el navegador

    var recognition;
    var recognizing = false; // para saber cuando se está escuchando

    if(!('webkitSpeechRecognition' in window)){
        alert("¡API de reconocimiento de voz no soportada!");
        escuchar.setAttribute('disabled','true');
    }else {
        recognition = new webkitSpeechRecognition();
        recognition.lang="es-ES"; //establece español como idioma a reconcer
        recognition.continuous = true; // escucha de forma continua incluso si el usuario hace pausas
        recognition.interimResults = true; // devuelve resultados provisionales

        recognition.onstart = function (){
            alert("onstart");
            recognizing = true;
        }

        recognition.onresult = function (event){
            alert("onresult");
            for(var i = event.resultIndex; i < event.results.length;i++){
                if(event.results[i].isFinal)
                    result.value += event.results[i][0].transcript;
            }
        }

        recognition.onerror = function (event){
            alert("onerror");
        }

        recognition.onend = function (){
            alert("onend");
            recognizing = false;
           // escuchar.value = "Comenzar reconocimiento voz";
        }

    }



    reproducir.addEventListener("click", presionar);
    escuchar.addEventListener("click", escucha);
    noEscuchar.addEventListener("click", noEscucha);
}

function presionar(){
    if(!video.paused && !video.ended){
        video.pause();
        reproducir.value = ">";
    }else {
        video.play();
        reproducir.value ="||";
    }
}

function escucha(){
    status.value = "Escuchando  ...";
    recognition.start();
    escuchar.value = "Parar reconocimiento voz";
    result.value =  " ";
}

function noEscucha(){
    recognition.stop();
    status.value = " ...";
    escuchar.value = "Comenzar reconocimiento voz";
    result.value =  " en true";
}

function hablar(){
    alert("hablar");
    if (recognizing === false){
        alert("recognizing false");
        recognition.start();
        recognizing =true;
        status.value = "Escuchando  ..."
        escuchar.value = "Parar reconocimiento voz"
        result.value =  " "
    }else{
        alert("recognizing true")
        recognition.stop();
        recognizing = false;
        status.value = " ..."
        escuchar.value = "Comenzar reconocimiento voz"
        result.value =  " en true"
    }
   /!* if($("#texto").val()=='reproducir'){
        if(!video.paused && !video.ended){
            video.play();
            reproducir.value ="||";
        }
    }
    if($("#texto").val()=='parar'){
        if(!video.paused && !video.ended){
            video.pause();
            reproducir.value = ">";
        }
    }*!/

}

window.addEventListener("load", iniciar)

*/

//------------

/*
(function inciar() {

    //Obtener enlace a los elemntos de la web
    var video = document.getElementById("video");
    var reproducir = document.getElementById("btnReproducir");
    var status =document.getElementById("txtStatus");
    var  result = document.getElementById("txtResult");
    var escuchar = document.getElementById("btnEscucharOn");
    //var escucharOff = document.getElementById("btnEscucharOff")


    if(!('webkitSpeechRecognition' in window)){
        alert("¡API de reconocimiento de voz no soportada!");

        //deshabilitar botón de reconocimiento de voz
        escuchar.setAttribute('disabled',true);

    }else {
        recognition = new webkitSpeechRecognition();
        recognition.lang = "es-ES"; //establece español como idioma a reconcer
        recognition.continuous = true; // escucha de forma continua incluso si el usuario hace pausas
        recognition.interimResults = true; // devuelve resultados provisionales

        recognition.onstart = function () {
            alert("onstart")
            recognizing = true;
        }


    }
    function presionar(){
        if(!video.paused && !video.ended){
            video.pause();
            reproducir.value = ">";
        }else {
            video.play();
            reproducir.value ="||";
        }
    }

        //Establecer los listeners
        reproducir.addEventListener("click", presionar);
        escuchar.addEventListener("click", hablar)
})();

window.addEventListener("load", iniciar)*/
