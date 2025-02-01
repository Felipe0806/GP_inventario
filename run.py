from app import app  # Importa la instancia 'app' desde 'app/__init__.py'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")  # Asegúrate de que Flask se ejecute en cualquier host
