## SSRF
服务端请求伪造，Attacker向服务端访问url，获取得服务端的资源的安全漏洞。需要向其他服务器获取资源。
eg：我不能直接访问A公司的网络，但是我向B公司的网络发起请求，B公司的一些资源需要A公司的服务器，，我就可以收到A公司的响应数据。
# PIKACHU
```php
?url=http://baidu.com
```
打开百度
## 危害
1. 内网探测
2. 窃取内网数据
3. 跳板攻击
4. 绕过安全啊防御
5. 拒绝服务攻击
## 利用
利用支持`URL Schema`发起请求伪造
读取本地文件
```php
?url=file:///etc/passwd
```
攻击内网应用漏洞 ``?url=ip.index.php?cmd=xxx`
绕过IP限制
	比如IPv6，十进制，八进制，十六进制，多进制混合IP，localhost替代
URL解析限制
	url欺骗，302跳转，Unicode转化
## 挖掘漏洞
1. 回显判断
2. 访问日志检查
3. 延时对比
4. DNS请求检测，DNSlog.cn
	`http://url.ssrf_curl.php?url=http://6s3rh1.dnslog.cn`
5. 容易出现的地方，能够对外放弃网络访问的地方，地址是用户可以控制的
	RSS订阅，字幕下载，支持`URL`输入，嵌入招聘，收取第三方邮件
	或者参数猜测 `url,domain,site,src,target`
	文件处理漏洞
	信息采集
	社交分享功能
## 防御
`Burp Collaborator` 默认提供DNS解析服务器
`SSRFmap` 常用漏洞
特定IP，特定域名，内网限制，禁用一些非必要协议