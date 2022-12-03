from flask import *
from db import *
import json,requests

app = Flask(__name__,template_folder="pages")

@app.route("/api/v1/<val>", methods=['POST'])
def api(val=None):
    req = request.json
    data = req['data']
    res = get_user(req['key'])
    if res == "ok":
        if val == "test":
          return test(data)
        ## add some
    return "403",403

@app.route('/api/v1', methods=['GET'])
def ap():
    return render_template('home.html')

@app.route('/', methods=['GET'])
def home():
    return redirect('/api/v1')

@app.route('/testapi', methods=['GET'])
def testapi():
    return requests.post('http://127.0.0.1:5000/api/v1/test', json={'key': 'key', 'data':'5'}).text
if __name__ == "__main__":
    app.debug = True
    app.run()