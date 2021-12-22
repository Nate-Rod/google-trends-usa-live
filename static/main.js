function getRandomColor() {
  //TODO: Refine this to generate more aesthetically pleasing colors
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

function getRandomGoogleColor(){
  var colors = ['#008744', '#0057e7', '#d62d20', '#ffa700'];
  return colors[Math.floor(Math.random()*colors.length)];
}

window.setInterval(function(){
    $(".state").each(function(index, state){
        // applies the randomization to each individual state
        $(state).css("fill", getRandomGoogleColor());
    })
}, 1000);
