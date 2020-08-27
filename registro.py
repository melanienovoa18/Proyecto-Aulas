from flask import Flask, render_template, request, session, redirect, url_for
from MethodUtil import MethodUtil
from UserLogic import UserLogic
app = Flask(__name__)

@app.route("/")
def index():
    return render_template ("index.html")

@app.route("/inicio_sesion", methods=MethodUtil.list_ALL())
def login():
    
    if request.method == "GET":
        return render_template ("login.html")
    if request.method == "POST": 
        usuario = request.form["Usuario"]
        contra = request.form["password"]

        logic = UserLogic()
        userData = logic.getUserData(usuario)

        if userData is not None: 
            session["iduser"] = userData.id
            session["username"] = userData.usuario

            if userData.password == contra: 


                 return redirect(url_for("login.html"))

@app.route("/usuario/sesion",  methods=MethodUtil.list_ALL())
def sesion():
    if "username" in session: 
        session.pop("username", None)

@app.route("/usuario")
def usuario():
    return render_template ("usuario.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")
    
@app.route("/reservaciones")
def reservaciones():
    return render_template("reservaciones.html")

@app.route("/extras")
def extras():
    return render_template("extras.html")

@app.route("/tipo_pago")
def tipo_pago():
    return render_template("tipo_pago.html")

@app.route("/info_tarjeta")
def info_tarjeta():
    return redirect(url_for("info_tarjeta.html"))

@app.route("/cancelar")
def cancelar():
    return render_template("cancelar.html")

@app.route("/reserva_termianda")
def reserva_termianda():
    return render_template("reserva_terminada.html")

if __name__ == "__main__":
    app.run(debug=True)
