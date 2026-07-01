from .logout import Logout
from .register_device import RegisterDevice
from .send_code import SendCode
from .sign_in import SignIn


class Auth(
    Logout,
    RegisterDevice,
    SendCode,
    SignIn
):
    pass