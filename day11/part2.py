from dataclasses import dataclass

from _utils.text_utils import get_lines


@dataclass
class Device:
    """A device"""

    name: str
    children: list[str]


def get_devices(lines: list[str]) -> dict[str, Device]:
    """Gets the devices from the data"""
    devices: dict[str, Device] = {}

    for line in lines:
        name, children = line.split(": ")
        device: Device = Device(name=name, children=children.split(" "))
        devices[name] = device

    return devices


def get_total_routes_to_out(device_name: str, devices: dict[str, Device]) -> int:
    """Gets the total routes to out from a device"""
    if device_name == "out":
        return 1
    device: Device = devices[device_name]
    if len(device.children) == 0:
        return 0

    return sum(
        (get_total_routes_to_out(child_name, devices)) for child_name in device.children
    )


def get_result_part_2(data: str) -> int:
    """Gets the result"""

    lines: list[str] = get_lines(data)
    devices: dict[str, Device] = get_devices(lines)

    # Multiple devices can start with svr
    return get_total_routes_to_out("svr", devices)
