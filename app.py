import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/music_collection")
def music_collection():
    music = mongo.db.music.find()
    return render_template("music.html", music=music)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        users = mongo.db.users
        existing_user = users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        return redirect(url_for(
                            "home", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        users = mongo.db.users
        existing_user = users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "email": request.form.get("email").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["userLog"] = request.form.get("username").lower()
        flash("You are registered! Please log in")
        return redirect(url_for("login", username=session["userLog"]))
    return render_template("register.html")


@app.route("/logout")
def logout():
    flash("You have logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/user_profile")
def user_profile():
    return render_template("user_profile.html")


@app.route("/file/<filename>")
def file(filename):
    print(filename)
    return mongo.send_file(filename)


@app.route("/share", methods=["GET", "POST"])
def share():
    if request.method == "POST":
        print(request.files["inputImageArtwork"].filename)
        piece={
            "title": request.form.get("inputTitle"),
            "artist": request.form.get("inputArtist"),
            "sound": request.files["inputSoundFile"].filename,
            "sheetmusic": request.files["inputSheetMusic"].filename,
            "genre": request.form.get("inputGenre"),
            "instrument": request.form.get("inputInstrument"),
            "user": session["user"],
            "image": request.files["inputImageArtwork"].filename
        }
        mongo.db.music.insert_one(piece)
        flash("Music upload shared")
    if "inputImageArtwork" in request.files:
        inputImageArtwork = request.files["inputImageArtwork"]
        mongo.save_file(inputImageArtwork.filename, inputImageArtwork)
    if "inputSoundFile" in request.files:
        inputSoundFile = request.files["inputSoundFile"]
        mongo.save_file(inputSoundFile.filename, inputSoundFile)
    if "inputSheetMusic" in request.files:
        inputSheetMusic = request.files["inputSheetMusic"]
        mongo.save_file(inputSheetMusic.filename, inputSheetMusic)
    return render_template("share.html")


@app.route("/delete_piece/<piece_id>")
def delete_piece(piece_id):
    mongo.db.music.remove({"_id": ObjectId(piece_id)})
    flash("Your music share has been deleted")
    return redirect(url_for("music_collection"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
