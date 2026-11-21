from flask import Flask, render_template
from service import get_forecast


app = Flask(__name__)

@app.route('/')
def index():
    forecast = get_forecast() 
    
    return render_template('index.html', forecast=forecast)

if __name__ == '__main__':
    app.run(debug=True)