from suds.client import Client
from suds.sudsobject import asdict


def recursive_translation(d):
    result = {}
    for k, v in asdict(d).iteritems():
        if hasattr(v, '__keylist__'):
            result[k] = recursive_translation(v)
        elif isinstance(v, list):
            result[k] = []
            for item in v:
                if hasattr(item, '__keylist__'):
                    result[k].append(recursive_translation(item))
                else:
                    result[k].append(item)
        else:
            result[k] = v
    return result


def get_result(url, scope):
    client = Client(url)
    response = client.service.DFUFileView(Scope=scope)
    dict = recursive_translation(response)
    return dict