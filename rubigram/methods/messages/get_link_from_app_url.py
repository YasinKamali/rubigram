import rubigram


class GetLinkFromAppUrl:
    async def get_link_from_app_url(
        self: "rubigram.Client",
        url: str,
    ) -> ...:
        return await self.invoke("getLinkFromAppUrl", {
            "app_url": url,
        })