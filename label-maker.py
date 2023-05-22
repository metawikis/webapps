import tkinter as tk


data = {
  "Title": "The Great Gatsby",
  "Author": "F. Scott Fitzgerald",
  "Genre": "Classic Fiction",
  "Publication Date": "1925",
  "Setting": "West Egg, Long Island",
  "Characters": [
    "Nick Carraway",
    "Jay Gatsby",
    "Daisy Buchanan",
    "Tom Buchanan",
    "Jordan Baker",
  ],
  "Plot": "The story follows Nick Carraway, a young man from the Midwest, as he moves to West Egg, Long Island, seeking his fortune as a bond salesman. There he meets his neighbor, Jay Gatsby, a mysterious millionaire who throws extravagant parties. Nick is drawn into Gatsby's world and eventually learns that Gatsby is in love with Daisy Buchanan, a married woman who lives across the bay. Nick sets out to reunite Gatsby and Daisy, but their love affair is doomed from the start.",
  "Themes": [
    "The American Dream",
    "Love",
    "Loss",
    "Greed",
    "Deception",
  ],
  "Critical Reception": "The Great Gatsby was a critical and commercial success upon its publication. It has since been praised by critics for its writing, its characters, and its themes. The novel has been adapted into several films, including a 2013 version starring Leonardo DiCaprio.",
  "Modern Authors": [
    "Haruki Murakami",
    "Cormac McCarthy",
    "Stephen King",
    "Ocean Vuong",
    "Zadie Smith",
    "Margaret Atwood",
    "Chimamanda Ngozi Adichie",
    "Jonathan Franzen",
    "Kazuo Ishiguro",
    "Ian McEwan",
  ],
  "Favorite Foods": ["Pizza", "Ice Cream", "Chocolate", "Sushi", "Hamburgers"],
  "Favorite Movies": ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction", "The Lord of the Rings: The Fellowship of the Ring"],
  "Favorite TV Shows": ["Breaking Bad", "Game of Thrones", "The Office", "Friends", "The Simpsons"],
  "Favorite Bands": ["The Beatles", "The Rolling Stones", "Pink Floyd", "Led Zeppelin", "The Who"],
  "Favorite Books": ["The Catcher in the Rye", "To Kill a Mockingbird", "1984", "Animal Farm", "The Color Purple"],
  "Favorite Authors": ["J.D. Salinger", "Harper Lee", "George Orwell", "George Orwell", "Alice Walker"],
  "Favorite Sports Teams": ["New York Yankees", "New York Giants", "New York Knicks", "New York Rangers", "New York Islanders"],
  "Favorite Athletes": ["Tom Brady", "LeBron James", "Michael Jordan", "Tiger Woods", "Serena Williams"],
  "Favorite Places to Visit": ["New York City", "Los Angeles", "London", "Paris", "Rome"],
  "Favorite Things to Do": ["Traveling", "Reading", "Watching Movies", "Listening to Music", "Playing Sports"],
  "Favorite Quotes": ["The only way to do great work is to love what you do.", "If you can dream it, you can do it.", "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.", "Never give up on what you really want to do. The person with big dreams is more powerful than one with all the facts.", "The only way to fail is to give up."],
  "Favorite Colors": ["Blue", "Green", "Red", "Yellow", "Purple"],
  "Favorite Animals": ["Dogs", "Cats", "Horses", "Birds", "Fish"],
  "Favorite Flowers": ["Roses", "Tulips", "Lilies", "Sunflowers", "Orchids"],
}
def create_button(root, text, command):
  button = tk.Button(root, text=text, command=command, width=10, height=2)
  button.pack(side="left", fill="y")

def move_to_next_key():
    global current_key
    current_key += 1
    if current_key >= len(data):
        current_key = 0
current_key = 0


def main():
  root = tk.Tk()
  text_block = tk.Text(root)
  text_block.pack()
  # Add the data from the dictionary to the text box.
  for key, value in data.items():
      for key in data:
          create_button(root, key, lambda: text_block.insert("end", data[key]))
          text_block.delete("1.0", "end")
          text_block.insert("end", data[key])
  # Create a text block.


  # Create buttons for each key in the dictionary.

    # Create a button to move to the next key.
  next_key_button = tk.Button(root, text="Next Key", command=lambda: move_to_next_key())
  next_key_button.pack(side="right")

  root.mainloop()

# Create a variable to keep track of the current key.


if __name__ == "__main__":
  main()
