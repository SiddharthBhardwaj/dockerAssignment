from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import time
import sqlite3
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'application/json'

# create tables in db
@app.route('/createtables/', methods = ['GET'])
def createtables():
    try:
        conn = sqlite3.connect('assignment.db')
        conn.execute("CREATE TABLE SQUARE_METRIC(START_TIME REAL, END_TIME REAL, TIME_DIFF REAL)")
        conn.execute("CREATE TABLE CUBE_METRIC(START_TIME REAL, END_TIME REAL, TIME_DIFF REAL);")
        conn.execute("CREATE TABLE FIB_METRIC(START_TIME REAL, END_TIME REAL, TIME_DIFF REAL);")
        conn.commit()
        res = "Table creation is success."
        return jsonify({'response': res})
    except:
        res = "Tabkle creation was an error."
        return jsonify({'response': res})
    

# square of a number
@app.route('/square/<int:num>', methods = ['GET'])
def square(num):
    metric_start = time.time()
    square_value = num**2
    metric_end  = time.time()
    metric_diff = metric_end - metric_start
    conn = sqlite3.connect('assignment.db')
    conn.execute("INSERT INTO SQUARE_METRIC (START_TIME,END_TIME,TIME_DIFF) VALUES (?,?,?)",(metric_start,metric_end,metric_diff))
    conn.commit()
    return jsonify({'value': square_value,'time_taken': metric_diff})

# cube of a number
@app.route('/cube/<int:num>', methods = ['GET'])
def cube(num):
    metric_start = time.time()
    square_value = num**3
    metric_end  = time.time()
    metric_diff = metric_end - metric_start
    conn = sqlite3.connect('assignment.db')
    conn.execute("INSERT INTO CUBE_METRIC (START_TIME,END_TIME,TIME_DIFF) VALUES (?,?,?)",(metric_start,metric_end,metric_diff))
    conn.commit()
    return jsonify({'value': square_value,'time_taken': metric_diff})


# fibonacci series of a number
@app.route('/fib/<int:nterms>', methods = ['GET'])
def fibonacci(nterms):
    metric_start = time.time()
    fib = []
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
    conn = sqlite3.connect('assignment.db')
    conn.execute("INSERT INTO FIB_METRIC (START_TIME,END_TIME,TIME_DIFF) VALUES (?,?,?)",(metric_start,metric_end,metric_diff))
    conn.commit()
    if fib[0]==999999:
        return jsonify({'value': "Please enter a value greated than 0",'time_taken': metric_diff})
    else:
        return jsonify({'value': fib,'time_taken': metric_diff})

# metrics display
@app.route('/metrics/', methods = ['GET'])
def metrics():
    square_avg_time = getDataFromDb("SQUARE_METRIC")
    cube_avg_time   = getDataFromDb("CUBE_METRIC")
    fib_avg_time   = getDataFromDb("FIB_METRIC")
    
    return jsonify({'Square_Avg_time': square_avg_time,'Cube_Avg_time': cube_avg_time,'Fib_Avg_time': fib_avg_time})


def getDataFromDb(tableName):
    conn = sqlite3.connect('assignment.db')
    cursor = conn.cursor()
    query = 'SELECT * from {}'.format(tableName)
    cursor.execute(query)
    results = cursor.fetchall()
    conn.commit()
    total_time=0
    for row in results:
        total_time += row[2]
    if len(results) == 0:
        avg_time = "NA"
    else:
        avg_time = total_time/len(results)
    
    return avg_time

# driver function
if __name__ == '__main__':
  
    app.run(debug = True,host = '0.0.0.0')
