import json as js

from flask import Flask, request

import app.service.salary_service as service

controller = Flask(__name__)


@controller.route('/compensation_data', methods=['GET'])
def compensation_data():
    try:
        result = service.process_request(request.args.to_dict())
        return create_response(http_status=200, result=result)
    except Exception as exception:
        return create_response(400, process_error(str(exception)))


def process_error(error_description):
    return {
        "result": "error",
        "description": error_description
    }


def create_response(http_status, result):
    return controller.response_class(
        response=js.dumps(result),
        status=http_status,
        mimetype='application/json'
    )
