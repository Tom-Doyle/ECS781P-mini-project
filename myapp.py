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
<h1>Investment Restful API Service</h1>
<h3>Designed, developed and implemented by Freddie Savundra, Christa Dobson and Tom Doyle</h3>
<b>Group: 34</b>
<br></br>
<br></br>

# Next step is adding Get, Put, Post, Delete requests
