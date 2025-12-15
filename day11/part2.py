from dataclasses import dataclass

from _utils.text_utils import get_lines


@dataclass
class Device:
    """A device"""

    name: str
    children: list[str]


@dataclass
class DeviceItem:
    """A device item"""

    name: str
    children: list["DeviceItem"]


def get_devices(lines: list[str]) -> dict[str, Device]:
    """Gets the devices from lines"""
    devices: dict[str, Device] = {}

    for line in lines:
        name, children = line.split(": ")
        device: Device = Device(name=name, children=children.split(" "))
        devices[name] = device

    return devices


def get_device_item(name: str, devices: dict[str, Device]) -> DeviceItem:
    """Gets the device item"""

    if not name in devices:
        return DeviceItem(name=name, children=[])

    return DeviceItem(
        name=name,
        children=[
            get_device_item(child_name, devices)
            for child_name in devices[name].children
        ],
    )


def get_result_part_2(data: str) -> int:
    """Gets the result"""

    lines: list[str] = get_lines(data)
    devices: dict[str, Device] = get_devices(lines)

    device_item = get_device_item("svr", devices)

    return len(device_item.children)
