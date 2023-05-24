import tkinter as tk


class DataEntryWindow(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create a label for the data.
        self.data_label = tk.Label(self, text="Data:")
        self.data_label.pack(side="top")

        # Create a text box for the data.
        self.data_textbox = tk.Text(self, width=50, height=10)
        self.data_textbox.pack(side="top")

        # Create a list of buttons.
        self.button_list = []
        for i in range(14):
            button = tk.Button(self, text="Button {}:".format(i))
            self.button_list.append(button)

        # Pack the buttons in a horizontal row.
        for button in self.button_list:
            button.pack(side="left")


        # Bind the buttons to an event handler that updates the text box.
        for button in self.button_list:
            button.config(command=self.on_button_click)

        # Create a button drawer for tagging the data.
        self.tag_button_drawer = tk.Frame()
        self.tag_button_drawer.pack(side="top")

        # Create a list of tag buttons.
        self.tag_button_list = []
        for tag in ["Positive", "Negative", "Neutral"]:
            button = tk.Button(self.tag_button_drawer, text=tag)
            self.tag_button_list.append(button)

        # Pack the buttons in a vertical column.
        for button in self.tag_button_list:
            button.pack(side="top")

    def on_button_click(self, event):
        # Get the button text.
        button_text = event.widget.cget("text")

        # Append the button text to the text box.
        self.data_textbox.insert("end", button_text + "\n")

        # Get the tag of the button that was clicked.
        tag = event.widget.cget("text")

        # Tag the text in the text box with the selected tag.
        self.data_textbox.tag_add(tag, "end", "end")

if __name__ == "__main__":
    root = tk.Tk()
    data_entry_window = DataEntryWindow(root)
    data_entry_window.pack(side="top", fill="both", expand=True)
    root.mainloop()
