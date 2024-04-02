import math
import re

constants = {
    "in": {
        "rate": 1
    },
    "ft": {
        "rate": 12
    },
    "m": {
        "rate": 39.37
    },
    "rot": {
        "rate": 10.78 / (6 * math.pi)
    }
}

def parse_unit_string(unit_string: str):
    pattern = re.compile(r'\b(\d+(\.\d+)?)\s*(\w+)\b')
    return [[float(match.group(1)), match.group(3)] for match in pattern.finditer(unit_string)]

def convert(unit_string: str, unit_to: str) -> float:
    value = 0
    matches = parse_unit_string(unit_string)
    for match in matches:  
        number, unit = match
        value += (number * constants[unit]["rate"])
    return value / constants[unit_to]["rate"]
