from flask import Flask
from config import TestConfig, Config
from flask_jsonrpc import JSONRPC

app = Flask(__name__)
jsonrpc = JSONRPC(app, '/api/')

# app.config.from_object(ProductConfig)
app.config.from_object(Config)

from .views import *
