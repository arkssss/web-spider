## 爬虫入门 day1

### 1. HTTP协议

#### 1.1http请求	

- get  请求 : **直接拼接于访问url后**, 可以处理小规模是数据, 但是不安全
- post 请求: 不会拼接于url后, 比较安全, 且没有数据量的限制, 且可以上传文件
- put 请求
- delete 请求
- ...

get & post 请求的方法最为常用



#### 1.2 请求头信息 和 响应头信息

- Requestheader

  ```
  Accept: */*
  Accept-Encoding: gzip, deflate
  Accept-Language: zh-CN,zh;q=0.9
  Connection: keep-alive
  Content-Length: 0
  Cookie: nickname=%E5%B0%8F%E4%BB%BB%E7%9A%84%E5%B8%85%E8%88%9F; loving=90; birthday=19951103; register_time=2019-03-15%2012%3A47%3A00; face_img=fangzhou.png; id=2; email=522500442%40qq.com; username=19951103; PHPSESSID=s64k7q9snu9dj0uq6ilpft52o4
  Host: www.baidu.com
  Origin: www.baidu.com
  Referer: www.baidu.com
  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36
  X-Requested-With: XMLHttpRequest
  ```

  1. Accept : 表示接受的文本格式
  2. Accept-Encoding: 可以接受的编码格式
  3. Accept-Language
  4. Connection : 长链接 | 短链接
  5. User-Agent : 客户端的机器信息
  6. Referer : 跳转的页面

### 2.什么是爬虫 ? 

**使用代码模拟用户, 批量的发送网络请求** , 也就是说, 爬虫只能爬到作为一个用户可以访问到的数据, 而不能访问的的数据是不可以爬的.

#### 2.1 爬虫分类

1. 通用爬虫	

   使用搜索引擎 : 百度, 谷歌, ...

2. 聚焦爬虫

   **我们要学习的爬虫**

   只返回我们需要的数据

#### 2.2 爬虫的基本步骤

1. 获得目标网页的url

2. 利用python (java, go) 发送http请求

   **利用python的urllib.request 库**

3. 获得返回数据并且解析

4. 存储数据



### 3. Python的url基本函数

1. 对一个url进行访问请求, 且返回response对象

```python
url = "http://www.baidu.com"
response = liburl.request.urlopen(url)
```



1. 读取response对象的内容

**注意此时的data可能为bytes格式, 也可能为str格式, 这取决于访问的web服务器**

```python
data = response.read()

# str 和 bytes 格式之间的相互转化

# bytes => str
str = _bytes.decode('utf-8')

# str => bytes 
_bytes = str.encode('utf-8')
```

**经过读取之后便可以得到HTML的源代码** 



1. 对于get方式的请求, 如果传参为中文, 还需要进行转义之后再拼接

```python
url = "http://www.baidu.com/s?wd="
params = "蜘蛛"
# 拼接
url += params
# 转义
# safe=定义表示可以忽略的字符(即可以不用转义的)
# string.printable 便是所有可以打印的字符
# 如果不加 string.printable, 那么http://的 ‘:’ 也会被转义, 加了只有则只会处理中文字符
url = urllib.parse.quote(url, safe=string.printable)
```

































