`Samy`蠕虫攻击最大的xss漏洞
1. 反射型`xss`，不持久的跨站脚本，将代码放在url参数中进行执行，`<script>alert(1)</script>
	```php
	if arry_key_exists("name",$_GET){
	echo"Hello $_GET["name"];
	}
	```
	可以看到没有对name进行过滤，get后直接执行了。
2. 存储型`xss`，将恶意代码存储到服务器中，guest访问url就触发该xss，源代码和上面一样
3. DOM型`xss`，web和脚本语言连接起来的编程接口漏洞，不经过服务器，url进行触发
pikachu中点击文本框，将数据传输给了，`href='javascript:alert(1)`执行的函数
两种攻击  
1. Cookie获取 `document.cookie`![[Pasted image 20230406205900.png]]
2. Ajax
3. BeEF，包含丰富的xss漏洞利用功能  

### 检测
黑盒测试：  
	所有输入数据处输入`xss payload`，看是否解析出payload
	搜集测试案例：看是否有过滤
	如果script不能imag也可以
	自动化工具：dommate
白盒测试：sink
#### 防御：
输入检测：白名单限制，黑名单：特殊字符  
输出检测：服务器内一些标签  
企业中防御的方法：HTTPonly CSP  

