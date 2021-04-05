# Import the necessary libraries
from flask import Flask, jsonify, request, render_template
import mysql.connector
import requests
import json
import collections

# Libraries that are no longer needed
#import jwt
#import pandas as pd

app = Flask(__name__)

# This allows for testing when the database is turned off
try:
    # Define the connection parameters for the SQL database
    mydb = mysql.connector.connect(
    host="music-db.caozbhwr6zij.us-east-1.rds.amazonaws.com",
    user="music_maestro",
    password="music2021",
    database="music-db"
    )
except:
    x=1

@app.route('/')
def api_information():
    # This function returns a HTML page with information on all the other APIs
    return """<html>
<body>
<h1>Music Restful API Service</h1>
<h3>Designed, developed and implemented by Freddie Savundra, Christa Dobson and Tom Doyle</h3>
<b>Group: 34</b>
<br></br>
<br></br>
<b>Get all music</b>
<p>Request type: GET</p>
<p>Path: /music/</p>
<br></br>
</body>
</html>"""

# Get Request
@app.route('/music/', methods=['GET'])
def get_music():
    # This function gets all the music in the database
    try:
        # Open a connection to the database
        mycursor = mydb.cursor()

        # Perform the select statement and extract the rows
        mycursor.execute("SELECT * FROM music_data")
        rows = mycursor.fetchall()

        # For each row append the relevant data to an array
        rowarray_list = []
        for row in rows:
            t = (row[0], row[1], row[2])
            rowarray_list.append(t)
            
        # Convert the array into JSON
        j = json.dumps(rowarray_list)

        # Convert JSON to key-value pairs
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d["track_id"] = row[0]
            d["track_title"] = row[1]
            d["artist"] = row[2]
            d["album"] = row[3]
            objects_list.append(d)
        
        # Convert key-value pairs to JSON
        response = json.dumps(objects_list)
        #response = jwt.encode(response, 'secret', algorithm='HS256')
        return(response),200
    except:
        return jsonify({'error':'there was an error getting the music'}), 400
 
# Get Request
@app.route('/music/<artist>', methods=['GET'])
def get_stock(artist):
    # This function gets a specific stock from the database
    try:
        # Open a connection to the database
        mycursor = mydb.cursor()

        # Perform the select statement and extract the rows for the stock
        sql_script = 'SELECT * FROM music_data WHERE artist = \'' + symbol + '\''
        
        mycursor.execute(sql_script)
        rows = mycursor.fetchall()
        
        # Respond with an error if no rows were obtained from the SQL query
        if rows == []:
            return jsonify({'error':'the artist does not exist'}), 404
        else:        
            # For each row append the relevant data to an array
            rowarray_list = []
            for row in rows:
                t = (row[0], row[1], row[2], row[3])
                rowarray_list.append(t)

            # Convert the array into JSON
            j = json.dumps(rowarray_list)

            # Convert JSON to key-value pairs
            objects_list = []
            for row in rows:
                d = collections.OrderedDict()
                d["track_id"] = row[0]
                d["track_title"] = row[1]
                d["artist"] = row[2]
                d["album"] = row[3]
                objects_list.append(d)

            # Convert key-value pairs to JSON
            response = json.dumps(objects_list)
            return(response),200
    except:
        return jsonify({'error':'there was an error getting the artist'}), 400


 if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
