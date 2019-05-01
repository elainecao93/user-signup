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
    #TODO

@app.route("/", methods=['POST', 'GET'])
def index():
    er = ""
    un = request.args.get("username")
    if un == None:
        un = ""
    em = request.args.get("email")
    if em == None:
        em = ""
    p = request.args.get("password")
    p2 = request.args.get("v_password")

    if isCorrect: #TODO
        return render_template("success.html")
    return render_template("signup.html", error=er, username=un, email=em)

app.run()