from bleak import BleakClient

from .operations import select_user_on_scale


async def select_user(client: BleakClient, pin):
    await select_user_on_scale(client, pin, 30)
