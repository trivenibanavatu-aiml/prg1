// Navbar scroll effect
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Contact form validation and submission
const contactForm = document.getElementById('contact-form');
const formMessage = document.getElementById('form-message');

contactForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get form values
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    // Validate form
    if (!name || !email || !message) {
        showMessage('Please fill in all fields', 'error');
        return;
    }

    if (!isValidEmail(email)) {
        showMessage('Please enter a valid email address', 'error');
        return;
    }

    // Simulate form submission
    showMessage('Sending message...', 'info');
    
    // Simulate API call with timeout
    setTimeout(() => {
        showMessage('Thank you! Your message has been sent successfully.', 'success');
        contactForm.reset();
    }, 1500);
});

// Email validation helper
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Message display helper
function showMessage(text, type) {
    formMessage.textContent = text;
    formMessage.style.display = 'block';
    
    // Set message style based on type
    if (type === 'error') {
        formMessage.style.backgroundColor = '#ffe6e6';
        formMessage.style.color = '#ff0000';
    } else if (type === 'success') {
        formMessage.style.backgroundColor = '#e6ffe6';
        formMessage.style.color = '#008000';
    } else {
        formMessage.style.backgroundColor = '#e6f3ff';
        formMessage.style.color = '#0066cc';
    }
}