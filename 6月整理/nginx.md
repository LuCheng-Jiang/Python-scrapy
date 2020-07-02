## nginx

- web服务  Apache  iis
- django web框架
- lvs  负载均衡   章文嵩博士
- vue  尤雨溪
- tengine   淘宝开源的 基于nginx，针对大访问量的情况下使用





yum install -y gcc   C compiler  编译C环境


yum install gcc zlib2-devel pcre-devel openssl-devel

make&& make install



#### 目录结构

- nginx 
- conf html logs sbin
- conf 配置文件
- html   存静态文件   index.html  默认的欢应界面
- logs 日志目录
- sbin   二进制文件
- 启动之后生成一个主进程，根据配置文件的选项来生成子进程（工作进程）



##### ss -tnlp   查看端口


location /img {
	root /data/im;
}

location /data/img  里必须有/img

location /img {
	alias /data/img;
}

alias /data/img 里不需要有/img

server_name  www.kwtop.com s22.com;



