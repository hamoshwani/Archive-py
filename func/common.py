from func import request
from urllib.parse import unquote

def common(target,filters,limit,search):
    if limit:
        url = 'https://web.archive.org/cdx/search/cdx?url=*.' + str(
        target) + '&output=text&fl=original&collapse=urlkey&limit='+str(
        limit)+'&filter=statuscode:' + str(
        filters)
    else:
        url = 'https://web.archive.org/cdx/search/cdx?url=*.' + str(
            target) + '&output=text&fl=original&collapse=urlkey&limit=20000&filter=statuscode:' + str(
            filters)
    resp = request.req(url)
    resp=unquote(resp)
    final=[]

    final=[i for e in search for i in resp.split("\n") if e in i]
    return final