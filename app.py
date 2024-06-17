from flask import Flask, redirect
import subprocess

app = Flask(__name__)

# Function to run Streamlit app as a separate process
def run_streamlit_app():
    subprocess.Popen(["streamlit", "run", "stockapp.py"])

# Route to start and embed Streamlit app
@app.route('/')
def index():
    run_streamlit_app()
    return redirect("http://localhost:8501")

# Route for other pages
@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
