import rubigram


class Propagation:
    async def stop_propagation(self):
        raise rubigram.StopPropagation

    async def continue_propagation(self):
        raise rubigram.ContinuePropagation