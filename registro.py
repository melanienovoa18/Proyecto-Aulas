from flask import Flask, render_template, request, session, redirect, url_for
from MethodUtil import MethodUtil
from UserLogic import UserLogic
from CardLogic import CardLogic
from CardObj import CardObj

app = Flask(__name__)
app.secret_key = "Reserv12345"

@app.route("/")
def index():
    return render_template ("index.html")

@app.route("/inicio_sesion", methods=MethodUtil.list_ALL())
def login():

    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        usuario = request.form["Usuario"]
        contra = request.form["contra"]
        
        logic = UserLogic()
        userData = logic.getUserData(usuario)

        if userData is not None:
            session['user'] = {"idUser": userData[0][0], "user":userData[0][1]}

            if userData[0][2] == contra:

                return render_template("reservaciones.html")
            else:
                return render_template("login.html")


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

@app.route("/info_tarjeta", methods=MethodUtil.list_ALL())
def info_tarjeta():
    if request.method == "GET":
        return render_template("info_tarjeta.html")
    if request.method == "POST":
        numero_tarjeta = request.form["numero_tarjeta"]
        mes_vencimiento = request.form["mes_vencimiento"]
        annos_vencimiento = request.form["annos_vencimiento"]
        CCV = request.form["CCV"]
        logic = CardLogic()
        confirmation = logic.insertCard( numero_tarjeta, mes_vencimiento, annos_vencimiento, CCV)
        if confirmation is True:
            return render_template("reserva_terminada.html")
        else:
            return redirect(url_for("info_tarjeta"), conv = confirmation)

@app.route("/cancelar")
def cancelar():
    return render_template("cancelar.html")

@app.route("/reserva_termianda")
def reserva_termianda():
    return render_template("reserva_terminada.html")

if __name__ == "__main__":
        app.run(debug=True)
