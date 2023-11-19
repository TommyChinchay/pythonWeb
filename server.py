from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def mostrar_html():
    # Lee el contenido de index.html
    with open('index.html', 'r') as file:
        content = file.read()
    return content

@app.route('/romper')
def romper():
    os._exit(1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
