from rest_framework.exceptions import APIException


class TechnologyDoesNotExist(APIException):
    status_code = 400
    default_detail = 'The requested technology does not exist.'

class BuildingDoesNotExist(APIException):
    status_code = 400
    default_detail = 'The requested building does not exist.'
