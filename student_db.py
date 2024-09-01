import psycopg2
from flask import Flask, request, jsonify
import os
from psycopg2 import OperationalError, sql
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from.env file

app = Flask(__name__)

# Connect to the PostgreSQL database 

def connectToDb():
    try:
        print("Connected to the database")
        return psycopg2.connect(
        host=os.getenv('HOSTNAME'),
        database=os.getenv('DATABASE'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        port=os.getenv('PORT')
        )
       
    except OperationalError as e:
        print(f"Unable to connect to the database: {e}")
    # except (Exception, psycopg2.Error) as error:
    #     print("Error while connecting to PostgreSQL", error)
    #     return error
    
conn = connectToDb()

@app.post("/add-student")
def add_student():
    # BODY
    data = request.get_json() 
    name = data['name']
    age = data['age']
    grade = data['grade']

    conn = connectToDb()
    if not conn:
        return "missing credentials",401
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", (name, age, grade))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Student added successfully'})

@app.get("/get-student")

def get_student():
    conn = connectToDb()
    if not conn:
        return "missing credentials",401
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    result = []
    for row in rows:
        result.append({'id': row[0], 'name': row[1], 'age': row[2], 'grade': row[3]})
    return jsonify(result)

@app.put("/update-student/<int:id>")
def update_student(id):
    data = request.get_json()
    name = data['name']
    age = data['age']
    grade = data['grade']
    
    
    conn = connectToDb()
    if not conn:
        return "missing credentials",401
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=%s, age=%s, grade=%s WHERE student_id=%s", (name, age, grade, id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Student updated successfully'})

@app.delete("/delete-student/<int:id>")
def delete_student(id):
    conn = connectToDb()
    if not conn:
        return "missing credentials",401
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE student_id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Student deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True, port = 5001)