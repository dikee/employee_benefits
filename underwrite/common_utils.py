def is_none_or_blank(value):
    if value in ['', None]:
        return True
    return False


def is_valid_email(email):
    return '@' in email and '.' in email
