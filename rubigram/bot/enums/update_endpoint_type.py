#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from enum import Enum


class UpdateEndpointType(Enum):
    RECEIVE_UPDATE = "ReceiveUpdate"
    RECEIVE_INLINE_MESSAGE = "ReceiveInlineMessage"
    RECEIVE_QUERY = "ReceiveQuery"
    GET_SELECTION_ITEM = "GetSelectionItem"
    SEARCH_SELECTION_ITEMS = "SearchSelectionItems"