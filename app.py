import os
import sys

from flask import Flask, render_template, send_from_directory
from appoptics_apm.middleware import AppOpticsApmMiddleware

app = Flask(__name__)
app.wsgi_app = AppOpticsApmMiddleware(app.wsgi_app)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route("/")
def home():
    
    # myPlatform = sys.platform
    
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


