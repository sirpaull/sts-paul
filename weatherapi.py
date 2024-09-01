

'''
    Create a rest API that interacts with openweather API
    You pass

'''


from sys import api_version
import psycopg2
from flask import Flask, request, jsonify
import os
from psycopg2 import OperationalError, sql
from dotenv import load_dotenv
import requests

load_dotenv() 

app = Flask(__name__)

API_KEY = "a393fedf47fab09afb60a5218d0ba1ef"
#API_KEY='a393fedf47fab09afb60a5218d0ba1ef'
#API_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API_key}'


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
    
conn = connectToDb()

# Route to get weather data by city
@app.route('/weather', methods=['POST'])
def get_weather():
    # Call the OpenWeather API
    body = request.get_json()
    city = body['city'] 
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    #url = f"{API_URL}?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()
    #return data to check for errors
    
    if data["cod"] == 200:
        
        #Extract the necessary data
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        country = data['sys']['country']
        

        # Save the data in the database
        conn = connectToDb()
        if not conn:
            return "missing credentials",401
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO weathers (city, country, temperature, description)
            VALUES (%s, %s, %s, %s)
        """, (city, country, temperature, description))
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({
            'city': city,
            'country': country,
            'temperature': temperature,
            'description': description,
        })
    else:
        return jsonify({'error': 'City not found'}), 404


#get_weather()

@app.route('/weather', methods=['GET'])

def get_all_weather():
    conn = connectToDb()
    cur = conn.cursor()
    cur.execute("SELECT * FROM weathers")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify([
        {'city': row[1], 'country': row[2], 'temperature': row[3], 'description': row[4]} for row in rows
    ])

if __name__ == '__main__':
    app.run(debug=True, port = 5001)






