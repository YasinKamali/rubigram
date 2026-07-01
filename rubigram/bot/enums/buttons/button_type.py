#  RubigramClient - Rubika API library for python
#  Copyright (C) 2025-present Javad <https://github.com/DevJavad>
#  Github - https://github.com/DevJavad/rubigram


from enum import Enum


class ButtonType(Enum):
    SIMPLE = "Simple"
    SELECTION = "Selection"
    CALENDAR = "Calendar"
    NUMBER_PICKER = "NumberPicker"
    STRING_PICKER = "StringPicker"
    LOCATION = "Location"
    PAYMENT = "Payment"
    CAMERA_IMAGE = "CameraImage"
    CAMERA_VIDEO = "CameraVideo"
    GALLERY_IMAGE = "GalleryImage"
    GALLERY_VIDEO = "GalleryVideo"
    FILE = "File"
    AUDIO = "Audio"
    RECORD_AUDIO = "RecordAudio"
    MY_PHONE_NUMBER = "MyPhoneNumber"
    MY_LOCATION = "MyLocation"
    TEXTBOX = "Textbox"
    LINK = "Link"
    ASK_MY_PHONE_NUMBER = "AskMyPhoneNumber"
    ASK_LOCATION = "AskLocation"
    BARCODE = "Barcode"