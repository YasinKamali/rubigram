from typing import Any
from dataclasses import dataclass, field

from rubigram.enums import ChatStatus, ChatAccess
from rubigram.types import LastMessage, Base, Keypad


@dataclass(repr=False)
class Chat(Base):
    auto_delete: str
    chat_keypad: "Keypad"
    create_time: int
    access:ChatAccess
    count_unseen: int
    group_my_last_send_time: int
    group_voice_chat_id: str
    has_schedule: bool
    is_archived: bool
    is_blocked: bool
    is_in_contact: bool
    is_mute: bool
    is_pinned: bool
    last_deleted_mid: int
    chat_last_message: ...  # ChatMessage
    last_seen_my_mid: int
    mute_expire_time: int
    object_guid: str
    offset_count_seen: int
    pinned_message_id: int
    pinned_message_ids: list[int]
    show_ask_spam: bool
    slow_mode_duration: int
    unseen_mention_message_count: int
    time_string: str
    last_message: "LastMessage"
    last_seen_peer_mid: str
    status: "ChatStatus"
    time: int
    last_message_id: str
    raw: dict = field(repr=False)

    @classmethod
    def read(cls, data: dict[str, Any], **kwargs) -> "Chat":
        data.update(kwargs)
        return cls(
            auto_delete= (data.get("auto_delete")),
            chat_keypad= Keypad.read(data.get("chat_keypad",{})),
            create_time= int(data.get("create_time",0)),
            access = [ChatAccess[access] for access in data.get("access",[])],
            count_unseen= int(data.get("count_unseen",0)),
            group_my_last_send_time= int(data.get("group_my_last_send_time",0)),
            group_voice_chat_id= (data.get("group_voice_chat_id")),
            has_schedule= bool(data.get("has_schedule")),
            is_archived= bool(data.get("is_archived")),
            is_blocked= bool(data.get("is_blocked")),
            is_in_contact= bool(data.get("is_in_contact")),
            is_mute= bool(data.get("is_mute")),
            is_pinned= bool(data.get("is_pinned")),
            last_deleted_mid= int(data.get("last_deleted_mid",0)),
            chat_last_message= None  ,# ChatMessage
            last_seen_my_mid= int(data.get("last_seen_my_mid",0)),
            mute_expire_time= int(data.get("mute_expire_time",0)),
            object_guid= (data.get("object_guid")),
            offset_count_seen= int(data.get("offset_count_seen",0)),
            pinned_message_id= int(data.get("pinned_message_id",0)),
            pinned_message_ids= [m_id for m_id in data.get("pinned_message_ids",[])],
            show_ask_spam= bool(data.get("show_ask_spam")),
            slow_mode_duration= int(data.get("slow_mode_duration",0)),
            unseen_mention_message_count= int(data.get("unseen_mention_message_count",0)),
            time_string= (data.get("time_string")),
            last_message= LastMessage.read(data.get("last_message")) if data.get("last_message") else None,
            last_seen_peer_mid= (data.get("last_seen_peer_mid")),
            status = ChatStatus[data.get("status")] if data.get("status") else None,
            time= int(data.get("time",0)),
            last_message_id= (data.get("last_message_id")),
            raw = data
        )
