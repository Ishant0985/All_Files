const faqs = document.querySelectorAll('.faq-container');

faqs.forEach(faq => {
    faq.addEventListener('click', () => {
        faq.classList.toggle('active');
    });
});
