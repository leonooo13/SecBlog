SQL注入是一种攻击技术，黑客通过在Web应用程序中注入恶意的SQL代码来破坏或获取敏感信息。攻击者通常通过在Web应用程序表单和URL参数中注入恶意的SQL代码来实现SQL注入攻击。

例如，攻击者可以在Web应用程序的登录页面上注入以下SQL代码：

`SELECT * FROM users WHERE username = '' OR 1=1; --' AND password = '';`

这段代码将返回所有用户的详细信息，因为OR 1=1永远为true。攻击者还使用双破折号（--）来注释掉原始的SQL查询，并在语句的末尾添加了一个单引号（'），以确保原始查询不会执行。

为了防止SQL注入攻击，开发人员应始终使用参数化查询或预处理语句来构建SQL查询，而不是直接将用户输入连接到查询字符串中。此外，开发人员应该对用户输入进行严格的验证和过滤，以删除任何可能的恶意代码。

除此之外，还有其他防范SQL注入的措施，比如限制应用程序用户的访问权限、使用安全的编码标准以及定期更新应用程序以修复已知的漏洞等。
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

