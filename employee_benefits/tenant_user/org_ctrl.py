from employee_benefits.common_utils import common_utils


def validate_org(org):
    org_name = org.get('org_name', None)
    city = org.get('city', None)
    state = org.get('state', None)
    country = org.get('country', None)
    admin_user_id = org.get('admin_user_id', None)

    if common_utils.is_none_or_blank(org_name):
        return (False, 'Organization Name is required')

    if common_utils.is_none_or_blank(city):
        return (False, 'City is required')

    if common_utils.is_none_or_blank(state):
        return (False, 'State is required')

    if common_utils.is_none_or_blank(country):
        return (False, 'Country is required')

    if common_utils.is_none_or_blank(admin_user_id):
        return (False, 'Admin User is required')

    try:
        int(admin_user_id)
    except:
        return (False, 'Admin User ID must be a number')

    return (True, 'Success')
