from flask import Flask, request, render_template
import mysql.connector
import os

app = Flask(__name__)

# Railway database credentials
db_config = {
    "host": os.environ.get("DB_HOST", "interchange.proxy.rlwy.net"),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASSWORD", "VpUTUZxhQKFFmpEXrLeacOssnQfDmXFv"),
    "database": os.environ.get("DB_NAME", "NuevaAppBebe"),
    "port": 37968
}

@app.route('/bebe')
def mostrar_bebe():
    bebe_id = request.args.get('id')
    if not bebe_id:
        return "ID del bebé no proporcionado", 400

    try:
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM DatosNeonato WHERE idNeonato = %s", (bebe_id,))
        bebe = cursor.fetchone()

        if not bebe:
            return "Bebé no encontrado", 404

        return render_template('bebe.html', bebe=bebe)

    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
