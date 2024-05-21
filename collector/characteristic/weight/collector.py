from bleak import BleakClient

from model.scale_response import ScaleResponse
from .operations import notify


async def collect_weight(client: BleakClient, scale_response: ScaleResponse):
    await notify(client, scale_response, 30)
