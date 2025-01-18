// List of background music files (URLs or relative paths)
const musicTracks = [
    'music/music1.mp3', // Replace with your music file paths
    'music/music2.mp3',
    'music/music3.mp3',
    'music/music4.mp3',
    'music/music5.mp3',
    'music/music6.mp3'
];

// Function to select a random track
function getRandomTrack() {
    const randomIndex = Math.floor(Math.random() * musicTracks.length);
    return musicTracks[randomIndex];
}

// Add a cache-busting parameter to avoid caching issues
function getTrackWithCacheBust(track) {
    return track + '?v=' + new Date().getTime();
}

// Set the audio source to a random track
const audioElement = document.getElementById('background-music');

// Load the track, but don't autoplay until user interaction
const randomTrackWithCacheBust = getTrackWithCacheBust(getRandomTrack());
audioElement.src = randomTrackWithCacheBust;
audioElement.loop = true;

// Play audio after user interaction (click anywhere on the page)
document.body.addEventListener('click', () => {
    audioElement.play().then(() => {
        console.log("Audio is playing");
    }).catch((error) => {
        console.error("Autoplay failed:", error);
    });
}, { once: true }); // The event will fire only once (the first click)
