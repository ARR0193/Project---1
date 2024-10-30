document.getElementById('bookingForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const movie_title = document.getElementById('movie_title').value;
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const seats = document.getElementById('seats').value;

    const bookingData = {
        movie_title,
        name,
        email,
        seats
    };

    fetch('/api/book', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(bookingData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Booking successful!');
            // Optionally, close modal or navigate to another page
        } else {
            alert('Booking failed. Please try again.');
        }
    })
    .catch(error => console.error('Error:', error));
});
