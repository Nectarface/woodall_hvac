document.addEventListener('DOMContentLoaded', function() {
    console.log('Hoosier Daddy HVAC loaded.');
    
    // Simple console log for diagnostic
    // In a real build, we'd add mobile menu toggling here.
    // Since we are keeping it minimal CSS-only for the prototype nav, this is just a placeholder.
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
