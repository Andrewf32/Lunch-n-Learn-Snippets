from flask import request, Flask, jsonify, Response

import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname='lunchnlearn' user='andrewfletcher' host='localhost'")
cursor = conn.cursor()

