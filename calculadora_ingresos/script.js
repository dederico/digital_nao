function calculateIncome() {
    var hours = parseFloat(document.getElementById("hours").value);
    var rate = parseFloat(document.getElementById("rate").value);
  
    if (!isNaN(hours) && !isNaN(rate)) {
      var income = hours * rate;
      document.getElementById("result").innerHTML = "Ingresos: $" + income.toFixed(2);
    } else {
      document.getElementById("result").innerHTML = "Por favor ingrese valores numéricos válidos.";
    }
  }
  