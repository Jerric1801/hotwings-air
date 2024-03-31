from flask import jsonify, request
from app import app, db
from app import schema

@app.route('/graphql', methods=['POST'])
def graphql():
    data = request.get_json()
    query = data.get('query')
    variables = data.get('variables', {})

    result = schema.execute(
        query,
        variable_values=variables,
    )

    # Preparing the response object
    response = {"data": result.data}
    if result.errors:
        # Formatting errors as a list of messages
        response['errors'] = [error.message for error in result.errors]

    return jsonify(response)