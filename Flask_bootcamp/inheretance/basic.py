from flask import Flask, render_template # render_template  run html files

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info/<name>')
# View No.2
def info_view(name):
    return render_template('info.html',name=name)

if __name__=='__main__':
    app.run(debug=True,port=5002)