function getRandomColor() {
  //TODO: Refine this to generate more aesthetically pleasing colors
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

window.setInterval(function(){
    $(".state").each(function(index, state){
        // applies the randomization to each individual state
        $(state).css("fill", getRandomColor());
    })
}, 1000);
