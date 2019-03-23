from rest_framework.exceptions import APIException


class SourceTechnologyDoesNotExist(APIException):
    status_code = 400
    default_detail = 'The requested source technology does not exist.'

class SourceBuildingDoesNotExist(APIException):
    status_code = 400
    default_detail = 'The requested source building does not exist.'

class SourceEventDoesNotExist(APIException):
    status_code = 400
    default_detail = 'The requested source event does not exist.'

class TechnologyDoesNotExist(APIException):
    status_code = 400
    default_detail = 'The requested technology does not exist.'

class BuildingDoesNotExist(APIException):
    status_code = 400
    default_detail = 'The requested building does not exist.'

class EventDoesNotExist(APIException):
    status_code = 400
    default_detail = 'The requested event does not exist.'