from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost', 
        user='root',  
        password='password',  
        database='book_my_show'  
    )

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookins (
            id INT AUTO_INCREMENT PRIMARY KEY,
            movie_title VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            seats INT NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/book', methods=['POST'])
def book_movie():
    try:
        data = request.form
        print(data)  # Check if data is received correctly

        movie_title = data.get('movieTitle')
        name = data.get('name')
        email = data.get('email')
        seats = data.get('seats')

        if not movie_title or not name or not email or not seats:
            return jsonify({'success': False, 'message': 'All fields are required!'}), 400

        try:
            seats = int(seats)
        except ValueError:
            return jsonify({'success': False, 'message': 'Seats must be an integer!'}), 400

        print(f"Received data: movie_title={movie_title}, name={name}, email={email}, seats={seats}")

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO bookins (movie_title, name, email, seats)
            VALUES (%s, %s, %s, %s)
        ''', (movie_title, name, email, seats))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({'success': True, 'message': 'Booking successful!'}), 201

    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
        return jsonify({'success': False, 'message': 'Database error occurred!'}), 500

    except Exception as e:
        print(f"General Error: {e}")
        return jsonify({'success': False, 'message': 'An error occurred!'}), 500

if __name__ == '__main__':
    app.run(debug=True)
