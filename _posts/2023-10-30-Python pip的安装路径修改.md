---
title: Python pip的安装路径
categories: Python
tags:
- pip
---

1. `python -m site`

查看最后两行的`user_base`,`user_site`

2. 修改Lib/site.py

``` python
USER_SITE = "D:\Program Files\Python310\Lib\site-packages"
USER_BASE = "D:\Program Files\Python310\Scripts"
```
上面一行的user_base等价于
`USER_BASE = "D:\Program Files"`
会自动寻址