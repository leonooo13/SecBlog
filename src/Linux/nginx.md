# nginx
Nginx（发音为“engine-x”）是一款高性能的 Web 服务器和反向代理服务器软件。它具有占用资源少、稳定可靠、支持高并发等优点，因此被广泛应用于互联网企业中。

以下是 Nginx 的一些常见用途：

1. Web 服务器：Nginx 可以作为一个 HTTP 服务器来提供静态文件和处理动态请求。

2. 反向代理服务器：Nginx 可以将客户端请求转发到多个后端服务器上，实现负载均衡和高可用性。

3. 邮件代理服务器：Nginx 还可以用来作为邮件代理服务器，提供 SMTP、POP3 和 IMAP 协议支持。

4. WebSocket 服务器：Nginx 可以作为 WebSocket 服务器来实现全双工通信功能，在实时应用程序中得到广泛应用。

5. RTMP 服务器：Nginx 还可以作为流媒体服务器，提供 RTMP 协议支持，用于视频直播等场景。

Nginx 采用了事件驱动的异步架构，可以高效地处理大量并发连接。同时，Nginx 还支持模块化扩展，用户可以根据自己的需求选择不同的模块来进行二次开发或定制化配置。由于其卓越的性能和灵活性，在互联网企业中得到了广泛的应用。
# 负载均衡的算法
在 Nginx 中，常用的负载均衡算法有以下几种：

1. 轮询（Round Robin）：将请求轮流分配给每个后端服务器，保证每个服务器都能获得相同数量的请求。

2. 加权轮询（Weighted Round Robin）：与轮询类似，但是可以为每个后端服务器分配一个权重值，根据权重值的大小来决定分配的请求数量。

3. 最少连接数（Least Connections）：将请求分配给当前连接数最少的服务器，以确保资源使用最优化。

4. IP Hash：根据客户端 IP 地址的哈希值来确定请求分配给哪个后端服务器，这样可以确保同一客户端的请求总是被分配到同一台服务器上，保证会话的可靠性。此算法适用于无状态应用。

5. Fair：基于后端服务器的响应时间和连接数等指标，动态地调整请求分配策略，从而实现最优化的负载均衡策略。该算法需要安装第三方模块才能使用。

需要注意的是，在实际应用中，不同的负载均衡算法适用于不同的场景，需要根据具体的业务需求和系统架构来选择合适的算法。
## Fask的部署
```python
# app.py
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run()
```
在开发中 使用`python app.py`进行启动，在部署中可以使用uwsgi和nginx来实现负载均衡
### 使用uwsgi
`uwsgi --socket 0.0.0.0:5000--protocol=http -p 3-w run:app`
`uwsgi --socket 0.0.0.0:5000--protocol=http -p 3-w run:app` 命令用于启动一个 uWSGI 应用服务器，用于运行 Flask Web 应用程序。

该命令的各个参数含义如下：

- `--socket 0.0.0.0:5000`：指定监听 IP 地址和端口号，0.0.0.0 表示监听所有网卡。
- `--protocol=http`：指定使用 HTTP 协议进行通信。
- `-p 3`：指定启动 3 个 worker 进程，用于处理用户请求。可以根据需要调整此参数来优化性能。
- `-w run:app`：指定要运行的应用程序，run 表示运行 run.py 文件，app 表示 Flask 应用程序实例名称。

在执行该命令之前，需要确保已经安装了 uWSGI 和 Flask 库，并且在项目目录下创建了名为 `run.py` 的文件，其中包含 Flask 应用程序的代码。

当命令执行完成后，Web 应用程序将会运行在指定的地址和端口上，您可以使用浏览器或命令行工具对其进行访问。

`uwsgi --http :8000 --wsgi-file app.py --callable app`
准备好配置文件后，命令行运行`uwsgi --ini uwsgi.ini`即可
```py
# filename:start.ini
[uwsgi]
#uwsgi启动时，所使用的地址和端口（这个是http协议的）
http=0.0.0.0:8000
#指向网站目录
chdir=/Users/wangjie/PycharmProjects/flask
#python 启动程序文件
wsgi-file=app.py
#python 程序内用以启动的application 变量名
callable=app
#处理器数
processes=4
#线程数
threads=2
```
`uwsgi --ini start.ini` 启动