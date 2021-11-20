class UbademyException(Exception):
    def __init__(self, status_code, detail):
        super().__init__(detail)
        self.detail = detail
        self.status_code = status_code


class InvalidExamStateException(UbademyException):
    def __init__(self):
        msg = "Exam template has an invalid state"
        super().__init__(status_code=400, detail=msg)


class InvalidQuestionTypeException(UbademyException):
    def __init__(self):
        msg = "Question template has an invalid type"
        super().__init__(status_code=400, detail=msg)
