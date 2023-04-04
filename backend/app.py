from flask import Flask, jsonify, request
from datetime import datetime
import time
app = Flask(__name__)

# square root of function
@app.route('/square/<int:num>', methods = ['GET'])
def square(num):
    metric_start = time.time()
    square_value = num**2
    metric_end  = time.time()
    metric_diff = metric_end - metric_start
    return jsonify({'value': square_value,'time_taken': metric_diff})

@app.route('/cube/<int:num>', methods = ['GET'])
def cube(num):
    metric_start = time.time()
    square_value = num**3
    metric_end  = time.time()
    metric_diff = metric_end - metric_start
    return jsonify({'value': square_value,'time_taken': metric_diff})

@app.route('/fibonacci/<int:nterms>', methods = ['GET'])
def fibonacci(nterms):
    metric_start = time.time()
    fib = {}
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        fib.append(999999)
    # if there is only one term, return n1
    elif nterms == 1:
        fib.append(n1)
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            fib.append(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
    metric_end  = time.time()
    metric_diff = metric_end - metric_start
    if fib[0]==999999:
        return jsonify({'value': "Please enter a positive value",'time_taken': metric_diff})
    else:
        return jsonify({'value': fib,'time_taken': metric_diff})

# driver function
if __name__ == '__main__':
  
    app.run(debug = True, host='0.0.0.0')
