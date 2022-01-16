import logging
from datetime import datetime


def generate_api_response(message, result, status_code):
    return {
        "message": message,
        "result": result,
        "status_code": status_code
    }

def generate_error_api_response(api_response, input_data):
    data = api_response.json()
    message = f"message: {data['message']} | status code: {api_response.status_code} | user input: {input_data}"
    create_log_to_db(message)

    return generate_api_response(
        message=data['message'],
        result={},
        status_code=api_response.status_code
    )


def create_log_to_db(message):
    # db_logger = logging.getLogger('db')
    # db_logger.exception(message)
    pass

def change_format_temperature(temperature):
    return "{:.2f}°C".format(((temperature) - 273.15))


def change_format_to_title(description):
    return str(description).title()


def change_format_wind(wind):
    return f"{wind} kmph"


def change_format_humidity(humidity):
    return f"{humidity}%"


def get_date_now():
    return datetime.now().strftime("%b %d %Y | %I:%M:%S %p")
