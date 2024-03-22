from flask import Flask, request, jsonify

app = Flask(__name__)

# Список допустимых HWID, которые вы получили от пользователей
allowed_hwids = set()

@app.route('/check_hwid', methods=['POST'])
def check_hwid():
    data = request.json
    received_hwid = data.get('hwid')

    if received_hwid in allowed_hwids:
        return jsonify({'message': 'HWID подтвержден'}), 200
    else:
        return jsonify({'message': 'Неправильный HWID'}), 403

@app.route('/add_hwid', methods=['POST'])
def add_hwid():
    data = request.json
    new_hwid = data.get('hwid')
    allowed_hwids.add(new_hwid)
    return jsonify({'message': 'HWID добавлен успешно'}), 200

if __name__ == '__main__':
    app.run(debug=True)