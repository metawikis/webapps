from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/api/v1/characters")
def get_characters():
    characters = [
        {
            "id": 1,
            "character_name": "My Character",
            "level": 10,
            "experience": 10000,
            "race": "Human",
            "class": "Warrior",
            "guild": "The Guild",
            "location": "Stormwind City",
            "online": True,
        },
        {
            "id": 2,
            "character_name": "Your Character",
            "level": 20,
            "experience": 20000,
            "race": "Orc",
            "class": "Mage",
            "guild": "The Other Guild",
            "location": "Orgrimmar",
            "online": False,
        },
    ]
    return jsonify(characters)

@app.route("/api/v1/characters/<id>")
def get_character(id):
    character = next((c for c in characters if c["id"] == id), None)
    if character is None:
        return "Character not found", 404
    return jsonify(character)

@app.route("/api/v1/characters/create", methods=["POST"])
def create_character():
    character = request.json
    character["id"] = len(characters) + 1
    characters.append(character)
    return jsonify(character), 201

@app.route("/api/v1/characters/update", methods=["PUT"])
def update_character():
    character = request.json
    character_to_update = next((c for c in characters if c["id"] == character["id"]), None)
    if character_to_update is None:
        return "Character not found", 404
    character_to_update.update(character)
    return jsonify(character_to_update), 200

@app.route("/api/v1/characters/delete", methods=["DELETE"])
def delete_character():
    character_id = request.json["id"]
    character_to_delete = next((c for c in characters if c["id"] == character_id), None)
    if character_to_delete is None:
        return "Character not found", 404
    characters.remove(character_to_delete)
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
