from flask import Flask, render_template
from programa_feliz_piada import get_piada

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/piada/new")
def piada():
	return 	{ 
		'piada': get_piada()
	}

if __name__ == "__main__":
	app.run()
