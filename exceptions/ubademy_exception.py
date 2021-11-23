class UbademyException(Exception):
    def __init__(self, status_code, detail):
        super().__init__(detail)
        self.detail = detail
        self.status_code = status_code


# Exam Template Exceptions


class InvalidExamStateException(UbademyException):
    def __init__(self, detail):
        msg = f"Exam template has an invalid state: \"{detail}\". Expected values: are \"active\" and \"inactive\""
        super().__init__(status_code=400, detail=msg)


class InvalidExamTemplateScoreException(UbademyException):
    def __init__(self, detail):
        msg = f"Exam template has a non positive max_score: {detail}"
        super().__init__(status_code=400, detail=msg)


class InvalidExamFilterException(UbademyException):
    def __init__(self, has_multiple_choice, has_written, has_media):
        msg = (f"Exam template has invalid filters while trying to publish the exam. "
               f"has_multiple_choice: {has_multiple_choice}, "
               f"has_written: {has_written}, "
               f"has_media: {has_media}")
        super().__init__(status_code=400, detail=msg)


# Question Template Exceptions


class InvalidQuestionTypeException(UbademyException):
    def __init__(self, detail):
        msg = (f"Question template has an invalid type: \"{detail}\". "
               f"Expected values: are \"multiple_choice\", \"written\" and \"media\"")
        super().__init__(status_code=400, detail=msg)


class EmptyOptionListException(UbademyException):
    def __init__(self):
        msg = "Question template has an empty option list for a multiple choice question"
        super().__init__(status_code=400, detail=msg)


class EmptyCorrectException(UbademyException):
    def __init__(self):
        msg = "Question template has an empty correct value for a multiple choice question"
        super().__init__(status_code=400, detail=msg)


class NonPositiveQuestionTemplateValueException(UbademyException):
    def __init__(self, detail):
        msg = f"Question template has a non positive value: {detail}"
        super().__init__(status_code=400, detail=msg)


# Exam Solution Exceptions


class NonPositiveExamSolutionMaxScoreException(UbademyException):
    def __init__(self, detail):
        msg = f"Exam solution has a non positive max_score: {detail}"
        super().__init__(status_code=400, detail=msg)


class NonPositiveExamSolutionScoreException(UbademyException):
    def __init__(self, detail):
        msg = f"Exam solution has a non positive score: {detail}"
        super().__init__(status_code=400, detail=msg)
