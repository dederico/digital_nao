var recognition = new webkitSpeechRecognition();
var resultDiv = document.getElementById("result");
var startButton = document.getElementById("startButton");
var stopButton = document.getElementById("stopButton");

recognition.continuous = true;
recognition.lang = "es-ES";

recognition.onresult = function(event) {
  var result = event.results[event.results.length - 1][0].transcript;
  resultDiv.textContent = result;
};

recognition.onstart = function() {
  startButton.disabled = true;
  stopButton.disabled = false;
  startButton.textContent = "Escuchando...";
};

recognition.onend = function() {
  startButton.disabled = false;
  stopButton.disabled = true;
  startButton.textContent = "Iniciar";
};

startButton.addEventListener("click", function() {
  if (recognition.start) {
    recognition.start();
  } else {
    recognition.onstart();
  }
});

stopButton.addEventListener("click", function() {
  recognition.stop();
});
