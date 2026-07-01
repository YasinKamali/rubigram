#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from enum import Enum


class UpdateType(Enum):
    UPDATED_MESSAGE = "UpdatedMessage"
    NEW_MESSAGE = "NewMessage"
    REMOVED_MESSAGE = "RemovedMessage"
    STARTED_BOT = "StartedBot"
    STOPPED_BOT = "StoppedBot"
    UPDATED_PAYMENT = "UpdatedPayment"