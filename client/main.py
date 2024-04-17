import asyncio
import multiprocessing

from service import ClientService
from settings import settings


def run(*args):
    print(args)
    params = args[0]
    client = ClientService(pid=params[0], request_count=params[1], delay_range=params[2])
    asyncio.run(client.start())


if __name__ == "__main__":

    requests_count = settings.CONNECTION_VALUE // settings.CONNECTION_COUNT

    args = [(i, requests_count, settings.DELAY_RANGE) for i in range(settings.CONNECTION_COUNT)]

    with multiprocessing.Pool(processes=settings.CONNECTION_COUNT) as pool:
        try:
            pool.map(run, args)
        except KeyboardInterrupt:
            pool.close()
            pool.join()
