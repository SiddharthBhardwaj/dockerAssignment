from flask import Flask, jsonify, request
from datetime import datetime
app = Flask(__name__)

# square root of function
@app.route('/square/<int:num>', methods = ['GET'])
def square(num):
    metric_start = datetime.now()
    square_value = num**2
    metric_end  = datetime.now()
    return jsonify({'data': square_value})

# driver function
if __name__ == '__main__':
  
    app.run(debug = True)