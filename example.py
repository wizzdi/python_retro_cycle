from retro_cycle import _parse_and_decode
import pprint

json_str = """
{
    "name": "John Doe",
    "address": {
        "street": "123 Main St",
        "city": "Springfield",
        "country": "USA",
        "json-id": "1"
    },
    "contact": {
        "home": {
            "phone": "555-555-5555",
            "address": "1"
        }
    }
}
"""

value = _parse_and_decode(json_str)
pprint.pprint(value)
