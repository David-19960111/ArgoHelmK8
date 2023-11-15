from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', mensaje='¡Hola, Flask!')

if __name__ == '__main__':
    # Configura Flask para escuchar en todas las interfaces en el puerto 3000
    app.run(host='0.0.0.0', port=3000, debug=True)