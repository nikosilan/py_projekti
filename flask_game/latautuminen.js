const startButton = document.getElementById('startButton');
const barFill = document.getElementById('barFill');

startButton.addEventListener('click', () => {
    let progress = 0;

    function fillBar() {
        progress += Math.floor(Math.random() * 5) + 1;
        if (progress > 100) progress = 100;

        barFill.style.width = progress + '%';

        // move plane
        const plane = document.querySelector('.plane-inside');
        plane.style.left = progress + '%';

        if (progress < 100) {
            setTimeout(fillBar, 200);
        } else {
            setTimeout(() => {
                window.location.href = 'kartta.html';
            }, 500);
        }
    }

    fillBar();
});
