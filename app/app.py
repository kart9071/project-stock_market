import flask
from flask import Flask, request, render_template, Response
from package import fetch
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np



app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    info = {}
    if request.method == "POST":
        ticker = request.form["ticker"]
        info = fetch.company_info(ticker)
        
    return render_template("home.html", info = info)

@app.route("/stats", methods = ['GET', 'POST'])
def stats():
    if request.method == "POST":
        ticker = request.form["ticker"]
        fig = fetch.plot_stats(ticker)
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
        
            


if __name__ == "__main__":
    app.run(debug = True)