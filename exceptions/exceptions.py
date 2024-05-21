from fastapi import HTTPException

class BadRequestException(HTTPException):
    def __init__(self)->None:
        super().__init__(status_code=400, detail="Order not created, invalid inputs")


class UserExistException(HTTPException):
    def __init__(self)->None:
        super().__init__(status_code=404, detail="User with this email already exists")