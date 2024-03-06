from flask import request, make_response, jsonify

from BackendTaskApp import app, cursor
from BackendTaskApp.forms import DataHandleForm

@app.route('/api/assignment/query', methods=["POST"])
def assignment_query():
    request_data = request.get_json(True)
    form = DataHandleForm(**request_data)
    success, data = form.perform()
    if not success:
        return make_response(jsonify(description=form.form_error), form.error_code)
    return make_response(jsonify(data=data), 200)


@app.route('/api/test/query')
def test():
    query = "SELECT * FROM public.report_output WHERE main.dp > 90"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return jsonify(code="ok")
    