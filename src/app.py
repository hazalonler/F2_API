from flask import render_template
from flask_cors import CORS, cross_origin
import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")
cors = CORS(app.app, resources={r"/api/*": {"origins": "*"}})


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

