import utility

url = "http://10.239.227.6:8010/WsDfu/DFUFileView?ver_=1.31&wsdl"
result = utility.get_result(url, "vivek")

files = [element['Name'] for element in result['DFULogicalFiles']\
    ['DFULogicalFile'] if element['isDirectory'] is False]
folders = [element['Directory'] for element in result['DFULogicalFiles']\
    ['DFULogicalFile'] if element['isDirectory'] is True]

print "Files: ", files
print "Folders: ", folders