import utility
from datetime import datetime
from dateutil import parser


def get_attrib(full_name):
    def _is_dir():
        if result['NumFiles'] == 0: return False
        else: return True

    def _get_ctime():
        def unix_time(time_string):
            dt = parser.parse(time_string)
            epoch = datetime.utcfromtimestamp(0)
            return (dt - epoch).total_seconds() * 1000.0

        all_ctime = [unix_time(element['Modified']) for element in result['DFULogicalFiles']\
    ['DFULogicalFile'] if element['isDirectory'] is False]
        return max(all_ctime)

    return_dict = {}
    result = utility.get_result(url, full_name)
    if _is_dir():
        return_dict = {
            'st_ctime': _get_ctime()
        }
    return return_dict

url = "http://10.239.227.6:8010/WsDfu/DFUFileView?ver_=1.31&wsdl"
print get_attrib("vivek")
