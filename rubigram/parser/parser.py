from typing import Optional
from markdownify import markdownify

from rubigram.bot.enums import ParseMode
from .markdown import Markdown


class Parser:
    def __init__(
        self,
        parse_mode: "ParseMode" = ParseMode.MARKDOWN
    ):
        self.parse_mode = parse_mode

    def parse(self, text: str, parse_mode: Optional["ParseMode"] = None):
        mode = parse_mode or self.parse_mode

        if mode == ParseMode.HTML:
            text = markdownify(html=text)

        return Markdown.parse(text)