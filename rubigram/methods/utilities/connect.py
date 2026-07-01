import logging
import rubigram


logger = logging.getLogger(__name__)


class Connect:
    async def connect(
        self: "rubigram.Client"
    ):
        await self.connection.connect()
        
        if self.connect_handler:
            await self.connect_handler.execute(self, None)