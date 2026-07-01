from rubigram.types import Update
import rubigram
import logging


logger = logging.getLogger(__name__)


class GetUpdates:
    async def get__updates(self: "rubigram.Client") -> "Update":
        """
        Get updates from the server.

        Returns:
        - rubpy.types.Update: An Update object containing information about the updates.
        """

        while True:
            # try:
            return await self.get_updates()

            # except Exception as e:
            #     logger.error(f"Error get Updates {e}")
            #     raise e
            #     pass