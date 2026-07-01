import logging
import rubigram


logger = logging.getLogger(__name__)


class Disconnect:
    async def disconnect(
        self: "rubigram.Client"
    ):
        await self.connection.disconnect()

        if self.disconnect_handler:
            await self.disconnect_handler.execute(self, None)