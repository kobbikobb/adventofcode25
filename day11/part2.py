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


def get_device_item(parent_name: str, devices: dict[str, Device]) -> DeviceItem:
    """Gets the device item"""

    cache: dict[str, DeviceItem] = {}
    stack: list[str] = [parent_name]

    # Poplulate items without children
    while stack:
        current_name = stack.pop()
        if current_name in cache:
            continue

        cache[current_name] = DeviceItem(name=current_name, children=[])
        stack.extend(devices.get(current_name, Device("", [])).children)

    # Popluate children
    for name, item in cache.items():
        device: Device | None = devices.get(name)
        if device:
            item.children = [
                cache[cache_name]
                for cache_name in device.children
                if cache_name in cache
            ]

    return cache[parent_name]


def get_result_part_2(data: str) -> int:
    """Gets the result"""

    lines: list[str] = get_lines(data)
    devices: dict[str, Device] = get_devices(lines)

    # dac = get_device_item("dac", devices)
    # fft = get_device_item("fft", devices)

    svr = get_device_item("svr", devices)
    # How many of those paths visit both 'dac' and 'fft'?

    # 1. Find all paths from 'dac' to 'out'.
    # 2. Find all paths from 'fft' to 'out'.
    # 3. Find all paths from 'dac' to 'svr'.
    # 4. Find all paths from 'fft' to 'svr'.
    # 5. Combine the paths.
    # 6. Count unique paths.

    return len(svr.children)  # Placeholder return value
