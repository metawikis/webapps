from flask import Flask, request
import requests
from azure.storage.blob import BlobClient

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello, world!"

@app.route("/icons")
def get_icons():
  icons = []
  for icon in requests.get("https://fonts.googleapis.com/icon?family=Material+Icons").json():
    icons.append({
      "name": icon["name"],
      "url": icon["url"]
    })
  return jsonify(icons)

@app.route("/icons/<icon_name>")
def get_icon(icon_name):
  icon = requests.get("https://fonts.googleapis.com/icon?family=Material+Icons&icon={}".format(icon_name)).json()
  if icon is None:
    return 404
  return jsonify(icon)

@app.route("/add_icon")
def add_icon():
  icon = request.json
  blob_client = BlobClient(account_name="<account_name>", account_key="<account_key>", container_name="<container_name>")
  blob_client.upload_blob(icon["url"], icon["name"])
  return 201, {"Location": url_for("get_icon", icon_name=icon["name"])}

if __name__ == "__main__":
  app.run()
