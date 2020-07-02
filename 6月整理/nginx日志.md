#### nginx日志

- ```
   #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
      #  '$status $body_bytes_sent "$http_referer" '
      #  '"$http_user_agent" "$http_x_forwarded_for"';

      #access_log  logs/access.log  main;
  remote_addr  访问ip地址
  remote_user  访问的用户
  time_local  本地时间
  request  请求方式
  ```

  ​

```
 deny 192.168.241.1;
 deny 192.168.241.0/24;
 allow 192.168.241.0/24;
 
access_log logs/jingdong.log
```

#### 虚拟主机

- 基于ip地址

- 基于端口的

- 基于域名的

  ​

```
server {
        listen  80;
        server_name www.taobao.com;

        location / {
            root /data/taobao;
            index html/index.html;
        }
        }

server {
        listen       80;
        server_name  www.kwtop.com s22.com;

        #charset koi8-r;

        access_log  logs/kwtop.log  main;


        location / {
            root   /data/html;
            index  index.html index.htm;
        }

        location /img {
                alias /data/img;

        }
}
```

####  正向代理

#### 反向代理

- 动静分离   缓存静态文件
- 起到保存网站安全的作用
- 实现负载均衡  F5 A10 lvs haproxy nginx



#####weight

 

```
    upstream django{
        server 192.168.241.100:81 weight=3;
        server 192.168.241.101;

        }
	得到的结果 ：
访问100：81   3次
访问101  1次

```

#####ip_hash

- 对每个请求地址作哈希，这样每个固定的访客都会被固定到后端的机器上

  ```
  upstream django{
      ip_hash;
      server 192.168.241.100:81;
      server 192.168.241.101;
  }
  ```



##### backup

- 但前面的都访问不到，则请求backup的备份,只要有一个通，都不会走backup

  ```
  upstream django{
      server 192.168.241.100:82;
      server 192.168.241.100:81 backup;
  }
  ```

  ​

#### nginx location匹配规则

```
location = /{
    精确匹配/，后面不能带其他东西
}
location /{
    所有以/开头的地址
}
location /documents/{
    只匹配/documents/后面有东西的
}

location ^~ /images/ {
    匹配以/images/开头
    ~严格区分大小写
}
location ~* \.(gif|jpg\jpeg)$ {
	~*不区分大小写
    匹配以这些结尾的
}

优先级 
 = >  完整路径 > ^~ > /
```

