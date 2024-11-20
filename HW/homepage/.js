document.addEventListener('DOMContentLoaded', () => {
    const funFactBtn = document.getElementById('funFactBtn');
    const funFact = document.getElementById('funFact');

    funFactBtn.addEventListener('click', () => {
        funFact.style.display = funFact.style.display === 'none' ? 'block' : 'none';
    });
});