class RecordAlreadyExistsError(Exception):
    message = "Record already exists."

class RecordDoesNotExistError(Exception):
    message = "Record does not exist."

class PhoneValueError(Exception):
    message = "Phone is not correct. Expected format is 10 digits."

class BirthdayValueError(Exception):
    message = "Birthday is not correct. Expected format is DD.MM.YYYY."