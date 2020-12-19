class NotFoundException(Exception):
    def __init__(self, resource_name, id):
        self.resource_name = resource_name
        self.id = id
        super().__init__("Resource not found")

class ValidationException(Exception):
    def __init__(self, errors):
        self.errors = errors
        super().__init__("Validation error")
