import os
import io
import aiofiles

from typing import Optional, Union, Callable

import rubigram
from rubigram import utils
from rubigram.enums import FileType


class SendFile:
    async def send_file(
        self: "rubigram.Client",
        guid: str,
        file: Union[str, bytes, io.BytesIO],
        type: "FileType" = FileType.FILE,
        name: Optional[str] = None,
        caption: Optional[str] = None,
        thumbnail: Optional[Union[str, bytes]] = None,
        reply_to_message_id: Optional[str] = None,
        is_spoil: bool = False,
        artist: Optional[str] = None,
        chunk_size: Optional[int] = None,
        timeout: Optional[float] = None,
        file_inline: Optional[dict] = None,
        progress: Callable = None,
        progress_args: tuple = (),
        *args, **kwargs
    ) -> ...:
        FileInline = file_inline
        if not FileInline:
            file_data = await self.upload(file, name, chunk_size, timeout, progress=progress, progress_args=progress_args, *args, **kwargs)
            FileInline = {
                "dc_id": file_data.dc_id,
                "file_id": file_data.id,
                "file_name": file_data.name,
                "size": file_data.size,
                "mime": file_data.mime,
                "access_hash_rec": file_data.access_hash_rec,
                "type": type.value,
                "is_spoil": is_spoil
            }

        if not FileInline:
            raise

        if guid in ["me", "self"]:
            guid = self.guid

        input = {
            "file_inline": FileInline,
            "object_guid": guid,
            "rnd": utils.rnd(),
            "reply_to_message_id": reply_to_message_id
        }

        if type in [FileType.IMAGE, FileType.VIDEO, FileType.GIF, FileType.VIDEO_MESSAGE]:
            thumb_inline = None
            thumb_inline_bytes = None

            if thumbnail:
                if isinstance(thumbnail, bytes):
                    thumb_inline_bytes = thumbnail
                elif utils.islink(thumbnail):
                    thumb_inline_bytes = await self.server.request(thumbnail, "GET")
                elif os.path.exists(thumbnail):
                    async with aiofiles.open(thumbnail, "rb") as fp:
                        thumb_inline_bytes = await fp.read()
                else:
                    thumb_inline_bytes = None

            if thumb_inline_bytes:
                thumb_inline = utils.get_image_thumbnail(thumb_inline_bytes)

            if not type == FileType.IMAGE:
                video_data = utils.get_video_data(file_data.file)
                input["file_inline"]["time"] = video_data[2] * 1000

            file_size = utils.get_image_size(
                file_data.file) if type == FileType.IMAGE else video_data[1]
            input["file_inline"]["width"] = file_size[0]
            input["file_inline"]["height"] = file_size[1]

            if type == FileType.VIDEO_MESSAGE:
                input["file_inline"]["type"] = "Video"
                input["file_inline"]["is_round"] = True

            input["file_inline"]["thumb_inline"] = thumb_inline or utils.get_image_thumbnail(
                file_data.file
            ) if type == FileType.IMAGE else video_data[0]

        elif type in [FileType.MUSIC, FileType.VOCIE]:
            input["file_inline"]["time"] = utils.get_voice_duration(
                file_data.file
            ) * (1000 if type == FileType.VOCIE else 1)

            if type == FileType.MUSIC:
                input["file_inline"]["music_performer"] = artist or utils.get_music_artist(
                    file_data.file
                )

        if caption:
            text, metadata = self.parser.parse(caption)
            input['text'] = text
            input['metadata'] = metadata

        return await self.invoke("sendMessage", input, timeout=timeout)