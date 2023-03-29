
from pathlib import Path
from flask import Flask, render_template, request
from main.main import main

app = Flask(__name__)

if not Path(Path.cwd(), 'uploads').exists():
    Path(Path.cwd(), 'uploads').mkdir()

app.config["IMAGE_UPLOADS"] = str(Path(Path.cwd(), 'uploads'))
 

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':

        main(Path(Path.cwd(), 'uploads'))
        return render_template('index.html')

    else:

        return render_template('index.html')


app.run(debug=True)
