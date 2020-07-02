Dev和Ops冲突

development  与  operations

功能性需求 非功能性需求

共同协作   开发  运维 测试  

#### 提高产品质量

1.自动化测试

2.持续集成

3.代码质量管理大师

4.程序员鼓励师

**DevOps如何实现**

既然这么好，为什么有些公司没有?

设计架构规则 - 代码的存储- 构建-测试-预生产-部署-监控

**Git版本控制系统**

vcs(version control system)

版本控制系统是一种记录一个若干文件内容的变化，以便将来查阅版本内容情况系统



**SVN集中式版本控制软件，只有一个中央数据仓库，如果中央数据仓库挂了或者不可以访问，所有使用者无法使用svn，无法提交或者备份文件**

**分布式的版本控制系统，再每一个使用者电脑上就有一个完整的数据仓库，没有网络也可以使用git，当然为了团队协作，会将本地数据同步到git服务器或者github仓库** 



### Git基本操作

- git  init  初始化仓库  把一个目录初始化为版本仓库（可以是空目录  也是可以带内容的目录）
- git status  查看当前仓库的状态
- git add file 提交文件到暂存区
- git add. 或者git add *  提交当前所有的文件到暂存区
- git rm --cached <file>  撤出暂存区  
- git rm -f  <file> 同时从暂存区 同工作区一同删除文件
- git commit -m "message"  从缓存区提交到本地代码仓库

**小结**：如何真正意义上通过版本控制系统  管理文件

1.工作目录必须有个代码仓库

2.通过 git  add file  提交到暂存区

3.通过git commit  提交到本地仓库

- git mv old-filename new-filename  直接更改文件名称 更改完直接commit提交即可
- git diff  默认比对工作目录和暂存区有什么不同
- git diff --cached 比对暂存区和本地仓库
- 如果某个文件已经被仓库管理，如果再更改此文件，直接需要一条命令提交即可
  - git  commit -am "add newfile"
- git log 查看历史提交过的信息
  - -p  查看具体的改动
  - -l  查看最近一次
  - git log --oneline --decorate    查看当前指针的指向
- git reset --head  **  
  - git  reflog  查看所有的执行的版本
- git branch testing 创建一个测试分支
- git checkout testing 切换到一个测试分支
- git checkout -b testing  创建并切换分支

git tag  打标签

- git tag -a v1.0 -m "aaa bbb master testing version 1.0" -a 指定标签名字 -m 指定说明文字

- git show  v1.0 查看标签

- git tag -d v1.0  删除标签

- ```
  git remote add origin git@github.com:LuCheng-Jiang/git_data.git   添加远程仓库  名称为origin

  生产免密钥
  ssh-keygen -t rsa
  cat .ssh/id_rsa.pub
  ```

  ​