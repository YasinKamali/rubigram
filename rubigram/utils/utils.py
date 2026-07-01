import os
import logging
import asyncio
import textwrap
import tempfile
import functools

from time import time
from io import BytesIO
from filetype import guess
from getpass import getpass
from typing import Optional
from base64 import b64encode
from mutagen import mp3, File
from urllib.parse import urlparse
from random import choices, randint
from concurrent.futures.thread import ThreadPoolExecutor as Executor

# from user_agent import generate_user_agent
# from .enums import Platform


try:
    from PIL import Image
except (ImportError, RuntimeError):
    Image = None

try:
    from moviepy.editor import VideoFileClip
except (ImportError, RuntimeError):
    VideoFileClip = None


logger = logging.getLogger(__name__)


UTF8: str = "UTF-8"
DEFAULT_THUMBNAIL: str = "iVBORw0KGgoAAAANSUhEUgAAACgAAAARCAIAAAAg6XlfAAAEwUlEQVR4nK1VXWwUVRQ+587s7HZ3u+x0u/3bav8WgQqkP1RpKdW0adXgSxFjCg9gxJhomvCIz/pgNE0gjfHBv6ARjVFDNCUagkkLTbS0Sw00BYoUuuy23dLZ7ezs7szszD0+jMEXoj70PJ2cLznfPSfnfh8SEWxiEAFxYAIALCsX/1z9fDpxt6asb2DHW8GSCgDgRAwRAHAzibntUGazN+cefPZAuSShcE3hSW2j0lvW1fT60/VDLkEkIAAUN42VCJhgq2v58x+ZG2O+KFflLZbEGGa2SO5lvXQkNr/N+O1Q7RN7AhVAgETkDI2Ij+r2/yDigFiY+lb/aRTWkuLuSnelN8v1ZKh4rijPqi1c2AkolDbIJAjtZZVDkR3iI/sSkVN8JKUTDkRECADICrEZ7fS7UoR4QOaIuqW4WWhn9ZtSuDd7/XpsecEtipIQZmUlV+4s6T/eEQFAVVVVVYPBoN/vN01TkiRELBQKAKAoCgBEIhEAcCDbtonItu1UKuX3+2VZLuo6c7nshUVzqYajxxtICIxj00vSjtfAV70N4P1nq369W3/2xlUyLd+5eOj8/eyGKebz+ZGRkYaGhkwm09HRMTU1deLEidnZ2cXFxXw+n8vlfD6fYRj79++fnp4+fPjwzMxMJpNZWVkxTdMwjM7OTm1DFeQtnX6/CoYn659PNHl6X9m15yACAHEOiIi99VtbKmreGf5CurYmlLqgVGK6rgeDwWPHjkWj0Xg83tPTc+rUqYmJiYGBAU3T9u7de+DAgVQqlU6nDcMgItM0dV03TbOjoyMSiSiKYtmWbhYZ43mSxij6lb4rUaxWMqmMkuYEDNEqWllNE00rm7LmCbKARRuZ2+1OJpOjo6OJRKK3t7e9vX19fb21tdXv9xcKhcnJyZMnT/b39zvbRkSPxwMAjLHZ2dmVlRUism3uFeCWJX9stv1hVQvAXWAS4EY2u7q6qmlaPp8jzjmQ4IKsAddVECxVLBQKVVVVw8PDD8+qsbExHA4713706NF0On3mzJnjx4/H4/GlpaVYLNbc3JxIJPr6+mzbvnDhQn1dQ8A2bxrBqQ2hRTYFBBciASBjlmWZpimKIoIN6MraUpVkDMlLT7kV0efzdXd3ExHnHBEZYy0tLaFQCBG7u7t1Xa+tre3q6mKMDQ4Ojo2NRSKRffv22bY9Pj4uSdKRI0eU9bTX7165vWwTLW4UmcETRG2InKFBgEAAAJLMteShwM223N2Qp5hD138r18Ov9e/xzacTn7z3c0lTeVz2hp+L9rZEng946ktczB9GLMK9MXb7rOvKvdx9WVfK0AIRADjnjLGHLZzREdGpOwni31LjbIVz7rzYyRljW5+sWW4so2i5wEkkmlK12Lr5THngZW08eOvLYuYaCd684GbVGY+Y5HLP5mg1EQHi15dvnP5+JrmqNvdvL9/+OMvN+4zv+kvnWvNiZdYjcNSvrnG1ILb1eQ++vWkm4SxjNaON/hCbgQd1j12uMieRCtsqQkGvq0Qr1C9r8r06qecNT9sLsLnuZHMSGALAkrJwaeGDudXfOYhtlf6AqDN3dTQ8VF8+yAQJHJHfXD8mAk5cYAwA5pIXf7nxYcSr7I682Fj5qlsKAfxjnX8BoH+PlgeA47wAAAAASUVORK5CYII="


def get_image_size(data: bytes) -> tuple[int]:
    """Return width and height image"""
    return Image.open(BytesIO(data)).size


def get_image_thumbnail(data: bytes) -> str:
    image = Image.open(BytesIO(data))
    width, height = image.size
    if height > width:
        new_height = 40
        new_width = round(new_height * width / height)
    else:
        new_width = 40
        new_height = round(new_width * height / width)
    image = image.resize((new_width, new_height), Image.LANCZOS)
    changed_image = BytesIO()
    image.save(changed_image, format="PNG")
    return b64encode(changed_image.getvalue()).decode(UTF8)


def get_video_data(data: bytes) -> list:
    try:
        with tempfile.NamedTemporaryFile(delete=False, dir=".") as tmp:
            tmp.write(data)
            tmp_path = tmp.name

        os.chmod(tmp_path, 0o777)

        with VideoFileClip(tmp_path) as clip:
            duration = clip.duration
            resolution = clip.size
            thumbnail = clip.get_frame(0)
            thumbnail_image = Image.fromarray(thumbnail)
            thumbnail_buffer = BytesIO()
            thumbnail_image.save(thumbnail_buffer, format="JPEG")
            thumbnail_b64 = b64encode(thumbnail_buffer.getvalue()).decode(UTF8)

        os.remove(tmp_path)
        return thumbnail_b64, resolution, duration

    except Exception as error:
        logger.error(
            "Error to get video data: %s", error
        )
        return DEFAULT_THUMBNAIL, [900, 720], 1


def get_voice_duration(data: bytes) -> int:
    file = BytesIO()
    file.write(data)
    file.seek(0)
    return mp3.MP3(file).info.length


def get_music_artist(data: bytes) -> str:
    try:
        audio = File(BytesIO(data), easy=True)

        if audio and "artist" in audio:
            return audio["artist"][0]

        return "rubigram"

    except:
        return "rubigram"


CHAT_TYPES: dict[str, str] = {
    "b": "Bot",
    "u": "User",
    "g": "Group",
    "c": "Channel",
    "s": "Service"
}


async def ainput(prompt: str = "", *, hide: bool = False, loop: Optional[asyncio.AbstractEventLoop] = None):
    """Just like the built-in input, but async"""
    if isinstance(loop, asyncio.AbstractEventLoop):
        loop = loop
    else:
        loop = get_event_loop()

    with Executor(1) as executor:
        func = functools.partial(getpass if hide else input, prompt)
        return await loop.run_in_executor(executor, func)


def rnd() -> str:
    return str(randint(10000000, 999999999))


def get_mime_from_bytes(value: bytes) -> str:
    mime = guess(value)
    return mime.extension if mime else "bin"


def islink(value: str) -> bool:
    return str(value).startswith(("http://", "https://"))


# def create_user_agent(platform: Platform) -> str:
#     if platform == Platform.ANDROID:
#         return generate_user_agent(os='android')
#     elif platform == Platform.PWA:
#         return generate_user_agent(os='android', navigator='chrome')
#     else:
#         return generate_user_agent(os='win', navigator='chrome')


def fix_base64(s):
    return s + '=' * (-len(s) % 4)


def create_tmp_session() -> str:
    return "".join(choices("abcdefghijklmnopqrstuvwxyz", k=32))


def create_device_hash() -> str:
    return str(randint(-99999999, 99999999))


def get_state() -> int:
    return int(time()) - 150


def get_chat_type_by_guid(object_guid: str) -> str:
    return CHAT_TYPES.get(object_guid[0])


def parse_phone_number(phone_number: str) -> str:
    phone_number = phone_number.strip()

    if phone_number.startswith("0") or phone_number.startswith("+"):
        phone_number = phone_number[1:]

    if not phone_number.startswith("98"):
        phone_number = "98" + phone_number

    return phone_number


def get_event_loop() -> asyncio.AbstractEventLoop:
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    return loop


def get_file_name_from_url(url: str) -> str:
    return os.path.basename(urlparse(url).path)


def remvoe_none_value(data: dict):
    return {
        key: value for key, value in data.items() if value is not None
    }


def clean_key(private_key: str) -> str:
    """
    Cleans an RSA private key by removing the standard BEGIN/END markers.

    Args:
        private_key: The raw private key string, potentially with markers.

    Returns:
        The content of the private key string without the markers.

    Raises:
        ValueError: If the input private key is empty after stripping whitespace.
    """
    if not private_key:
        raise ValueError("Private key cannot be empty.")

    cleaned_key = private_key.strip()

    # Check if the key starts and ends with the standard markers
    begin_marker = "-----BEGIN RSA PRIVATE KEY-----"
    end_marker = "-----END RSA PRIVATE KEY-----"

    if cleaned_key.startswith(begin_marker) and cleaned_key.endswith(end_marker):
        # Find the start and end positions of the actual key content
        content_start = cleaned_key.find(begin_marker) + len(begin_marker)
        content_end = cleaned_key.rfind(end_marker)

        # Extract the content between the markers and strip any leading/trailing whitespace
        key_content = cleaned_key[content_start:content_end].strip()
    else:
        # If markers are not present, assume the entire cleaned key is the content
        key_content = cleaned_key

    # Optionally, you might want to remove newline characters from the content as well,
    # depending on how you plan to use this cleaned key.
    # For now, we just return the content stripped of surrounding whitespace.
    # If you want to remove all newlines within the content:
    # key_content = key_content.replace('\n', '')

    return key_content


def format_key(private_key: str) -> str:
    """
    Formats an RSA private key by ensuring it starts and ends with standard markers
    and wraps lines to a maximum of 64 characters.

    Args:
        private_key: The raw private key string.

    Returns:
        The formatted private key string.

    Raises:
        ValueError: If the input private key is empty or invalid.
    """
    if not private_key:
        raise ValueError("Private key cannot be empty.")

    cleaned_key = private_key.strip()

    if cleaned_key.startswith("-----BEGIN RSA PRIVATE KEY-----") and cleaned_key.endswith("-----END RSA PRIVATE KEY-----"):
        content_start = cleaned_key.find(
            "-----BEGIN RSA PRIVATE KEY-----") + len("-----BEGIN RSA PRIVATE KEY-----")
        content_end = cleaned_key.rfind("-----END RSA PRIVATE KEY-----")
        key_content = cleaned_key[content_start:content_end].strip()
    else:
        key_content = cleaned_key

    wrapped_lines = textwrap.wrap(
        key_content, width=64, break_long_words=False, break_on_hyphens=False)

    formatted_key = "-----BEGIN RSA PRIVATE KEY-----\n" + \
        "\n".join(wrapped_lines) + "\n-----END RSA PRIVATE KEY-----"

    return formatted_key
