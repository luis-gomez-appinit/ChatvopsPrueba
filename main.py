from flask_cors import CORS
from flask import Flask


FLASK_PORT = 6001
# Crear app Flask
app = Flask(__name__)
CORS(app, origins="*")

@app.route("/sync-data", methods=["GET"])
def sync_data():
    return "Sincronización iniciada", 200
