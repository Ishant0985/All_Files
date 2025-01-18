document.addEventListener("DOMContentLoaded", function () {
    const countdownElem = document.getElementById("countdown");
    const countdownSection = document.getElementById("countdown-section");
    const fireworksSection = document.getElementById("fireworks-section");
    const videoSection = document.getElementById("video-section");
    const contentElem = document.getElementById("content");
    const videoElem = document.getElementById("birthday-video");
    const backgroundVideo = document.getElementById("background-video");
    const musicElem = document.getElementById("birthday-music");
    const firecrackerSound = document.getElementById("firecracker-sound");

    // Set the countdown time (1 minute for demo purposes)
    const birthdayDate =  new Date('2024-10-10T00:00:00');    // 1 min countdown

    // Error handling wrapper
    function handleError(fn) {
        try {
            fn();
        } catch (error) {
            console.error("Error occurred: ", error);
        }
    }

    function updateCountdown() {
        handleError(() => {
            const now = new Date();
            const timeLeft = birthdayDate - now;

            if (timeLeft > 10000) {
                const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
                const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);
                countdownElem.innerHTML = `${minutes}m ${seconds}s`;
            } else if (timeLeft <= 10000 && timeLeft > 0) {
                startFinalCountdown();
            } else {
                triggerFireworks();
            }
        });
    }

    function startFinalCountdown() {
        handleError(() => {
            let seconds = 10;
            const interval = setInterval(() => {
                countdownElem.innerHTML = seconds;
                seconds--;

                if (seconds < 0) {
                    clearInterval(interval);
                    triggerFireworks();
                }
            }, 1000);
        });
    }

    function triggerFireworks() {
        handleError(() => {
            countdownSection.classList.add('hidden');
            fireworksSection.classList.remove('hidden');
            firecrackerSound.play();

            createFireworks();

            setTimeout(() => {
                firecrackerSound.pause();
                firecrackerSound.currentTime = 0;
                fireworksSection.classList.add('hidden');
                playBirthdayVideo();
            }, 4000); // Firecrackers play for 4 seconds
        });
    }

    function playBirthdayVideo() {
        handleError(() => {
            videoSection.classList.remove('hidden');
            videoElem.play();

            setTimeout(() => {
                videoElem.pause();
                videoSection.classList.add('hidden');
                showContentPage();
            }, 30000); // Play video for 30 seconds
        });
    }

    function showContentPage() {
        handleError(() => {
            contentElem.classList.remove('hidden');
            backgroundVideo.play();
            musicElem.play();
        });
    }

    function createFireworks() {
        handleError(() => {
            const container = document.getElementById("fireworks-container");
            for (let i = 0; i < 30; i++) {
                const firework = document.createElement('div');
                firework.classList.add('firework');
                firework.style.left = Math.random() * 100 + '%';
                firework.style.top = Math.random() * 100 + '%';
                firework.style.backgroundColor = `rgb(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255})`;
                container.appendChild(firework);

                setTimeout(() => firework.remove(), 1000); // Remove after animation
            }
        });
    }

    setInterval(updateCountdown, 1000); // Update countdown every second
});
