### FLASK框架

- Flask 非常短小精悍  精简到只有一个session
- 第三方组件非常全 
- Flask  第三方组件  运行稳定性相对较差



### 羽绒服       半截袖

- Django适合大型  密集型
- Flask   适合小型  API 服务类项目




Flask WEB框架+HelloWorld

####  Flask Flask库文件

- Jinja2 模板渲染库
- MarkupSafe 返回安全标签  只要Flask  返回模板或者标签时都会依赖MarkupSafe
- Werkzeug  德文“工具” == uWSGI  底层是WSGI  FLASK项目启动都是基于Werkzeug

#### Flask 中 Response

- HTTPResponse('HelloWorld')   "HelloWorld"
- render("html文件")   rend_template("HTML文件")
  - 默认为templates
- redirect("/home")   redirect("/home")
  - 302  HTTP status code   请求重定向
  - 4XX  客户端错误
  - 5XX  服务器错误



####  Flask中的特殊返回值

- send_file("文件路径")  返回文件
  - 打开并返回文件内容  自动识别文件类型  在ResponseHeaders中加入
  - Content-Type：文件类型 是可以被客户端识别的文件类型
  - 不能识别的类型  下载处理 -- 浏览器会下载  .exe
  - x-ms  x二进制文件  ms微软    wma文件
-  jsonify("字符串或数据类型")      返回标准格式的json
  - Content-Type:application/json == 标准格式
  - Flask 1.1.1
  - return d 暂时不建议使用  兼容性
  - 直接返回dict时  本质上在执行jsonify(d)
  - API   接口  AJAX.post({username:123}){function(data){obj = data}}
- ​



#### Flask中的Request

- methods = ["GET","POST"]  在添加路由的装饰器中允许请求方式 ，覆盖

  - request.form  获取FormData中的数据to_dict()  

  - request.method 获取请求方式

  - request.args 获取URL中的数据，字符串  get("keys")

  - ```
    #获取一个FileStorage  Flask文件特殊对象
    my_file = request.files.get("my_file")
    new_file = os.path.join("xht",my_file.filename)
    my_file.save(new_file)
    ```



#### Flask 中的session

- Session 服务器端的键值对

- Cookie客户端的键值对

- 交由客户端保管机制

  - 1.开启Session[username] =123


  - 2.序列化字典 == 字符串
  - 3.加密字符串 SecretKey 密钥字符串

- ​

- 接受反序列化Session

  - 1.从Cookie中获取一个交session Key的zhi
  - 2.通过SecretKey解密为session
  - 3,反序列化成字典

  ​

#### Jinja2

- {{ }}引用变量数据  执行函数
- {%%}