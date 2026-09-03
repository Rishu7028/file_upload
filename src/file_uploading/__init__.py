# import os
# from flask import Flask, request

# app = Flask(__name__)

# UPLOAD_FOLDER = "uploads"
# # os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route("/upload", methods=["POST"])
# def upload_file():
#     if "file" not in request.files:
#         return "No file selected"

#     file = request.files["file"]

#     # if file.filename == "":
#     #     return "No file selected"

#     file.save(os.path.join(UPLOAD_FOLDER,file.filename))

#     return "File uploaded successfully"


# if __name__ == "__main__":
#     app.run(debug=True)


#-------------------------------------------------------------------------------->

import os
from flask import Flask, request, render_template

app = Flask(__name__)


UPLOAD_FOLDER = os.path.join(app.root_path, "uploads")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file selected", 400

    file = request.files["file"]
    filename = file.filename

    file.save(os.path.join(UPLOAD_FOLDER, filename))

    return render_template("index.html", filename=filename)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()