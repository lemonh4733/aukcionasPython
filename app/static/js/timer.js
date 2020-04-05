
let time = document.querySelector('.time')
let monthsArr = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
]
var countDownDate = new Date(`${monthsArr[time.textContent.substring(8,9)-1]} ${time.textContent.substring(10,12)}, ${time.textContent.substring(2,6)} 15:37:25`).getTime();
let months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
]
console.log(time.textContent.substring(10,12)+" test")

var x = setInterval(function() {


  var now = new Date().getTime();
    

  var distance = countDownDate - now;
    

  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  document.getElementById("demo").innerHTML = days + "d " + hours + "h "
  + minutes + "m " + seconds + "s ";
    
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("demo").innerHTML = "ENDED";
  }
}, 1000);