// List of background music files (URLs or relative paths)
const musicTracks = [
    'music/music1.mp3', // Replace with your music file paths
    'music/music2.mp3',
    'music/music3.mp3',
    'music/music4.mp3',
    'music/music5.mp3',
    'music/music6.mp3',
    'music/music7.mp3',
    'music/music8.mp3',
    'music/music9.mp3',
    'music/music10.mp3',
    'music/music11.mp3',
    'music/music12.mp3'
];

// Function to select a random track
function getRandomTrack() {
    const randomIndex = Math.floor(Math.random() * musicTracks.length);
    return musicTracks[randomIndex];
}

// Set the audio source to a random track and play
const audioElement = document.getElementById('background-music');
audioElement.src = getRandomTrack();
audioElement.play();

// Get references to the play and pause buttons
const playBtn = document.getElementById('play-btn');
const pauseBtn = document.getElementById('pause-btn');

// Play button functionality
playBtn.addEventListener('click', () => {
    audioElement.play();
});

// Pause button functionality
pauseBtn.addEventListener('click', () => {
    audioElement.pause();
});
