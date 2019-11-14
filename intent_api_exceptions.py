class IntentExceptionBase(Exception):

    def __init__(self, message, label, status_code):
        super().__init__(self)
        self.message = message
        self.label = label
        self.status_code = status_code

    def to_dict(self):
        rv = dict()
        rv['label'] = self.label
        rv['message'] = self.message
        return rv
        
        
class BodyMissingException(IntentExceptionBase):    
    def __init__(self):
        super().__init__("Request doesn't have a body.", "BODY_MISSING", 400)


class TextMissingException(IntentExceptionBase):
    def __init__(self):
        super().__init__("\"text\" missing from request body.", "TEXT_MISSING", 400)
    
    
class InvalidTextTypeException(IntentExceptionBase):
    def __init__(self):
        super().__init__("\"text\" is not a string.", "INVALID_TYPE", 400)
        
        
class TextEmptyException(IntentExceptionBase):
    def __init__(self):
        super().__init__("\"text\" is empty.", "TEXT_EMPTY", 400)
        

class InternalServerException(IntentExceptionBase):
    def __init__(self, message):
        super().__init__(message, "INTERNAL_ERROR", 500)