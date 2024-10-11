from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message="")

@app.route('/process', methods=['POST'])
def process():
    first_name = request.form['first_name']  
    last_name = request.form['last_name']     
    age = request.form['age']
    
    message = f"Hello {first_name }{last_name}, you are {age} years old!"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
