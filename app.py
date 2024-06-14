from flask import Flask, render_template
import subprocess
import requests

app = Flask(__name__)

# Function to run Streamlit app as a separate process
def run_streamlit_app():
    subprocess.Popen(["streamlit", "run", "streamlit_app/stockapp.py"])

# Route to start and embed Streamlit app
@app.route('/')
def streamlit():
    run_streamlit_app()  # Start Streamlit app
    return "Your application is running"

# # Route to interact with Streamlit app (example)
# @app.route('/getData')
# def get_data_from_streamlit():
#     response = requests.get('http://localhost:8501')  # Example: Get data from Streamlit app
#     data = response.json()
#     return data

# Route for other pages
# @app.route('/')
# def index():
#     return 'Welcome to my Flask app!'

if __name__ == '__main__':
    app.run(debug=True)
