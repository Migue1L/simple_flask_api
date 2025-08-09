from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message:" "--- DevOps p i p e l i n e ---"})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)

    