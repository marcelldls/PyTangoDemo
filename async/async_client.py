import asyncio
from tango.asyncio import DeviceProxy
from time import sleep


async def async_read():
    dev = await DeviceProxy("test/tempcontroller_device/01")

    while True:
        #res = await dev.enabled(wait=False)  # Does not work
        res = await dev.read_attribute('enabled', wait=False)
        print(res.value)


class accumulator:
    def __init__(self, difficulty=1):
        self.store = 0
        self.difficulty = difficulty

    def work(self):
        sleep(self.difficulty)
        self.store = self.store + 1
        print(f"{self.store} work completed")


def do_work(task_man):
    task_man.work()


async def main():

    # run the background task
    asyncio.create_task(async_read())

    task_man = accumulator(difficulty=0.5)

    # execute blocking call in a new thread
    for _ in range(10):
        await asyncio.to_thread(do_work, task_man)

    # Does not run forever

asyncio.run(main())  # An asyncio application
