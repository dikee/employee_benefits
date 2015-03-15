import common_utils


def validate_user(user):
    try:
        email = user['email']
        password = user['password']
        confirm_password = user['confirm_password']
        first_name = user['first_name']
        last_name = user['last_name']
    except KeyError:
        return (False, 'Missing Value')

    if common_utils.is_none_or_blank(email):
        return (False, 'Email is required.')

    if not common_utils.is_valid_email(email):
        return (False, 'Invalid Email.')

    if common_utils.is_none_or_blank(first_name):
        return (False, 'First Name is required.')

    if common_utils.is_none_or_blank(last_name):
        return (False, 'Last Name is required.')

    if len(password) < 8:
        return (False, 'Password must be eight characters.')

    if password != confirm_password:
        return (False, 'Passwords do not match.')

    return (True, 'Success')
