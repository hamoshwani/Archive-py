import requests
from fake_useragent import UserAgent


def req(url):
    resp=False
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    try:
        r = requests.get(url,headers=headers)
        resp=r.text
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
    except Exception as e:
        raise print(e)
    finally:
        return resp