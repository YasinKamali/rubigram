#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from typing import Optional, Any


class Storage:
    STATES: dict[str, Any] = {}
    DATA: dict[str, dict[str, Any]] = {}

    def __init__(self):
        pass

    def set_state(self, user_id: str, state: str):
        self.STATES[user_id] = state
        return True

    def get_state(self, user_id: str) -> Any:
        return self.STATES.get(user_id)

    def check_state(self, user_id: str, state: Any) -> bool:
        return self.STATES.get(user_id) == state

    def delete_state(self, user_id: str):
        self.STATES.pop(user_id, None)
        return True

    def set_data(self, user_id: str, data: dict[str, Any]):
        if user_id in self.DATA:
            self.DATA[user_id].update(data)
        else:
            self.DATA[user_id] = data
        return True

    def get_data(self, user_id: str, key: Optional[str] = None) -> Any:
        if key is None:
            return self.DATA.get(user_id)

        return self.DATA.get(key, {}).get(key)

    def delete_data(self, user_id: str, key: Optional[str] = None):
        if key is None:
            self.DATA.pop(user_id, None)
        else:
            if user_id in self.DATA:
                self.DATA[user_id].pop(key, None)

        return True