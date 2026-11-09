from flask import Flask, request, jsonify
app = Flask(name)
students = {
1: {"id": 1, "EMP": "Sreshta", "SAL": 10000}
}
@app.route('/employees', methods=['GET'])
def get_():
    return jsonify(list(students.values()))
@app.route('/emplyees', methods=['POST'])
def add_student():
    data = request.json
    emp_id = data['id']
    employees[emp_id] = data
    return jsonify({"message": "added successfully"})
@app.route('/   employees/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.json
    employees[id] = {
        "id": id,
        "EMP": data['EMP'],
        "SAL": data['SAL']
        }
return jsonify({"message": "updated successfully"})
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_student(id):
    del students[id]
    return jsonify({"message": "deleted successfully"})
app.run(host='0.0.0.0', port=5000)