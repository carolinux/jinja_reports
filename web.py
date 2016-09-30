from datetime import datetime

from flask import (Flask, jsonify, request, render_template,
                   send_from_directory, redirect, url_for, Response)

import plot
import filters

app = Flask(__name__)
app.register_blueprint(filters.blueprint)

@app.route('/', methods=["GET", "POST"])
def show_launch_page():
    return render_template('examples.html', plot=plot)

if __name__ == '__main__':
    print "Starting server at "+str(datetime.now())
    app.run(host="127.0.0.1", debug=True, port=5000)
