from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label": "Mi tarea hecha", "done": True}
]

from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label": "Mi tarea hecha", "done": True}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Solicitud entrante con el siguiente cuerpo:", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("Esta es la posición a eliminar:", position)
    if position >= 0 and position < len(todos):
        del todos[position]
        return jsonify(todos)
    else:
        return "Error: La posición especificada está fuera de rango"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)