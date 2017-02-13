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


client = Client("http://10.239.227.6:8010/WsDfu/DFUInfo?ver_=1.31&wsdl")
response = client.service.DFUInfo(Name="vivek::c_ecolids.csv")
dict = recursive_translation(response)
print dict
import pdb
pdb.set_trace()
# response = client.DFUFileView()
# result = response['AddResult']
# print response