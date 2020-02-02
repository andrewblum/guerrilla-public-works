from flask import Flask, redirect, request, session, jsonify, Response

app = Flask(__name__)
app.secret_key = "aksdjfhasdf"

pw_list = {'name': 'create todo demo', 
            'done': 'true', 
            'funded': 'false', 
            'description': 'clean wall',
            'id': 7
        }

@app.route('/hi')
def homepage():
    return jsonify(pw_list)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")