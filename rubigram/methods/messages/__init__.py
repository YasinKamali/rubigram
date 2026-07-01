from .send_message import SendMessage
from .send_file import SendFile
from .edit_message import EditMessage
from .forward_messages import ForwardMessages
from .get_messages import GetMessages
from .get_messages_interval import GetMessagesInterval
from .get_messages_updates import GetMessagesUpdates
from .delete_messages import DeleteMessages
from .auto_delete_message import AutoDeleteMessage
from .get_message_share_url import GetMessageShareUrl
from .get_messages_by_id import GetMessagesByID
from .get_link_from_app_url import GetLinkFromAppUrl
from .send_live import SendLive

class Messages(
    EditMessage,
    SendMessage,
    SendFile,
    ForwardMessages,
    GetMessages,
    GetMessagesInterval,
    GetMessagesUpdates,
    DeleteMessages,
    AutoDeleteMessage,
    GetMessageShareUrl,
    GetMessagesByID,
    GetLinkFromAppUrl,
    SendLive
):
    pass