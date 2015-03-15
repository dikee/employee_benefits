from Underwrite.underwrite.user_ctrl import validate_user

# user_ctrl = user.user_ctrl  # .user_ctrl import UserCtrl


def test_validate_new_user():
    '''
    Test that a valid submission passes
    '''
    new_user = {
        'email': 'dkalu@g.com',
        'password': 'foobar123',
        'confirm_password': 'foobar123',
        'org_id': 1,
        'first_name': 'Dike',
        'last_name': 'Kalu'
    }

    assert validate_user(new_user) == (True, 'Success')


def test_validate_new_user_fail():
    '''
    Test email is provided.
    '''
    new_user = {
        'email': '',
        'password': 'foobar123',
        'confirm_password': 'foobar123',
        'org_id': 1,
        'first_name': 'Dike',
        'last_name': 'Kalu'
    }

    assert validate_user(new_user) == (
        False,
        'Email is required.'
    )


def test_validate_new_user_fail2():
    '''
    Test passwords match.
    '''
    new_user = {
        'email': 'dkalu@g.com',
        'password': 'foobar123d',
        'confirm_password': 'foobar123',
        'org_id': 1,
        'first_name': 'Dike',
        'last_name': 'Kalu'
    }

    assert validate_user(new_user) == (
        False,
        'Passwords do not match.'
    )


def test_validate_password_eight_char():
    '''
    Test password exists.
    '''
    new_user = {
        'email': 'dkalu@g.com',
        'password': '',
        'confirm_password': 'fr123',
        'org_id': 1,
        'first_name': 'Dike',
        'last_name': 'Kalu'
    }

    assert validate_user(new_user) == (
        False,
        'Password must be eight characters.'
    )


def test_validate_new_user_fail3():
    '''
    Test First Name is provided.
    '''
    new_user = {
        'email': 'dkalu@g.com',
        'password': 'foobar123',
        'confirm_password': 'foobar123',
        'org_id': 1,
        'first_name': '',
        'last_name': 'Kalu'
    }

    assert validate_user(new_user) == (
        False,
        'First Name is required.'
    )


def test_validate_new_user_fail4():
    '''
    Test Last Name is required.
    '''
    new_user = {
        'email': 'dkalu@g.com',
        'password': 'foobar123',
        'confirm_password': 'foobar123',
        'org_id': 1,
        'first_name': 'Dike',
        'last_name': ''
    }

    assert validate_user(new_user) == (
        False,
        'Last Name is required.'
    )


def test_validate_new_user_fail5():
    '''
    Test email without @ fails.
    '''
    new_user = {
        'email': 'dkalug.com',
        'password': 'foobar123',
        'confirm_password': 'foobar123',
        'org_id': 1,
        'first_name': 'Dike',
        'last_name': 'Kalu'
    }

    assert validate_user(new_user) == (False, 'Invalid Email.')


def test_validate_new_user_fail6():
    '''
    Test email without '.' fails
    '''
    new_user = {
        'email': 'dkalu@gcom',
        'password': 'foobar123',
        'confirm_password': 'foobar123',
        'org_id': '',
        'first_name': 'Dike',
        'last_name': 'Kalu'
    }

    assert validate_user(new_user) == (False, 'Invalid Email.')


def test_validate_new_user_fail7():
    '''
    Test missing values
    '''
    new_user = {
        'emadil': 'dkalu@gcom',
        'password': 'foobar123',
        'confirm_password': 'foobar123',
        'org_id': '',
        'first_name': 'Dike',
        'last_name': 'Kalu'
    }

    assert validate_user(new_user) == (False, 'Missing Value')
