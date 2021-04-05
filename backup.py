

import time
import mwclient
import requests
from pathlib import Path

"""
"""

site = mwclient.Site("www.minkewiki.org", path='/', scheme='http')
root = Path("data")

ns_list = [
    ('主空间', ''),
    ('模板', '模板'),
    ('分类', '分类')
]

reversed_ns = {
    v: k
    for k, v in site.namespaces.items()
}

missing_ns = {ns for _, ns in ns_list} - set(reversed_ns.keys())
assert not missing_ns, missing_ns

if __name__ == "__main__":
    for ns_name, ns in ns_list:
        ns_id = reversed_ns[ns]
        for p in site.allpages(namespace=ns_id):
            path = root / ns_name / f"{p.page_title}.txt"
            path.parent.mkdir(exist_ok=True, parents=True)
            print(f"{ns}:{p.page_title}")
            with open(path, 'w') as f:
                f.write(p.text())
            html_path = root / ns_name / f"{p.page_title}.html"
            res = requests.get("http://www.minkewiki.org/index.php", params={'title': p.page_title, 'printable':'yes'})
            html_code = res.text
            with open(html_path, 'w') as f:
                f.write(html_code)
            time.sleep(2)