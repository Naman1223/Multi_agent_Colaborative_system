from flask import Flask, render_template, request
import webbrowser
import threading
from models import UI_llm
import execjs
from tools import markdown_to_text
import webview
from threading import Thread # Import your Flask instance



ui_roadmap = markdown_to_text("roadmap.md")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',python_data=ui_roadmap)

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    return f"User Input: {user_input}"

def run_flask():
    app.run(port=5000)

if __name__ == '__main__':
    # Start Flask in a background thread
    Thread(target=run_flask, daemon=True).start()

    # Open the pywebview "canvas" pointing to the Flask server
    webview.create_window('My App Canvas', 'http://localhost:5000')
    webview.start()


