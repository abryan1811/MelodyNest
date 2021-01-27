/* Variables */
var music = document.getElementById('music'); // id for audio element
var duration = music.duration; // Duration of audio clip, calculated here for embedding purposes
var playButton = document.getElementById('playButton'); // play button
var stopButton = document.getElementById('stopButton'); // stop button



// Gets audio file duration
music.addEventListener("canplaythrough", function () {
    duration = music.duration;
}, false);

//Play Button

// play button work when clicked
playButton.addEventListener("click", play);

//Play and Pause

function play() {
    // start music
    if (music.paused) {
        music.play();
        // remove play, add pause
        playButton.className = "";
        playButton.className = "fas fa-pause";
    } else { // pause music
        music.pause();
        // remove pause, add play
        playButton.className = "";
        playButton.className = "fas fa-play";
    }
}

// Stop Button

// stop button works when clicked
stopButton.addEventListener("click", stop);

// stop and reset

function stop() {
    if (music.pause){
        playButton.className = "";
        playButton.className = "fas fa-play"
    }
    music.currentTime = 0
    music.pause();
}

// getPosition
// Returns elements left position relative to top-left of viewport
function getPosition(el) {
    return el.getBoundingClientRect().left;
}