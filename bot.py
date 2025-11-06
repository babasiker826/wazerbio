from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('wazerbio.html')

@app.route('/api', methods=['POST'])
def api():
    try:
        data = request.get_json()
        # Burada gelen JSON verisini işleyebilirsin
        # Örnek olarak sadece geri döndürelim:
        return jsonify({
            "status": "success",
            "received": data
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
