from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos
libros = [
    {"id": 1, "titulo": "1984", "autor": "George Orwell", "año": 1949},
    {"id": 2, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "año": 1967},
    {"id": 3, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "año": 1943},
]

# Ruta principal
@app.route("/")
def home():
    return jsonify({"mensaje": "Bienvenido a la API de Libros"}), 200

# Obtener todos los libros
@app.route("/api/libros", methods=["GET"])
def obtener_libros():
    return jsonify(libros), 200

# Obtener un libro por ID
@app.route("/api/libros/<int:libro_id>", methods=["GET"])
def obtener_libro_por_id(libro_id):
    libro = next((libro for libro in libros if libro["id"] == libro_id), None)
    if libro is None:
        return jsonify({"error": "Libro no encontrado"}), 404
    return jsonify(libro), 200

# Agregar un nuevo libro
@app.route("/api/libros", methods=["POST"])
def agregar_libro():
    datos = request.get_json()
    if not datos or "titulo" not in datos or "autor" not in datos or "año" not in datos:
        return jsonify({"error": "Datos inválidos"}), 400
    nuevo_libro = {
        "id": len(libros) + 1,
        "titulo": datos["titulo"],
        "autor": datos["autor"],
        "año": datos["año"],
    }
    libros.append(nuevo_libro)
    return jsonify(nuevo_libro), 201

# Actualizar parcialmente un libro por ID
@app.route("/api/libros/<int:libro_id>", methods=["PATCH"])
def actualizar_libro_parcial(libro_id):
    datos = request.get_json()
    libro = next((libro for libro in libros if libro["id"] == libro_id), None)
    if libro is None:
        return jsonify({"error": "Libro no encontrado"}), 404

    libro.update({key: value for key, value in datos.items() if key in libro})
    return jsonify(libro), 200

# Eliminar un libro por ID
@app.route("/api/libros/<int:libro_id>", methods=["DELETE"])
def eliminar_libro(libro_id):
    global libros
    libros = [libro for libro in libros if libro["id"] != libro_id]
    return jsonify({"mensaje": "Libro eliminado"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
