from func import request
from urllib.parse import unquote
import re

def params(target, fro, to, filters,limit,black_list):
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
        resp=unquote(resp)
        final = []
        ''' 
        regexp : r'.*?:\/\/.*\?.*\=[^$]'
        regexp : r'.*?:\/\/.*\?.*\='
        '''

        parsed = list(set(re.findall(r'.*?:\/\/.*\?.*\=[^$]', resp)))
        final_uris = []
        level=""

        for i in parsed:
            delim = i.find('=')
            second_delim = i.find('=', i.find('=') + 1)
            if len(black_list) > 0:
                words_re = re.compile("|".join(black_list))
                if not words_re.search(i):
                    final_uris.append((i[:delim + 1])+"FUZZ")
                    final_uris.append(i[:second_delim + 1]+"FUZZ")
            else:
                final_uris.append((i[:delim + 1])+"FUZZ")
                final_uris.append(i[:second_delim + 1]+"FUZZ")

#Param extractor coded by https://twitter.com/0xAsm0d3us, Thank you

        return list(set(final_uris))


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
        resp=unquote(resp)
        ''' 
        regexp : r'.*?:\/\/.*\?.*\=[^$]'
        regexp : r'.*?:\/\/.*\?.*\='
        '''

        parsed = list(set(re.findall(r'.*?:\/\/.*\?.*\=[^$]', resp)))
        final_uris = []
        place = "FUZZ"

        for i in parsed:
            delim = i.find('=')
            second_delim = i.find('=', i.find('=') + 1)
            if len(black_list) > 0:
                words_re = re.compile("|".join(black_list))
                if not words_re.search(i):
                    final_uris.append((i[:delim + 1]))
                    final_uris.append(i[:second_delim + 1])
            else:
                final_uris.append((i[:delim + 1]))
                final_uris.append(i[:second_delim + 1])


        return list(set(final_uris))
