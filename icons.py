import google_images_search
from io import BytesIO
from PIL import Image

# in this case we're using PIL to keep the BytesIO as an image object
# that way we don't have to wait for disk save / write times
# the image is simply kept in memory
# this example should display 3 pictures of puppies!

gis = google_images_search.GoogleImagesSearch('your_dev_api_key', 'your_project_cx')

my_bytes_io = BytesIO()
listbox=[]
gis.search({'q': 'puppies', 'num': 3})
for image in gis.results():
    # here we tell the BytesIO object to go back to address 0
    my_bytes_io.seek(0)

    # take raw image data
    raw_image_data = image.get_raw_data()

    # this function writes the raw image data to the object
    image.copy_to(my_bytes_io, raw_image_data)

    # or without the raw data which will be automatically taken
    # inside the copy_to() method
    image.copy_to(my_bytes_io)

    # we go back to address 0 again so PIL can read it from start to finish
    my_bytes_io.seek(0)

    # create a temporary image object
    temp_img = Image.open(my_bytes_io)

    # show it in the default system photo viewer
    listbox.append(temp_img)

import labels as tk
import requests
import os
# Define the search terms.
SEARCH_TERMS = ["dogs", "cats", "birds"]

# Define the output directory.
OUTPUT_DIRECTORY = "/"

# Create the output directory if it does not exist.
if not os.path.exists(OUTPUT_DIRECTORY):
    os.mkdir(OUTPUT_DIRECTORY)

# Initialize the image downloader.
#gis = GoogleImagesSearch()

# Create the GUI.
root = tk.Tk()

# Create the search bar.
search_bar = tk.Entry(root)
search_bar.pack()

# Create the search button.
search_button = tk.Button(root, text="Search", command=lambda: search(search_bar.get()))
search_button.pack()

# Create the image list.
image_list = tk.Listbox(root)
image_list.pack()

# Create the download button.
download_button = tk.Button(root, text="Download", command=lambda: download(image_list.get(image_list.curselection())))
download_button.pack()

# Start the GUI.
root.mainloop()


# Define the search function.
def search(search_term):
    # Clear the image list.
    image_list.delete(0, tk.END)

    # Search for images.
    results = gis.search(search_term)

    # Add the images to the image list.
    for result in results:
        image_url = result["image_url"]
        image_name = image_url.split("/")[-1]
        image_list.insert(tk.END, image_name)


# Define the download function.
def download(image_name):
    # Download the image.
    image_url = gis.get_info(image_name)["image_url"]
    requests.get(image_url, stream=True).save(os.path.join(OUTPUT_DIRECTORY, image_name))


# Run the app.
gis_search_app()
