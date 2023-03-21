from flask import Flask, render_template, jsonify, request
from datetime import datetime, timedelta

app = Flask(__name__)

app.config['expiration_time'] = datetime.now() + timedelta(minutes=10)

remaining_time = app.config['expiration_time'] - datetime.now()

@app.route('/')
def home():
    return render_template('home.html')

def get_remaining_time_in_seconds():
    remaining_time = app.config['expiration_time'] - datetime.now()
    remaining_time_in_seconds = remaining_time.total_seconds()
    return remaining_time_in_seconds

@app.route('/remaining_time')
def remaining_time():
    remaining_time_in_seconds = get_remaining_time_in_seconds()
    return jsonify({'remaining_time_in_seconds': remaining_time_in_seconds})

@app.route('/reset', methods=['POST'])
def reset():
    if request.method == 'POST':
        app.config['expiration_time'] = datetime.now() + timedelta(minutes=10)
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, port=5005)