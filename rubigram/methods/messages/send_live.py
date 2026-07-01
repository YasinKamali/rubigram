# rubigram/live.py

from typing import Optional, List
import rubigram 
from rubigram.utils import utils


class SendLive:
    async def send_live(
        self: "rubigram.Client", # pyright: ignore[reportGeneralTypeIssues]
        title: str,
        object_guid: Optional[str] = None, 
        thumb_inline: Optional[str] = None, 
        suggestion_comments: Optional[List[str]] = None, 
        device_type: str = "Mobile"  # Mobile, Software
    ):
        """
        Start a live stream in Rubika
        
        Args:
            title: Live title (required)
            object_guid: Room/channel GUID (optional, personal live if None)
            thumb_inline: Cover image (base64 or guid)
            suggestion_comments: Predefined comment suggestions
            device_type: Device type (mobile, web, api)
        
        Returns:
            SendLiveOutput containing live_id, stream_url, etc.
        """
        
        input_data = {
            "title": title,
            "rnd": utils.rnd(),
            "device_type": device_type
        }
        
        if object_guid:
            input_data["object_guid"] = object_guid
        
        thumb_inline = utils.get_image_thumbnail(open('code.png','rb').read())
        input_data["thumb_inline"] = thumb_inline
        
        if suggestion_comments:
            input_data["suggestion_comments"] = suggestion_comments
        
        return await self.invoke("sendLive", input_data)