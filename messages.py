from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello, world!"

@app.route("/messages")
def get_messages():
  return "This endpoint returns a list of all messages."

@app.route("/messages/<message_id>")
def get_message(message_id):
  return "This endpoint returns a single message by its ID."

@app.route("/send_message")
def send_message():
  message = request.json
  web3.eth.sendTransaction({
    "from": web3.eth.accounts[0],
    "to": message["recipient"],
    "value": web3.toWei(1, "ether"),
    "data": web3.toHex(json.dumps(message))
  })
  return 200

if __name__ == "__main__":
  app.run()
