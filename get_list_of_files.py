url =  "http://10.239.227.6:8010/WsDfu/DFUFileView?Scope="
import urllib2
import re

response = urllib2.urlopen(url)
lines = response.read()

# Extract all the lines which as Open Folder written in them
content_1 = [line for line in lines.split('\n') if "Open folder..." in line]
# Extract the href tags
content_2 = [re.findall(r'href=[\'"]?([^\'" >]+)', c)[-1] for c in content_1]
# Extract the scope tags
content_3 = [c.split('Scope=')[-1] for c in content_2]
# Decoding the url encoding
files = [urllib2.unquote(c).decode() for c in content_3]
for f in files: print f
import pdb
pdb.set_trace()