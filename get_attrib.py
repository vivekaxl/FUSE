import utility



def get_attrib(full_name):
    def _is_dir(result):
        if result['NumFiles'] == 0: return False
        else: return True

    def _get_ctimed():
        all_ctime = [utility.unix_time(element['Modified']) for element in result['DFULogicalFiles']\
    ['DFULogicalFile'] if element['isDirectory'] is False]
        return max(all_ctime)

    def _get_ctimef(result):
        return utility.unix_time(result['FileDetail']['Modified'])

    def _get_sizef(result):
        return int(result['FileDetail']['Filesize'].replace(',',''))

    def _get_nlinksf(result):
        return 1  # the n_links for a file is always 1

    def _get_st_modef(result):
        return 33188



    def _get_nlinks():
        """ Counts the number of folders in the folder + 2"""
        return len([element['Directory'] for element in result['DFULogicalFiles'] \
            ['DFULogicalFile'] if element['isDirectory'] is True]) + 2

    def _get_st_mode():
        """ refer to http://stackoverflow.com/questions/35375084/c-unix-how-to-extract-the-bits-from-st-mode """
        return 16877

    url = "http://10.239.227.6:8010/WsDfu/DFUFileView?ver_=1.31&wsdl"
    result = utility.get_result(url, full_name)
    if _is_dir(result):
        return_dict = {
            'st_ctime': _get_ctimed(),
            'st_mtime': _get_ctimed(),
            'st_nlinks': _get_nlinks(),
            'st_mode': _get_st_mode(),
            # Since it is a folder always return 4096
            'st_size': 4096,
            'st_gid': 1000,
            'st_uid': 1000,
            'st_atime': _get_ctimed()
        }
    else:
        url = "http://10.239.227.6:8010/WsDfu/DFUInfo?ver_=1.31&wsdl"
        result = utility.get_result(url, full_name)
        return_dict = {
            'st_ctime': _get_ctimef(result),
            'st_mtime': _get_ctimef(result),
            'st_nlinks': _get_nlinksf(result),
            'st_mode': _get_st_modef(result),
            # Since it is a folder always return 4096
            'st_size': _get_sizef(result),
            'st_gid': 1000,
            'st_uid': 1000,
            'st_atime': _get_ctimef(result)
        }
    return return_dict


print "File: vivek::c_ecolids.csv : ", get_attrib("vivek::c_ecolids.csv")
print "Folder: vivek : ", get_attrib("vivek")
print "Folder: vn : ", get_attrib("vn")
