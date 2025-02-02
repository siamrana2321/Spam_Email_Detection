// Dark Mode Toggle
const darkModeToggle = document.getElementById('darkModeToggle');
const body = document.body;

// Check for saved dark mode preference in localStorage
if (localStorage.getItem('dark-mode') === 'enabled') {
    body.classList.add('dark-mode');
    darkModeToggle.querySelector('i').classList.replace('fa-moon', 'fa-sun');
}

darkModeToggle.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
    const icon = darkModeToggle.querySelector('i');
    if (body.classList.contains('dark-mode')) {
        icon.classList.replace('fa-moon', 'fa-sun');
        localStorage.setItem('dark-mode', 'enabled');
    } else {
        icon.classList.replace('fa-sun', 'fa-moon');
        localStorage.setItem('dark-mode', 'disabled');
    }
});