def get_home_page(user):
    if is_Accounts_Manager(user):
        return "homepage"
    if is_partner(user):
        return "partner-dashboard"
    return "index"


