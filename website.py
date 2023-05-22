from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  name = request.args.get("name")
  if name:
    return render_template("/static/index.html", name=name)
  else:
    return render_template("/static/index.html")

if __name__ == "__main__":
  app.run(debug=True)
