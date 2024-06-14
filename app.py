from flask import Flask, render_template
import subprocess

app = Flask(__name__)

# Function to run Streamlit app as a separate process
def run_streamlit_app():
    subprocess.Popen(["streamlit", "run", "streamlit_app/stockapp.py"])

# Route to start and embed Streamlit app
@app.route('/')
def streamlit():
    run_streamlit_app()  # Start Streamlit app
    return "Your application is running"

# Route for other pages
@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
