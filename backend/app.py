from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

# CONFIGURACIÓN MYSQL
db = pymysql.connect(
    host="mysql.railway.internal",
    user="root",
    password="MHaldhPJAvTVSpJcuDCXXzUtTwIAPWSE",
    database="railway"
)

# OBTENER VISITANTES
@app.route('/visitantes', methods=['GET'])
def obtener_visitantes():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM visitantes")
    resultados = cursor.fetchall()

    visitantes = []

    for fila in resultados:
        visitantes.append({
            "id": fila[0],
            "nombre": fila[1],
            "identificacion": fila[2],
            "motivo": fila[3],
            "fecha": str(fila[4])
        })

    return jsonify(visitantes)

# GUARDAR VISITANTE
@app.route('/visitantes', methods=['POST'])
def guardar_visitante():
    data = request.json

    nombre = data['nombre']
    identificacion = data['identificacion']
    motivo = data['motivo']

    cursor = db.cursor()

    sql = """
    INSERT INTO visitantes(nombre, identificacion, motivo)
    VALUES(%s, %s, %s)
    """

    cursor.execute(sql, (nombre, identificacion, motivo))
    db.commit()

    return jsonify({
        "mensaje": "Visitante registrado"
    })

if __name__ == '__main__':
    app.run(debug=True)