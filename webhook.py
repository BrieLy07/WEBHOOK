from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Obtener los datos enviados en el WebHook
    data = request.json
    print(f"Datos recibidos en el WebHook: {data}")
    return jsonify({"message": "WebHook recibido correctamente"}), 200

if __name__ == '__main__':
    app.run(port=5000)
