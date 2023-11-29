from flask import Flask, request, jsonify

app = Flask(__name__)

heart = [
    {
        "heart_id": "0",
        "date": "11/29/2023",
        "heart_rate": "78bpm",
    },
    {
        "heart_id": "1",
        "date": "11/29/2023",
        "heart_rate": "20bpm",
    },
]
@app.route('/heart', methods=['POST'])
def insert_new_heart():
    new_record = request.get_json()
    heart.append(new_record)
    return {'heart_id': len(heart)-1}, 200

@app.route('/heart', methods=['GET'])
def read_heart():
    return jsonify(heart)

@app.route('/heart/<int:index>', methods=['GET'])
def read_heart_id(index):
    specific = heart[index]
    return jsonify(specific)

@app.route('/heart/<int:index>', methods=['POST'])
def update_heart_id(index):
    update_record = request.get_json()
    heart[index] = update_record
    return {'heart_id': len(heart)}, 200

@app.route('/heart/<int:index>', methods=['DELETE'])
def delete_heart_id(index):
    heart.pop(index)
    return 'A record has been deleted', 200


if __name__ == "__main__":
    app.run()
