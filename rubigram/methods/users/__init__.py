from .get_me import GetMe
from .get_user_info import GetUserInfo
from .update_username import UpdateUsername
from .get_contacts import GetContacts


class Users(
    GetMe,
    GetUserInfo,
    UpdateUsername,
    GetContacts
):
    pass