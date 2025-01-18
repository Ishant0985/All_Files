$(document).ready(function() {
    // Hamburger menu toggle
    $('#hamburger').on('click', function() {
        $('#side-menu').toggleClass('open');
    });
    

// Get the sidebar, overlay, and the menu button
const sidebar = document.getElementById('sidebar');
const overlay = document.getElementById('overlay');
const menuButton = document.getElementById('menu-button');
const body = document.body;

// Function to toggle the sidebar
function toggleSidebar() {
  sidebar.classList.toggle('active');
  overlay.classList.toggle('active');

    // Toggle the no-scroll class on the body
    body.classList.toggle('no-scroll');
}

// Close the sidebar when clicking outside
overlay.addEventListener('click', toggleSidebar);

// Open the sidebar when the menu button is clicked
menuButton.addEventListener('click', toggleSidebar);


    // Query form submission handling
    $('#queryForm').on('submit', function(event) {
        if (!submitQueryForm()) {
            event.preventDefault();
        }
    });
});

function submitQueryForm() {
    const form = document.getElementById('queryForm');
    const errorMessage = document.getElementById('error-message');
    const lastSubmissionTime = localStorage.getItem('lastSubmissionTime');
    const currentTime = new Date().getTime();

    if (lastSubmissionTime && (currentTime - lastSubmissionTime < 300000)) {
        errorMessage.style.display = 'block';
        return false;
    }

    localStorage.setItem('lastSubmissionTime', currentTime);

    setTimeout(function() {
        form.reset();
        alert('Your query has been sent successfully.');
        errorMessage.style.display = 'none';
    }, 1000);

    return true;
}

