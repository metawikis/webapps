from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello, world!"

@app.route("/schedules")
def get_schedules():
  return "This endpoint returns a list of all schedules."

@app.route("/schedules/<schedule_id>")
def get_schedule(schedule_id):
  return "This endpoint returns a single schedule by its ID."

@app.route("/add_schedule")
def add_schedule():
  schedule = request.json
  web3.eth.sendTransaction({
    "from": web3.eth.accounts[0],
    "to": "0x0000000000000000000000000000000000000001",
    "value": web3.toWei(1, "ether"),
    "data": web3.toHex(json.dumps(schedule))
  })
  return 201, {"Location": url_for("get_schedule", schedule_id=schedule["id"])}

if __name__ == "__main__":
  app.run()
