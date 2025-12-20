from dataclasses import dataclass
from functools import cache

from _utils.text_utils import get_lines


@dataclass
class Device:
    """A device"""

    name: str
    children: list[str]


def get_devices(lines: list[str]) -> dict[str, Device]:
    """Gets the devices from lines"""
    devices: dict[str, Device] = {}

    for line in lines:
        name, children = line.split(": ")
        device: Device = Device(name=name, children=children.split(" "))
        devices[name] = device

    return devices


def get_result_part_2(data: str) -> int:
    """Gets the result"""

    lines: list[str] = get_lines(data)
    devices: dict[str, Device] = get_devices(lines)

    # Find all of the paths that lead from svr to out. How many of those paths visit both dac and fft?
    @cache
    def get_total_routes_to_out(
        device_name: str, seen_dac: bool, seen_fft: bool
    ) -> int:
        """Gets the total routes to out from a device"""
        if device_name == "out":
            return 1 if seen_dac and seen_fft else 0
        device: Device = devices[device_name]
        if len(device.children) == 0:
            return 0

        if device_name == "dac":
            seen_dac = True
        if device_name == "fft":
            seen_fft = True

        return sum(
            (get_total_routes_to_out(child_name, seen_dac, seen_fft))
            for child_name in device.children
        )

    return get_total_routes_to_out("svr", False, False)
