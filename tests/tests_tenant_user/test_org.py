from employee_benefits.tenant_user.org_ctrl import validate_org


def test_org_name_succeeds():
    '''
    Test that a valid submission passes
    '''
    new_org = {
        'org_name': 'Temple Consulatants',
        'city': 'Philadelphia',
        'state': 'PA',
        'country': 'USA',
        'admin_user_id': '3',
    }

    assert validate_org(new_org) == (True, 'Success')


def test_org_name_missing_fails():
    '''
    Test that a missing org_name fails.
    '''
    new_org = {
        'org_name': '',
        'city': 'Philadelphia',
        'state': 'PA',
        'country': 'USA',
        'admin_user_id': '3',
    }

    assert validate_org(new_org) == (False, 'Organization Name is required')


def test_city_missing_fails():
    '''
    Test that a missing city fails.
    '''
    new_org = {
        'org_name': 'Temple Consultants',
        'city': '',
        'state': 'PA',
        'country': 'USA',
        'admin_user_id': '3',
    }

    assert validate_org(new_org) == (False, 'City is required')


def test_state_missing_fails():
    '''
    Test that a missing state fails.
    '''
    new_org = {
        'org_name': 'Temple Consultants',
        'city': 'Philadelphia',
        'state': '',
        'country': 'USA',
        'admin_user_id': '3',
    }

    assert validate_org(new_org) == (False, 'State is required')


def test_country_missing_fails():
    '''
    Test that a missing country fails.
    '''
    new_org = {
        'org_name': 'Temple Consultants',
        'city': 'Philadelphia',
        'state': 'PA',
        'country': '',
        'admin_user_id': '3',
    }

    assert validate_org(new_org) == (False, 'Country is required')


def test_admin_user_id_missing_fails():
    '''
    Test that a missing admin_user_id fails.
    '''
    new_org = {
        'org_name': 'Temple Consultants',
        'city': 'Philadelphia',
        'state': 'PA',
        'country': 'USA',
        'admin_user_id': '',
    }

    assert validate_org(new_org) == (False, 'Admin User is required')


def test_string_admin_user_id_missing_fails():
    '''
    Test that a missing admin_user_id fails.
    '''
    new_org = {
        'org_name': 'Temple Consultants',
        'city': 'Philadelphia',
        'state': 'PA',
        'country': 'USA',
        'admin_user_id': 'Conwell',
    }

    assert validate_org(new_org) == (False, 'Admin User ID must be a number')
