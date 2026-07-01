class StopPropagation(StopAsyncIteration):
    pass


class ContinuePropagation(StopAsyncIteration):
    pass


from .rubigram import handlers, sync, types

from .rubigram.storage import Storage
from .rubigram import enums
from .rubigram.client import Client
from .rubigram.bot import Bot


__version__ = "1.7.34"
__author__ = ["PyJavad", "DeveloperYasin"]
__github__ = "https://github.ocm/DevJavad/rubigram"