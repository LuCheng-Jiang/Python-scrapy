## MongoDB

Mongodb数据类型

ObjectID

String:字符串  ，必须是utf-8

Boolean:布尔值,true或者false

Integer:整数

Double:浮点数

Arrays:数组或者列表

Object:就是Python中的字典

Null:None  Null

Timestamp:时间戳

Date:存储当前时间或者unix时间格式

## 增加

db.tablename.insert({})

db.user.insert({name:"沙悟净",age:66,hobby:[1,2,3,4,5]})

db.user.insert({},{})

官方推荐写法

**db.user.insertOne({})**

**db.user.insertMany([{},{}])**

### 查询

db.user.find({name:"孙悟空"})

db.user.findOne({})  #查询符合条件的第一条

db.user.find({age:{$gte:70}} )   #lt  小于  eq等于    ne  不等于



### 修改

db.tablename.update()

##### 所有MongoDb的修改全部基于修改器 

db.user.update({age:66.66},{$set:{age:66}})   #如果该字段不存在则创建该字段并且赋值



**官方推荐**

db.user.updateOne({},{})  #修改符合条件的第一条数据

db.user.updateMany({},{})  #

#### 删除

db.user.update({name:三悟空}，{$unset":{age18:1}})



db.user.update({name:孙悟空},{$inc:{age:1}})    #先引用原有数据，在原有数据的基础上增加



**官方推荐的写法**

db.user.deleteOne({})

db.user.deleteMany({})

#### 针对Array List操作

$push == append

db.user.update({name:'孙大圣'}，{$push:{hobby:"8"}})

$pushAll == extends   {$pushAll:{hobby:[12,232]}}

删除符合条件的数据

$pull == remove

$pullAll = 删除列表

$pop  删除数据  {$pop:{hobby:-1}}  #删除第一个

