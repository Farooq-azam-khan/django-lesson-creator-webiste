from django.core.exceptions import ValidationError

VALID_SUBJECTS = ['Math', 'Physics', 'English', 'Computer Science', 'History']
def validate_subject(value):
    cap_val = value.capitalize()
    print("capval:", cap_val)
    print("val: ", value)
    if  value not in VALID_SUBJECTS and cap_val not in VALID_SUBJECTS:
        ret_raise = "Subjects must be one of the following: {}".format(VALID_SUBJECTS)
        raise ValidationError(ret_raise)
