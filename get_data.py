from suds.client import Client
from suds.sudsobject import asdict
from bs4 import BeautifulSoup


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
    def return_tag(line, tag="line"):
        soup = BeautifulSoup(line, "html.parser")
        return soup.line.string

    client = Client(url)
    response = client.service.DFUBrowseData(LogicalName=scope, Count=3)
    results = response.Result.split('\n')
    # only get the lines which has the tag <Row>
    result = [result for result in results if '<Row>' in result]

    try:
        # Get the data between line
        lines = [return_tag(line) for line in result]
        return lines
    except:
        import xmltodict, json
        collector = "<dataset>" + "".join(result) + "</dataset>"
        o = xmltodict.parse(collector)
        return json.dumps(o)



def get_data(full_name):
    url = "http://10.239.227.6:8010/WsDfu/DFUBrowseData?ver_=1.31&wsdl"
    result = get_result(url, full_name)
    return result



print "File: vivek::c_ecolids.csv : "
print get_data("jctest::people")

