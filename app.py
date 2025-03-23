from flask import Flask,render_template, request,redirect
import os

app = Flask(__name__)

@app.route('/',methods=["GET", "POST"])
def hello():
    
    if request.method == "POST":
        
        file = request.files["file"]
        
        filename = "prueba.csv"
        file.save(os.path.join("csv", filename))
        
        exec(open("FixPronicsyst.py").read())
        
        return redirect("/static/prueba.csv")
    
    
    context = {
        "nombre" : "condorito",
        "edad" : 42
        
    }
    return render_template("index.html",context=context)

