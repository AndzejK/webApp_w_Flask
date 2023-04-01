# Volume Calculator APP
from flask import Flask, render_template, request

app=Flask(__name__)

# HTTPS Get request
@app.route('/')
def home():
    print("GET request...")
    return render_template('index.html')

# HTTPS POST request
@app.route('/',methods=['POST'])
def home_post():
    #The form has the List and in the list we have tuples()
    dimension_1=request.form['1st_value']
    dimension_2=request.form['2nd_value']
    dimension_3=request.form['3rd_value']
    get_volume=float(dimension_1)*float(dimension_2)*float(dimension_3)
    print("POST request")
    return render_template('index.html',output=get_volume,dimension_1_html=dimension_1,dimension_2_html=dimension_2,dimension_3_html=dimension_3)
app.run()