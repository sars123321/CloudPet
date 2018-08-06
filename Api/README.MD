API
===
#api签名

###APPID
cloudpet
###APPSECRET
4e3de007cd2fc7372ec161208b2ce5313a6b3c42ff82adba2e5c776ba8df736e27b0745967b5cbd506801027b3a05cc7aef84d3055466d7987806fb14fe405a3
###Content-Type
application/json
###签名参数
auth
本参数写入headers
###重要说明
timestemp
为固定参数，必须要传取当前时间的unix时间戳10位（精确到秒）与服务器当前时间差保证在10秒之内，否则签名将无效
###签名规则
例：
(```)
body:{
    userid:123,
    name:'123321',
    type:10,
    timestemp:1222
}
(```)
对于该请求参数签名
1.按照key值进行排序，排序结果为：
`name  timestemp  type  userid`
2.将键值对组合:
`name=123321&timestemp=1222&type=10&userid=123`
3.拼接带加密字符串
`BASESTR = APPID + (name=123321&timestemp=1222&type=10&userid=123) + APPSECRET`
4.使用hmac md5进行加密 编码格式统一为utf8
`sign = hmac(APPSECRET, BASESTR , digestmod='MD5').tolower()`
###签名传递
(```)
content = {
    userid:123,
    name:'123321',
    type:10,
    timestemp:1222
}
fetch('http://localhost:5001/api/v1/user/register',{
    method:'POST',
    headers: {
    'Content-Type': 'application/json',
    'auth':sign
    },
    body:JSON.stringify(content)
    })
(```)

本示例签名结果为：
`97c5f6d08c61d0f5575e17203890b535`

#建议使用Crypto.js
