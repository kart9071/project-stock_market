from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

# Function to run Streamlit app as a separate process
def run_streamlit_app():
    subprocess.Popen(["streamlit", "run", "streamlit_app/stockapp.py"])

# Route to start and embed Streamlit app
@app.route('/')
def index():
    run_streamlit_app()
    return render_template('index.html')

@app.route('/streamlit')
def streamlit_redirect():
    # Assuming the Streamlit app runs on localhost:8501 by default
    return redirect("http://localhost:8501")

# Route for other pages
@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
