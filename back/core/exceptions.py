from rest_framework.views import exception_handler

def core_exception_handler(exc, context):
    # DRF response to the exc exception.
    response = exception_handler(exc, context)
    # Dictionary of all supported errors with their handler.
    handlers = {
        'ProfileDoesNotExist': _handle_generic_error,
        'ValidationError': _handle_generic_error
    }
    # Type of the current exception.
    exception_class = exc.__class__.__name__
    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)
    return response

def _handle_generic_error(exc, context, response):
    ''' 
    Wrap DRF response in the `errors` key.
    '''
    response.data = {'errors': response.data}
    return response
