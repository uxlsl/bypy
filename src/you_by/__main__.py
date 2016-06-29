
"""
Python client for Baidu Yun (https://github.com/houtianze/bypy)
---

It provides file operations like: list, download, upload, syncup, syncdown, etc.

The main purpose is to utilize Baidu Yun in Linux environments (e.g. Raspberry Pi)

== NOTE ==
Proxy is supported by the underlying Requests library, you can activate HTTP proxies by setting the HTTP_PROXY and HTTPS_PROXY environment variables respectively as follows:
HTTP_PROXY=http://user:password@domain
HTTPS_PROXY=http://user:password@domain
(More information: http://docs.python-requests.org/en/master/user/advanced/#proxies)
Though from my experience, it seems that some proxy servers may not be supported properly.

---
@author:     Hou Tianze (GitHub: houtianze) and contributors
@license:    MIT

"""
from bypy import main


if __name__ == "__main__":
    main()
