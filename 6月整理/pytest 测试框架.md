### pytest 测试框架

1.简单，易读

2.支持参数化







#### pytest和unittest框架对比

直接使用                                          测试类必须继承unittest.TestCase

参数使用自带装饰器                     参数化依赖第三方组件

插件丰富：支持失败重新执行     **不支持失败自动重新执行**

支持运行unittest编写的Case





unittest前置和后置

（1）通过setUp每个测试用例前执行，tearDown每个用例执行后

（2）通过setUpClass类里面所有用例执行前执行，tearDownClass类里面所有用例执行后执行



pytest前置和后置

（1）函数级别  ：setup/teardown	

- - 运行于测试**方法**的始末
  - 运行一次测试用例会运行一次setup和teardown

（2）类别级 setup_class/teardown_class

- - 运行于测试**类**的始末

  - 一个测试内只运行一次setup_class和teardown_class

    ​

###### 跳过测试

1.skip

- 标记skip表示跳过该测试用例，运行不执行
- skip(reason = None)
- @pytest.mark.skip

2.skipif

- 条件判断是否忽略不执行
- 判断条件表达式skipif(condition,reason=None)



##### pytest数据参数化

1.传入单个参数  pytest.mark.parametrize(argnames,argvalues)

argnames:参数名

argvalues:参数必须要可迭代类型的，一般为list

2.传入多个参数：@pytest.mark.parametrize(("username","password"),[("xiaoming","123456"),)("xiaohong","456789")])

list中每个元素都是一个元组，元组里的每一个元素和按照参数顺序一一对应





##### 失败重试

使用：

- 在配置文件中的命令行参数中添加 --reruns n
- 如果你期望加上出错重试的等待时间， --reruns-delay

