import os
import sys

from flask import Flask, request, render_template

# In python we can create object instances 
# and assign them to variables for safekeeping!
app = Flask(__name__)

# Here we tell the server that whenever someone goes to
# "/", it needs to show them the home page
@app.route("/")
def home():
    return render_template("v1/home.html")

# Here we tell the server that whenever someone goes to
# "/about", it needs to show them the about page
@app.route("/about")
def about():
    return render_template("v1/about.html")

# Don't worry about this! It's just some settings for
# the server to follow
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, threaded=True, debug=True)
