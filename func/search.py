import re
from urllib.parse import unquote
from func import request
def search(target, fro, to, filters, search, only,limit):
    global re
    if limit:
        url = 'https://web.archive.org/cdx/search/cdx?url=*.' + str(
        target) + '&output=text&fl=original&collapse=urlkey&limit='+str(
        limit)+'&filter=statuscode:' + str(
        filters)
    else:
        url = 'https://web.archive.org/cdx/search/cdx?url=*.' + str(
            target) + '&output=text&fl=original&collapse=urlkey&limit=20000&filter=statuscode:' + str(
            filters)
    if fro == None or to == None:
        resp = request.req(url)
        resp = unquote(resp)
        if search:
            final = []
            for line in resp.split("\n"):
                if search in line:
                    line = line.strip()

                    if search in line:
                        line = line.strip()
                    else:
                        line=line
                    final.append(line)
            return list(final)


        else:
            final=[]
            for i in resp.split("\n"):
                final.append(i)
            if "" in final:
                final.remove("")
            return final


    else:
        if limit:
            url1 = 'https://web.archive.org/cdx/search/cdx?url=*.' + str(
            target) + '&output=text&fl=original&collapse=urlkey&limit='+str(
            limit)+'&from=' + fro + '&to=' + to + '&filter=statuscode:' + str(
            filters)
        else:
            url1 = 'https://web.archive.org/cdx/search/cdx?url=*.' + str(
                target) + '&output=text&fl=original&collapse=urlkey&limit=20000&from=' + fro + '&to=' + to + '&filter=statuscode:' + str(
                filters)
        resp = request.req(url1)
        resp = unquote(resp)
        final = []
        if search:

            for line in resp.split("\n"):
                if search in line:
                    line = line.strip()

                    if search in line:
                        line = line.strip()

                    else:
                        line=line
                    final.append(line)
            return list(final)
        else:
            final = []
            for i in resp.split("\n"):
                final.append(i)
            if "" in final:
                final.remove("")
            return final
