from flask import Flask, render_template

def create_app():
    tmp_app = Flask(__name__)

    @tmp_app.route('/')
    def hello_world():
       return render_template('main.html')
    return tmp_app

app = create_app()
if __name__ == '__main__':
   app.run()
