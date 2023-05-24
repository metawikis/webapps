import tkinter as tk


class LabelingWindow(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create a label for the data.
        self.data_label = tk.Label(self, text="Data:")
        self.data_label.pack(side="top")

        # Create a text box for the data.
        self.data_textbox = tk.Text(self, width=10, height=2)
        self.data_textbox.pack(side="top")

        # Create a label for the label.
        self.label_label = tk.Label(self, text="Label:")
        self.label_label.pack(side="top")

        # Create a text box for the label.
        self.label_textbox = tk.Text(self, width=10, height=2)
        self.label_textbox.pack(side="top")

        # Create a button to add the data and label to a list.
        self.add_button = tk.Button(self, text="Add")
        self.add_button.pack(side="top")

        # Create a button to clear the data and label text boxes.
        self.clear_button = tk.Button(self, text="Clear")
        self.clear_button.pack(side="top")

        # Create a list to store the data and label text.
        self.data_list = []

        # Bind the add button to an event handler that adds the data and label text to the list.
     #   self.add_button.config(command=self.on_add_button_click)

        # Bind the clear button to an event handler that clears the data and label text boxes.
#        self.clear_button.config(command=self.on_clear_button_click)

        # Create a dropdown list of genres.
        self.genre_dropdown = tk.OptionMenu(self, "", "Action", "Adventure", "Comedy", "Drama", "Horror", "Mystery", "Romance", "Sci-Fi", "Thriller")
        self.genre_dropdown.pack(side="top")

        # Create a lot more buttons for tags.
        self.tag_buttons = []
        for tag in ["Funny", "Sad", "Scary", "Happy", "Love", "Hate", "Peace", "War", "Life", "Death"]:
            button = tk.Button(self, text=tag)
            self.tag_buttons.append(button)

        # Pack the buttons in a vertical column.
        for button in self.tag_buttons:
            button.pack(side="top")

        # Create a text body to cycle through when buttons are pressed.
        self.text_body = tk.Text(self, width=100, height=20)
        self.text_body.pack(side="bottom")

        # Bind the tag buttons to an event handler that cycles through the text body.
        for button in self.tag_buttons:
            button.config(command=self.on_tag_button_click)

    def on_add_button_click(self, event):
        # Get the data text.
        data_text = self.data_textbox.get("1.0", "end")

        # Get the label text.
        label_text = self.label_textbox.get("1.0", "end")

        # Add the data and label text to the list.
        self.data_list.append((data_text, label_text))

        # Clear the data and label text boxes.
        self.data_textbox.delete("1.0", "end")
        self.label_textbox.delete("1.0", "end")

    def on_tag_button_click(self, event):
        # Get the tag text.
        tag_text = event.widget.cget("text")

        # Cycle through the text body, adding the tag text to each line.
        for i in range(self.text_body.get("1.0", "end").count("\n")):
            self.text_body.insert("end", tag_text + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    data_entry_window = LabelingWindow(root)
    data_entry_window.pack(side="top", fill="both", expand=True)
    root.mainloop()
