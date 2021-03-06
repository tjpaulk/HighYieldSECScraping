from flask import (Flask, render_template, abort, jsonify, request,
                   redirect, url_for)
import numpy as np
import pandas as pd


app = Flask(__name__)

df = pd.DataFrame({'Q': [0, 1, 2, 3, 4],
                   'JJ': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c--', 'd', 'e']})


@app.route("/", methods=("POST", "GET"))
def welcome():
    return render_template("welcome.html",
                           tables=[df.to_html(classes='sql_functions', index=False)],
                           titles=df.columns.values)
