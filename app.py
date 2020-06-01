import os
from flask import Flask, render_template


app = Flask(__name__, static_url_path='/static', static_folder='static')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))



@app.route('/')
@app.route('/homepage')
def home_page():
    return render_template("homepage.html")


@app.route('/gallery')
# def gallery():
#     images = os.listdir(os.path.join(app.static_folder, 'gallery_images'))
#     return render_template("gallery.html", images=images)
def gallery():
    images = os.listdir(os.path.join(app.static_folder, "gallery_images"))
    return render_template('gallery.html', images=images)


@app.route('/reviews')
def review_page():
    return render_template("review-page.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)
