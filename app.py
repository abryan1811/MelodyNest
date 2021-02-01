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
    musicPieces = []
    for piece in music:
        musicGenreId = mongo.db.genres.find_one({"_id": ObjectId(piece["genre"])}).get("genre")
        musicInstrumentId = mongo.db.instruments.find_one({"_id": ObjectId(piece["instrument"])}).get("instrument")
        userId = mongo.db.users.find_one({"_id": ObjectId(piece["user"])}).get("username")
        piece = {
            "_id": piece["_id"],
            "genre": musicGenreId,
            "title": piece["title"],
            "artist": piece["artist"],
            "instrument": musicInstrumentId,
            "user": userId,
            "sound": piece["sound"],
            "sheetmusic": piece["sheetmusic"],
            "image": piece["image"]
        }
        musicPieces.append(piece)
    return render_template("music.html", music=musicPieces)


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
                        session["userId"] = str(existing_user["_id"])
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
            "firstName": request.form.get("firstName"),
            "surname": request.form.get("surname"),
            "email": request.form.get("email").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("You are registered! Please log in")
        return redirect(url_for("login", username=session["user"]))
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
    if request.method == "GET":
        genres = []
        genresDB = list(mongo.db.genres.find().sort("genre"))
        for genre in genresDB:
            genres.append(genre)
        instruments = []
        instrumentsDB = list(mongo.db.instruments.find().sort("instrument"))
        for instrument in instrumentsDB:
            instruments.append(instrument)
        return render_template("share.html", genres=genres, instruments=instruments)
    elif request.method == "POST":
        if "inputImageArtwork" in request.files:
            inputImageArtwork = request.files["inputImageArtwork"]
            mongo.save_file(inputImageArtwork.filename, inputImageArtwork)
        if "inputSoundFile" in request.files:
            inputSoundFile = request.files["inputSoundFile"]
            mongo.save_file(inputSoundFile.filename, inputSoundFile)
        if "inputSheetMusic" in request.files:
            inputSheetMusic = request.files["inputSheetMusic"]
            mongo.save_file(inputSheetMusic.filename, inputSheetMusic)
        musicGenreId = ""
        if (request.form.get("inputGenre") == "addNew"):
            genre = {
                "genre": request.form.get("newGenreText")
            }
            musicGenreId = mongo.db.genres.insert(genre)
            print("musicGenreId: ", musicGenreId)
        else:
            musicGenreId = request.form.get("inputGenre")
        instrId = ""
        if (request.form.get("inputInstrument") == "addNew"):
            instr = {
                "instrument": request.form.get("newInstrumentText")
            }
            instrId = mongo.db.instruments.insert(instr)
            print("instrId: ", instrId)
        else:
            instrId = request.form.get("inputInstrument")
        piece = {
            "genre": ObjectId(musicGenreId),
            "title": request.form.get("inputTitle"),
            "artist": request.form.get("inputArtist"),
            "instrument": ObjectId(instrId),
            "user": ObjectId(session["userId"]),
            "sound": request.files["inputSoundFile"].filename,
            "sheetmusic": request.files["inputSheetMusic"].filename,
            "image": request.files["inputImageArtwork"].filename
        }
        mongo.db.music.insert_one(piece)
        flash("Music upload shared")
        return redirect(url_for('music_collection'))


@app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    mongo.db.music.insert_one(piece)


@app.route("/delete_piece/<piece_id>")
def delete_piece(piece_id):
    mongo.db.music.remove({"_id": ObjectId(piece_id)})
    flash("Your music share has been deleted")
    return redirect(url_for("music_collection"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
