from flask import Flask, request, jsonify, abort
from password_generator import create_password

app = Flask(__name__)

@app.route("/generate-password", methods=["GET"])
def generate_password():

    length = request.args.get("length", default=18, type=int)

    if length not in range(6, 100):
        return jsonify("Password length is out of range. Please enter a value between 6 and 100.")
    
    numbers = request.args.get("numbers", default=1, type=int)
    special = request.args.get("special", default=1, type=int)

    password = create_password(length, numbers, special)
    return jsonify(password)

if __name__ == '__main__':
    app.run(debug=True)