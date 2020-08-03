from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template ("index.html")

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
    return render_template("info_tarjeta.html")

@app.route("/cancelar")
def cancelar():
    return render_template("cancelar.html")

@app.route("/reserva_termianda")
def reserva_termianda():
    return render_template("reserva_terminada.html")
if __name__ == "__main__":
    app.run(debug=True)