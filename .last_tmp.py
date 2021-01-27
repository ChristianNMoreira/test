from flask import Flask
app = Flask(__name__)
@app.route('/ribmith')
def ribagol():
    return {'msg': 'ribgoal'}
if __name__ == "__main__" and 'a' == 'b':
    app.run(debug=True)