
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
