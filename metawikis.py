from flask import Flask, request
import requests
from azure.storage.blob import BlobClient
from web3 import Web3

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello, world!"

@app.route("/wikis")
def get_wikis():
  wikis = []
  for wiki in requests.get("https://en.wikipedia.org/w/api.php?action=query&list=allpages&format=json").json()["query"]["allpages"]:
    wikis.append({
      "id": wiki["id"],
      "title": wiki["title"]
    })
  return jsonify(wikis)

@app.route("/wikis/<wiki_id>")
def get_wiki(wiki_id):
  wiki = requests.get("https://en.wikipedia.org/w/api.php?action=query&titles={}&prop=revisions&rvprop=content&format=json".format(wiki_id)).json()["query"]["pages"][wiki_id]["revisions"][0]["content"]
  return wiki

@app.route("/wikis/<wiki_id>/pages")
def get_wiki_pages(wiki_id):
  pages = []
  for page in requests.get("https://en.wikipedia.org/w/api.php?action=query&titles={}&prop=revisions&rvprop=content&format=json".format(wiki_id)).json()["query"]["pages"][wiki_id]["revisions"]:
    pages.append({
      "id": page["id"],
      "content": page["content"]
    })
  return jsonify(pages)

@app.route("/wikis/<wiki_id>/pages/<page_id>")
def get_wiki_page(wiki_id, page_id):
  page = requests.get("https://en.wikipedia.org/w/api.php?action=query&titles={}&prop=revisions&rvprop=content&format=json".format(wiki_id)).json()["query"]["pages"][wiki_id]["revisions"][page_id]["content"]
  return page

@app.route("/add_wiki")
def add_wiki():
  wiki = request.json
  web3.eth.sendTransaction({
    "from": web3.eth.accounts[0],
    "to": "0x0000000000000000000000000000000000000001",
    "value": web3.toWei(1, "ether"),
    "data": web3.toHex(json.dumps(wiki))
  })
  return 201, {"Location": url_for("get_wiki", wiki_id=wiki["id"])}

@app.route("/add_wiki_page")
def add_wiki_page():
  wiki_page = request.json
  web3.eth.sendTransaction({
    "from": web3.eth.accounts[0],
    "to": "0x0000000000000000000000000000000000000002",
    "value": web3.toWei(1, "ether"),
    "data": web3.toHex(json.dumps(wiki_page))
  })
  return 201, {"Location": url_for("get_wiki_page", wiki_id=wiki_page["wiki_id"], page_id=wiki_page["id"])}

@app.route("/upload")
def upload():
  blob_client = BlobClient(account_name="<account_name>", account_key="<account_key>", container_name="<container_name>")
  for wiki in wikis:
    blob_client.upload_blob(wiki["url"], wiki["id"])
  for wiki_page in wiki_pages:
    blob_client.upload_blob(wiki_page["content"], wiki_page["id"])
