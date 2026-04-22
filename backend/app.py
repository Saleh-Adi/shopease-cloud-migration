from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/products')
def get_products():
    return jsonify([{"id": 1, "name": "Cloud Computing Laptop"}, {"id": 2, "name": "Smartphone"}])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
