from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config["DEBUG"] == True

def valUN(inp):
    return (len(inp) > 2 and len(inp) < 21)

def valPass(p, p2):
    return ((not p == None) and p == p2)

def valEM(inp):
    if len(inp) == 0:
        return True
    if (not inp.count("@") == 1) or (not inp.count(".") == 1):
        return False
    if inp.find("@") > inp.find("."):
        return False
    return True

@app.route("/", methods=["POST"])
def trySignup():
    un = request.form["username"]
    if un == None:
        un = ""
    em = request.form["email"]
    if em == None:
        em = ""
    p = request.form["password"]
    p2 = request.form["v_password"]

    er = "" #TODO fix this so the html doesn't autoescape
    if not valUN(un):
        er += "<p>Your username needs to be between 3 and 20 characters long.</p>"
    if not valPass(p, p2):
        er += "<p>Either you forgot to put in a password, or they don't match.</p>"
    if not valEM(em):
        er += "<p>Your email doesn't match the correct format.</p>"

    if er == "":
        return render_template("success.html")
    return render_template("signup.html", error=er, username=un, email=em)


@app.route("/", methods=["GET"])
def index():
    return render_template("signup.html", error="", username="", email="")

app.run()