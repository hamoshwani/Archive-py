import re
from func import request
from urllib.parse import unquote
def only(target, fro, to, filters, only,limit):
    if limit:
        url = 'https://web.archive.org/cdx/search/cdx?url=*.' + str(
            target) + '&output=text&fl=original&collapse=urlkey&limit=' + str(
            limit) + '&filter=statuscode:' + str(
            filters)
    else:
        url = 'https://web.archive.org/cdx/search/cdx?url=*.' + str(
            target) + '&output=text&fl=original&collapse=urlkey&limit=20000&filter=statuscode:' + str(
            filters)
    res = request.req(url)
    u = unquote(res)
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', u)
    mylist = list(dict.fromkeys(urls))
    final=[]
    for i in mylist:
        i = i
        final.append(i)
    return list(set(final))