/* Music Player */
var playButtons = $('.playButton'); // play buttons
var stopButtons = $('.stopButton'); // stop buttons

playButtons.on("click", play);
stopButtons.on("click", stop);

function play() {

    $(".music").each(function () {
        this.pause();
        this.currentTime = 0
    })

    var music = $("#music" + $(this).data("id"))[0];
    var playButton = $("#play" + $(this).data("id"))[0];
    var stopButton = $("#play" + $(this).data("id"))[0];

    if (music.currentTime > 1) {
        music.pause();
        // remove pause, add play
        playButton.className = "playButton fas fa-play";
    }
    else { // pause music
        music.play();      
        
    }
}

//Stop Button

function stop() {
    var music = $("#music" + $(this).data("id"))[0];
    var playButton = $("#play" + $(this).data("id"))[0];
    var stopButton = $("#play" + $(this).data("id"))[0];

    if (music.stop){
        playButton.className = "";
        playButton.className = "playButton fas fa-play"
    }
    music.currentTime = 0
    music.pause();
}

/* Add Genre to the share dropdown */
function newGenre(){
    if ($("#inputGenre").val() == "addNew") {
        $("#newGenreText").removeClass("d-none");
   }
    else {
        $("#newGenreText").addClass("d-none");
    }
}

/* Add Instrument to the share dropdown */
function newInstrument(){
    if ($("#inputInstrument").val() == "addNew") {
        $("#newInstrumentText").removeClass("d-none");
    }
    else {
        $("#newInstrumentText").addClass("d-none");
    }
}

/* Add option to see the password when typed in */
//code located https://www.w3schools.com/howto/howto_js_toggle_password.asp
function showPassword() {
  var x = document.getElementById("passwordLogin");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

/* If review is over 10 words, have it shrink down until More is clicked to read the rest. */
$(".reviewText").each(function(e, v) {
    $(v).data("full-text", $(v).html());
    if ($(v).html().split(' ').length > 10) {
        $(v).html($(v).html().split(' ').slice(0,10).join(' ') + " ... " + '<a class="expandReview">More</a>');
    }

    $(this).click(function() {
        $(v).html($(v).data("full-text"));
    });
});
