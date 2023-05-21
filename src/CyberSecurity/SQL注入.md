上传的SQL语句在服务器中进行了执行
包括
1. 输入可执行语句
2. 修改SQL查询条件语句
3. 在SQL语句中添加条件语句
前端的URL `wwww.url.com/index.php?id=1`
在后端的执行的SQL语句`$sql=“SELECT 123 FROM abc WHERE id='1'"`
比如一个页面里面有用户名和密码输入框
假设：验证SQL语句是`SELECT *FROM users WHERE uname='$uname' AND passwd='$passwd'`
攻击者可以通过输入以下内容来利用SQL注入漏洞：
uname: `"OR 1=1 --+`
passwd: `anything`
在这个例子中，攻击者在用户名输入框中输入了`'OR 1=1 --+`，这个代码将始终返回True，因为1等于1。在应用程序构建SQL查询语句时，这个输入将导致查询的WHERE子句变成：
`SELECT*FROM users WHERE uname=" OR 1=1 --+ AND passwd='$passwd'`
`sql="SELECT*FROM users WHERE uname=''OR 1=1 --+'' AND passwd='$passwd'"`
从而实现注入。

