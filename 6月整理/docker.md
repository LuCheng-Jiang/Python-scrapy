#### 镜像

可以理解为操作系统的os镜像

#### 容器

启动后的镜像

#### 仓库

#### 镜像

私有的仓库
公共的仓库
docer-ce  社区版本
docker-ee 商业版本

#### 底层实现原理

namespace
cgroup

#### 安装

- 启动容器的过程
- docker run 镜像名称
- 先查找本地是否存在镜像
- 如果不存在则下载镜像
- 下载以后在启动
- 容器启动后在原来的镜像的基础上加一层
- 配置加速器

docker 镜像分层的

显示镜像的id

######  删除全部镜像 docker rmi "docker images -q"

#### docker run -ti centos /bin/bash

-t 创建一个虚拟终端
-i  将容器的标准输入保持打开
--name   指定名字
-d 后台运行
-P  将容器的端口暴露在宿主机的端口上
-p  宿主机端口号:容器端口号
-v 宿主机目录：容器目录
退出 exitr

#### 导出镜像

docker save -o mycentos.tar.gz mycentos
docker save mycentos > mycentos.tar.gz

#### docker rm  去除镜像  -f  强制删除容器

docker load -i mycentos.tar.gz
docker load < mycentos.tar.gz

#### 查看端口映射

docker port  容器id或者容器名称


docker stop  容器id或者容器名称

docker status  容器id或者容器名称



#### 进入容器

docker exec -ti 容器id和名称 

