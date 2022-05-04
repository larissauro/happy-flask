from flask import Flask, render_template
from gerador_piada import generate_piada
import os

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/piada/new")
def piada():
	return 	{ 
		'piada': generate_piada()
	}

if __name__ == "__main__":
	if os.getenv("PORT"):
		port = os.getenv("PORT")
	else:
		port = 3000
	app.run(host='0.0.0.0', port=port)
