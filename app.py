from flask import Flask, render_template, request
from image_scraping import image_scrape
import os


app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/image_download", methods = ["GET", "POST"])
def images():
    if request.method == "POST":
        name = request.form["name"]
        no_of_images = request.form["number_of_images"]
        no_of_images = int(no_of_images)
        # print(name, no_of_images)

        image_scrape(name, no_of_images)

        # image display
        imageList = os.listdir('static/' + name)
        imagelist = [name + '/' + image for image in imageList]

        print(imagelist)

        return render_template("show_image.html", imagelist=imagelist)


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)