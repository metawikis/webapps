from flask import Flask, request
from web3 import Web3
from azure.storage.blob import BlobClient

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello, world!"

@app.route("/posts")
def get_posts():
  posts = []
  for post in web3.eth.getTransactionReceipts():
    if post["contractAddress"] == "0x0000000000000000000000000000000000000001":
      posts.append({
        "id": post["blockNumber"],
        "title": post["args"]["title"],
        "body": post["args"]["body"],
        "author": post["args"]["author"],
        "created_at": post["blockHash"]
      })
  return jsonify(posts)

@app.route("/posts/<post_id>")
def get_post(post_id):
  post = web3.eth.getTransactionReceipt(post_id)
  if post is None:
    return 404
  return jsonify({
    "id": post["blockNumber"],
    "title": post["args"]["title"],
    "body": post["args"]["body"],
    "author": post["args"]["author"],
    "created_at": post["blockHash"]
  })

@app.route("/posts", methods=["POST"])
def create_post():
  post = request.json
  web3.eth.sendTransaction({
    "from": web3.eth.accounts[0],
    "to": "0x0000000000000000000000000000000000000001",
    "value": web3.toWei(1, "ether"),
    "data": web3.toHex(json.dumps(post))
  })
  return 201, {"Location": url_for("get_post", post_id=post["id"])}

@app.route("/followers/<user_id>")
def get_followers(user_id):
  followers = []
  for follower in web3.eth.getTransactionReceipts():
    if follower["contractAddress"] == "0x0000000000000000000000000000000000000002":
      followers.append({
        "id": follower["blockNumber"],
        "user_id": follower["args"]["user_id"],
        "follower_id": follower["args"]["follower_id"]
      })
  return jsonify(followers)

@app.route("/followers", methods=["POST"])
def follow_user():
  follower = request.json
  web3.eth.sendTransaction({
    "from": web3.eth.accounts[0],
    "to": "0x0000000000000000000000000000000000000002",
    "value": web3.toWei(1, "ether"),
    "data": web3.toHex(json.dumps(follower))
  })
  return 201, {"Location": url_for("get_follower", follower_id=follower["id"])}

@app.route("/upload")
def upload():
  blob_client = BlobClient(account_name="<account_name>", account_key="<account_key>", container_name="<container_name>")
  for post in posts:
    blob_client.upload_blob(post.body, post.id)
  return 200

if __name__ == "__main__":
  app.run()
