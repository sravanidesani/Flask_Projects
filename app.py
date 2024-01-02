from flask import Flask, request, jsonify
import requests
app = Flask(__name__)
#basic routes added
@app.route("/")
def home():
    return "Home"

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id" : user_id,
        "name" : "sravani",
        "age" : 25
    }
    country = request.args.get("country")
    if country:
        user_data["country"] = country
    return jsonify(user_data), 200

@app.route("/create-user", methods = ["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 201

if __name__ == "__main__":
    app. run(debug = True)

    

    test_url = "http://127.0.0.1:5000/create-user"
    test_data = {"name": "John Doe", "age": 30}
    test_response = requests.post(test_url, json=test_data)

    print(test_response.status_code)
    print(test_response.json())
    print("hello")

