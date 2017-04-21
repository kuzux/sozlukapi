from __future__ import print_function

from flask import Flask, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

app.run(debug=True)
