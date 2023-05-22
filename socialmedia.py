from flask import Flask, request
from flask_restful import Resource, Api

import os
#from azure.storage.blob import BlobClient

app = Flask(__name__)
api = Api(app)

class SocialMediaData(object):
    def __init__(self, id, user_id, post_id, text, created_at, updated_at):
        self.id = id
        self.user_id = user_id
        self.post_id = post_id
        self.text = text
        self.created_at = created_at
        self.updated_at = updated_at

class SocialMedia(Resource):
    def get(self):
        # Get all of the user's social media posts
        posts = []
        for post in SocialMediaData.query.all():
            posts.append({
                "id": post.id,
                "user_id": post.user_id,
                "post_id": post.post_id,
                "text": post.text,
                "created_at": post.created_at,
                "updated_at": post.updated_at
            })
        return jsonify(posts)

    def post(self):
        # Get the user's social media post
        post = request.get_json()

        # Create the post
        new_post = SocialMediaData(id=None, user_id=post["user_id"], post_id=post["post_id"], text=post["text"], created_at=post["created_at"], updated_at=post["updated_at"])
        new_post.save()

        return new_post

    def put(self, id):
        # Get the user's social media post
        post = request.get_json()

        # Update the post
        social_media_data = SocialMediaData.query.get(id)
        social_media_data.user_id = post["user_id"]
        social_media_data.post_id = post["post_id"]
        social_media_data.text = post["text"]
        social_media_data.created_at = post["created_at"]
        social_media_data.updated_at = post["updated_at"]
        social_media_data.save()

        return social_media_data

    def delete(self, id):
        # Get the user's social media post
        post = SocialMediaData.query.get(id)

        # Delete the post
        post.delete()

        return "Post deleted"

api.add_resource(SocialMedia, "/")

@app.route("/upload")
def upload():
    # Get the blob client
 #   blob_client = BlobClient(account_name="<account_name>", account_key="<account_key>", container_name="<container_name>")

    # Get all of the social media posts
    posts = []
    for post in SocialMediaData.query.all():
        posts.append({
            "id": post.id,
            "user_id": post.user_id,
            "post_id": post.post_id,
            "text": post.text,
            "created_at": post.created_at,
            "updated_at": post.updated_at
        })

    # Upload the social media posts to the blob
   # for post in posts:
  #      blob_client.upload_blob(post.text, post.id)

    #return 200

if __name__ == "__main__":
    app.run(debug=True)
