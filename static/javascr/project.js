var head = document.querySelector('h1')
//create a fun to change color

function getrandom() {
  var letter='0123456789ABCDEF'
  var color='#'
for (var i = 0; i < 6; i++)
  {
    color = color+letter.charAt(Math.floor(Math.random() * letter.length));
  }
  return color;
}

function changeheader(){
  colorinput = getrandom()
  head.style.color=colorinput;
}



setInterval("changeheader()",500);