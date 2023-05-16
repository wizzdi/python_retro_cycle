import json

def _parse_and_decode(response):
    value = json.loads(response)
    if isinstance(value, dict):
        value = retro_cycle(value)
    return value

def do_retro_cycle(json, ref_map):
    for key, listV in json.items():
        if key == 'json-id':
            continue
        if isinstance(listV, str):
            val = ref_map.get(listV)
            if val is not None:
                if val != json:
                    json[key] = val
                else:
                    json[key] = None
        else:
            if isinstance(listV, dict):
                json_id = listV.get('json-id')
                if json_id is not None and json_id == json.get('json-id'):
                    continue
                else:
                    do_retro_cycle(listV, ref_map)
            elif isinstance(listV, list):
                for index in range(len(listV)):
                    element = listV[index]
                    if isinstance(element, dict):
                        do_retro_cycle(element, ref_map)
                    elif isinstance(element, str):
                        val = ref_map.get(element)
                        if val is not None:
                            if val != json:
                                listV[index] = val
                            else:
                                listV[index] = None
    return json

def get_reference_map(json):
    ref_map = {}
    populate_reference_map(json, ref_map)
    return ref_map

def populate_reference_map(json, ref_map):
    json_id = json.get('json-id')
    if json_id is not None:
        if ref_map.get(json_id) is None:
            ref_map[json_id] = json
        else:
            return
    for d in json.values():
        if isinstance(d, dict):
            populate_reference_map(d, ref_map)
        elif isinstance(d, list):
            for l in d:
                if isinstance(l, dict):
                    populate_reference_map(l, ref_map)

def retro_cycle(json):
    ref_map = get_reference_map(json)
    return do_retro_cycle(json, ref_map)
