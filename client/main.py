import asyncio
import multiprocessing
from multiprocessing import Process

from service import ClientService
from client.settings import settings


def run(*args):
    client = ClientService(pid=args[0], request_count=args[1], delay_range=args[2], lock=args[3])
    asyncio.run(client.start())


if __name__ == "__main__":

    requests_count = settings.CONNECTION_VALUE // settings.CONNECTION_COUNT

    lock = multiprocessing.Lock()

    process_pool = [Process(target=run, args=(connect, requests_count, settings.DELAY_RANGE, lock)) for connect in
                    range(settings.CONNECTION_COUNT)]

    for process in process_pool:
        try:
            process.start()
        except KeyboardInterrupt:
            process.close()
            process.join()
