/* Variables */
//var music = document.getElementById('music'); // id for audio element
//var duration = music.duration; // Duration of audio clip, calculated here for embedding purposes

var playButtons = $('.playButton'); // play buttons
var stopButtons = $('.stopButton'); // stop buttons

playButtons.on("click", play);
stopButtons.on("click", stop);

// Gets audio file duration

//Play Button

//Play and Pause

function play() {
    console.log("PLAY");

    $(".music").each(function() {
        this.pause();
    })

    var music = $("#music" + $(this).data("id"))[0];
    var playButton = $("#play" + $(this).data("id"))[0];
    var stopButton = $("#play" + $(this).data("id"))[0];

    // start music
    if (music.paused) {
        music.play();
        // remove play, add pause
        playButton.className = "playButton fas fa-pause";
    } else { // pause music
        music.pause();
        // remove pause, add play
        playButton.className = "playButton fas fa-play";
    }
}

// Stop Button

// stop and reset

function stop() {
    console.log("STOP");

    var music = $("#music" + $(this).data("id"))[0];
    var playButton = $("#play" + $(this).data("id"))[0];
    var stopButton = $("#play" + $(this).data("id"))[0];

    if (music.pause){
        playButton.className = "";
        playButton.className = "playButton fas fa-play"
    }
    music.currentTime = 0
    music.pause();
}
