import logging


def generate_error_api_response(api_response, input_data):
    data = api_response.json()
    message = f"message: {data['message']} | status code: {api_response.status_code} | user input: {input_data}"
    create_log_to_db(message)

    return {
        "message": data['message'],
        "result": {},
        "status_code": api_response.status_code
    }


def create_log_to_db(message):
    db_logger = logging.getLogger('db')
    db_logger.exception(message)