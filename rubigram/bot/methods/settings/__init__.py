#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from .set_bot_command import SetBotCommand
from .update_bot_endpoint import UpdateBotEndpoints


class Settings(
    SetBotCommand,
    UpdateBotEndpoints
):
    pass