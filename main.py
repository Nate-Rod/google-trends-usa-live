from flask import Flask, render_template
from trend_data import get_todays_top_hits, get_top_hit_for_state

def create_app():
    tmp_app = Flask(__name__)

    @tmp_app.route('/')
    def hello_world():
        top_hits = get_todays_top_hits()
        for hit in top_hits:
            print(hit)
        get_top_hit_for_state()
        return render_template('main.html')
    return tmp_app

app = create_app()
if __name__ == '__main__':
   app.run()
