import requests

webhook_url = "http://localhost:5000/webhook"

data = {
    "evento": "usuario_creado",
    "datos_usuario": {
        "id": 123,
        "nombre": "Juan Pérez",
        "email": "juan.perez@example.com"
    }
}

response = requests.post(webhook_url, json=data)

if response.status_code == 200:
    print("WebHook enviado correctamente")
else:
    print(f"Error al enviar WebHook: {response.status_code}")
