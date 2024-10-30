const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql2');

const app = express();
const port = 3000;

app.use(bodyParser.json());

const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'password',
    database: 'book_my_show'
});

db.connect((err) => {
    if (err) {
        console.error('Error connecting to database:', err);
    } else {
        console.log('Connected to database');
    }
});


app.get('/', (req, res) => {
    res.send('Welcome to the Book My Show API');
});

app.post('/api/book', (req, res) => {
    const { movie_title, name, email, seats } = req.body;

    const query = 'INSERT INTO bookins (movie_title, name, email, seats) VALUES (?, ?, ?, ?)';
    db.execute(query, [movie_title, name, email, seats], (err, results) => {
        if (err) {
            console.error('Error booking:', err);
            res.status(500).json({ success: false, error: err.message });
        } else {
            console.log('Booking successful');
            res.json({ success: true });
        }
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
