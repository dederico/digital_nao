function getTimeRemaining() {
    var now = new Date();
    var newYear = new Date(now.getFullYear() + 1, 0, 1);
    var timeRemaining = newYear - now;
  
    var seconds = Math.floor((timeRemaining / 1000) % 60);
    var minutes = Math.floor((timeRemaining / 1000 / 60) % 60);
    var hours = Math.floor((timeRemaining / (1000 * 60 * 60)) % 24);
    var days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
  
    return {
      'total': timeRemaining,
      'days': days,
      'hours': hours,
      'minutes': minutes,
      'seconds': seconds
    };
  }
  
  function initializeClock() {
    var daysSpan = document.getElementById('days');
    var hoursSpan = document.getElementById('hours');
    var minutesSpan = document.getElementById('minutes');
    var secondsSpan = document.getElementById('seconds');
  
    function updateClock() {
      var time = getTimeRemaining();
  
      daysSpan.textContent = time.days;
      hoursSpan.textContent = ('0' + time.hours).slice(-2);
      minutesSpan.textContent = ('0' + time.minutes).slice(-2);
      secondsSpan.textContent = ('0' + time.seconds).slice(-2);
  
      if (time.total <= 0) {
        clearInterval(timeinterval);
      }
    }
  
    updateClock();
    var timeinterval = setInterval(updateClock, 1000);
  }
  
  initializeClock();
  