from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/proceso",methods=["POST"])
def proceso():
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    ############
    lenguajes = request.form.getlist("cursos")
    return render_template("curso.html",nombre=nombre,apellido=apellido, lenguajes=lenguajes)

@app.route("/usuario")
def usuario():
    return render_template("usuario.html")

@app.route("/procesoC",methods=["POST"])
def procesoC():
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    correo = request.form.get("correo")
    clave =request.form.get("clave")
    ############
    return render_template("usuario1.html",nombre=nombre,apellido=apellido, correo=correo, clave=clave)

@app.route("/productos")
def productos():
    return render_template("productos.html")

@app.route("/procesoP", methods=["POST"])
def procesoP():
    product= request.form.get("product")
    carrito = request.form.getlist("carrito")
    existencia = request.form.get("existencia")
    precio = request.form.get("precio")

    return render_template("productos1.html", product= product, carrito=carrito, existencia=existencia, precio=precio)

@app.route("/libros")
def libros():
    return render_template("libros.html")

@app.route("/procesoL", methods=["POST"])
def procesoL():
    titulo= request.form.get("titulo")
    autor=  request.form.get("autor")
    medio= request.form.getlist("medio")
    resumen= request.form.get("resumen")

    return render_template("libros1.html", titulo=titulo,autor=autor,medio=medio,resumen=resumen)

if __name__ == "__main__":
    app.run(debug=True)
