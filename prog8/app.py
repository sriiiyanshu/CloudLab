from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        total = num1 + num2
        return render_template('index.html', result=total, num1=num1, num2=num2)
    except ValueError:
        return render_template('index.html', error="Please enter valid numbers")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
