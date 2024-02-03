from flask import Flask, request, jsonify
import socket

app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add_numbers():

    numbers = request.get_json()
    first_number = int(numbers["firstNumber"])
    second_number = int(numbers["secondNumber"])

    # Retrieve the server's own IP address
    try:
        server_ip = socket.gethostbyname(socket.gethostname())
    except:
        server_ip = 'unknown'

    # Create a JSON response
    return jsonify({
        "client_ip": request.remote_addr,
        "server_ip": server_ip,
        "total": first_number + second_number
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)

