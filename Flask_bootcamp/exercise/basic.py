from flask import Flask, render_template, request

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    # the logic starts as False 
    lower_letter=False
    upper_letter=False
    num_end=False
    username=request.args.get('username')

    # checking if any letter is lowercase
    lower_letter= any(c.islower()for c in username)
    upper_letter= any(c.isupper()for c in username)
    num_end=username[-1].isdigit()

    report= lower_letter and upper_letter and num_end

    return render_template('report.html',report=report,lower=lower_letter,upper=upper_letter,num_end=num_end,username=username)


if __name__=='__main__':
    app.run(debug=True,port=5002)