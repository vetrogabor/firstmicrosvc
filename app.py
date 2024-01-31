from flask import Flask, request

app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add_numbers():
    numbers = request.get_json()
    first_number = int(numbers["firstNumber"])
    second_number = int(numbers["secondNumber"])

    total = first_number + second_number

    return {"total": total}

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

