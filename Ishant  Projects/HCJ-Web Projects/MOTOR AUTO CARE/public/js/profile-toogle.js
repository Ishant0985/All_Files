        // Toggle dropdown for profile options
// Get the profile elements
const profileIcon = document.getElementById('profile-pic');
const profileDropdown = document.getElementById('profile-dropdown');

// Toggle dropdown visibility
profileIcon.addEventListener('click', function (event) {
    event.stopPropagation(); // Prevent closing when clicking on the icon
    profileDropdown.style.display = profileDropdown.style.display === 'block' ? 'none' : 'block';
});

// Close dropdown if clicking outside
document.addEventListener('click', function () {
    profileDropdown.style.display = 'none';
});

// Prevent closing when clicking inside the dropdown
profileDropdown.addEventListener('click', function (event) {
    event.stopPropagation();
});
