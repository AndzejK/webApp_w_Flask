from flask import Flask

app=Flask(__name__)

    ## Static Routes !! ##

# http://127.0.0.1:5000
@app.route('/') # view fn
def index():
    return "<h1>Hey, Flask!<br> go to /pupy_latin/name to see the results!</h1>"

# http://127.0.0.1:5000/info
@app.route('/info')
def info():
    return "<h2>Let's roll, mate!</h2>"

     ## Dynamic Routes !! ##
# @app.route('/flask/<name>')
# def flask(name):
#     return "<h2>Page name: {} </h2>".format(name.upper())

@app.route('/pupy_latin/<name>')
def flask(name):
    if name[-1]!='y':
        name_=name+'y'
    else:
        name_=name[:-1]+'iful'
    return "<h2>Hey G,<br> We have transformed this word: {} ".format(name) + " into: {} </h2>".format(name_)

if __name__=="__main__":
    app.run(debug=True,port=5001) #debug=True #change the post port=5001
