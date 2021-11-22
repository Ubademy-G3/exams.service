class UbademyException(Exception):
    def __init__(self, status_code, detail):
        super().__init__(detail)
        self.detail = detail
        self.status_code = status_code


class InvalidExamStateException(UbademyException):
    def __init__(self, detail):
        msg = f"Exam template has an invalid state: \"{detail}\". Expected values: are \"active\" and \"inactive\""
        super().__init__(status_code=400, detail=msg)


class InvalidQuestionTypeException(UbademyException):
    def __init__(self, detail):
        msg = f"Question template has an invalid type: \"{detail}\". "
        msg += "Expected values: are \"multiple_choice\", \"written\" and \"media\""
        super().__init__(status_code=400, detail=msg)


class EmptyOptionListException(UbademyException):
    def __init__(self):
        msg = f"Question template has an empty option list for a multiple choice question"
        super().__init__(status_code=400, detail=msg)


class EmptyCorrectException(UbademyException):
    def __init__(self):
        msg = f"Question template has an empty correct value for a multiple choice question"
        super().__init__(status_code=400, detail=msg)


class NonPositiveValueException(UbademyException):
    def __init__(self, detail):
        msg = f"Question template has a non positive value: {detail}"
        super().__init__(status_code=400, detail=msg)
