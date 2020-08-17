# Archive-py
Customizing web archives result
## Overview

Archive-py is a Python project for customizing web archives result

## Futures
* Search for urls between dates
* Modify your archive search result limit
* Search for custom strings in urls
* Extract parameters from target's archive result
* Find common filenames from target's archive result
* Find domains from target's archive result
* Exclude extensions
* Search based on statuscode
* Coloruful results so you can see results better

## Installation

Use [python3](https://www.python.org/downloads/) to use Archive-py.

```bash
$ git clone https://github.com/hamoshwani/Archive-py.git
$ cd Archive-py
$ pip3 install -r requirements.txt
$ python3 archive.py -u example.com -c 200
```

## Usage

```code

 █████╗ ██████╗  ██████╗██╗  ██╗██╗██╗   ██╗███████╗
██╔══██╗██╔══██╗██╔════╝██║  ██║██║██║   ██║██╔════╝
███████║██████╔╝██║     ███████║██║██║   ██║█████╗
██╔══██║██╔══██╗██║     ██╔══██║██║╚██╗ ██╔╝██╔══╝
██║  ██║██║  ██║╚██████╗██║  ██║██║ ╚████╔╝ ███████╗
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝
Coded by:Ahmad Shwani

python3 archive.py --help for help
________________________________________________________

usage: ./archive.py -u [target] -c [statuscode]

optional arguments:
  -h, --help       How To Use This Tool
  -u Target        target url ex:google.com
  -f From          archive date from
  -t To            archive date to
  -c Statuscode    status code ex:200
  -l Limit         Archive limit try increase limit for better results default
                   is 20k
  -s Search        Only print Urls contains searched word
  -e Exclude       Exclude extensions ex:css,js
  --domains        extract only urls from archive result
  --params         Extract urls contains parameters
  --common Common  Search for common filenames ex:php,aspx,html
  --save           Saving results to output directory
```

## Command instructions
| Command  | Description |
| ------------- | ------------- |
| python3 archive.py -u example.com -c 200  | Shows web archives result  |
| python3 archive.py -u example.com -c 200 -s admin  | Search for admin keyword in web archives result  |
| python3 archive.py -u example.com -c 200 -f 2007 -t 2020 -s admin  | Search between dates for admin keyword  |
| python3 archive.py -u example.com -c 200 -f 2007 -t 2020 -l 50000  | Increasing search limit to 50k default is 20k  |
| python3 archive.py -u example.com -c 200 --params  | Extract urls contains parameters  |
| python3 archive.py -u example.com -c 200 --params -s id  | Extract parameters then search for id keyword  |
| python3 archive.py -u example.com -c 200 -e js,css  | Exclude extensions |
| python3 archive.py -u example.com -c 200 --common php  | Find common filenames php,asp,aspx,wsdl,tpl,admin,install  |
| python3 archive.py -u example.com -c 200 --domain --save  | Extract domains from archives result  |
| python3 archive.py -u example.com -c 200 --domain --save  | Saving results to output directory  |

## Contributing
Thank you for your interest in Archive-py. Your contributions are highly welcome.
* Report a bug.
* Help in fixing bugs.
* Suggest a feature.

Thanks to [devanshbatham](https://github.com/devanshbatham)
## Contact me
Twitter: [hamoshwani](https://twitter.com/hamoshwani)

Email: hhamoka3@gmail.com


