from flask import Flask
from config import TestConfig,Config
app = Flask(__name__)

#app.config.from_object(ProductConfig)
app.config.from_object(Config)



from .views import *