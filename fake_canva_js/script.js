$(function() {
    var letsdraw = false;
  
    var theCanvas = document.getElementById('paint');
    var ctx = theCanvas.getContext('2d');
    var canvasOffset = $('#paint').offset();
  
    $('#paint').mousemove(function(e) {
      if (letsdraw === true) {
        ctx.lineTo(e.pageX - canvasOffset.left, e.pageY - canvasOffset.top);
        ctx.stroke();
      }
    });
  
    $('#paint').mousedown(function(e) {
      letsdraw = true;
      ctx.beginPath();
      ctx.moveTo(e.pageX - canvasOffset.left, e.pageY - canvasOffset.top);
    });
  
    $(window).mouseup(function() {
      letsdraw = false;
    });
  
    // Colores disponibles
    var colors = {
      black: 'black',
      red: 'red',
      blue: 'blue',
      green: 'green',
      yellow: 'yellow',
      // Agrega más colores aquí
    };
  
    // Agrega botones de colores
    Object.keys(colors).forEach(function(color) {
      var button = document.createElement('button');
      button.style.backgroundColor = colors[color];
      button.addEventListener('click', function() {
        ctx.strokeStyle = colors[color];
      });
      document.body.appendChild(button);
    });
  
    // Agrega botón de borrado
    var clearButton = document.createElement('button');
    clearButton.textContent = 'Borrar';
    clearButton.addEventListener('click', function() {
      ctx.clearRect(0, 0, theCanvas.width, theCanvas.height);
    });
    document.body.appendChild(clearButton);
  });
  