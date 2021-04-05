import time
import os
import mwclient
import requests
from pathlib import Path

"""
"""

site = mwclient.Site("www.minkewiki.org", path='/', scheme='http')
root = Path("images")


reversed_ns = {
    v: k
    for k, v in site.namespaces.items()
}


if __name__ == "__main__":
    ns_id = reversed_ns['文件']
    for p in site.allpages(namespace=ns_id):
        path = root / p.page_title
        path.parent.mkdir(exist_ok=True, parents=True)
        print(p.page_title)
        with open(path, 'wb') as fd:
            p.download(fd)
        time.sleep(2)