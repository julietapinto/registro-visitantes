from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

# FUNCIÓN DE CONEXIÓN (IMPORTANTE)
def get_connection():
    return pymysql.connect(
        host="kodama.proxy.rlwy.net",
        user="root",
        password="MHaldhPJAvTVSpJcuDCXXzUtTwIAPWSE",  
        database="railway",
        port=34642,
        cursorclass=pymysql.cursors.DictCursor
    )

# OBTENER VISITANTES
@app.route('/visitantes', methods=['GET'])
def obtener_visitantes():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM visitantes")
    resultados = cursor.fetchall()

    conn.close()

    return jsonify(resultados)

# GUARDAR VISITANTE
@app.route('/visitantes', methods=['POST'])
def guardar_visitante():
    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO visitantes(nombre, identificacion, motivo)
    VALUES(%s, %s, %s)
    """

    cursor.execute(sql, (
        data['nombre'],
        data['identificacion'],
        data['motivo']
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "mensaje": "Visitante registrado"
    })

if __name__ == '__main__':
    app.run(debug=True)