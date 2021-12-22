from flask import Flask, render_template
from concurrent.futures import ThreadPoolExecutor
from trend_data import get_top_hits_df_for_state

def create_app():
    tmp_app = Flask(__name__)

    @tmp_app.route('/')
    def hello_world():
        print(trending_by_state)
        return render_template('main.html')
    return tmp_app

print("Building hits by state . . .")
trending_by_state = get_top_hits_df_for_state()
app = create_app()
if __name__ == '__main__':
   app.run()
