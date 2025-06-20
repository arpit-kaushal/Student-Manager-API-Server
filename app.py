from flask import Flask, request, jsonify
from flask_cors import CORS
from db_config import init_db
from flask import render_template

app = Flask(__name__)
CORS(app)
mysql = init_db(app)

@app.route('/api/students', methods=['GET'])
def get_students():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    students = [{'id': row[0], 'name': row[1], 'email': row[2], 'course': row[3]} for row in data]
    return jsonify(students)

@app.route('/api/students', methods=['POST'])
def add_student():
    data = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO students (name, email, course) VALUES (%s, %s, %s)",
                (data['name'], data['email'], data['course']))
    mysql.connection.commit()
    return jsonify({'message': 'Student added'})

@app.route('/api/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute("UPDATE students SET name=%s, email=%s, course=%s WHERE id=%s",
                (data['name'], data['email'], data['course'], id))
    mysql.connection.commit()
    return jsonify({'message': 'Student updated'})

@app.route('/api/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id,))
    mysql.connection.commit()
    return jsonify({'message': 'Student deleted'})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
