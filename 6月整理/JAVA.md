## JAVA

#### 数据类型

- 整数型  byte,short,int,long
- 浮点型 float,double
- 字符型 
- 布尔型

#### 默认无参

#### 重载的条件

- 方法名必须相同
- 参数列表必须不同
- 方法的返回类型可以相同也可以不同
- 仅仅返回类型不同不足以成为方法的重载
- 重载是发生在编译时的，因为编译器根据参数的类型选择哪一种方法

#### 方法的重写

- 方法的重写与重载虽然名字相似，但却是完全不一样，重写发生在父类和子类之间
- @Override
- 重写的方法必须和父类保存一致

#### 初始化

- 类的初始化
- 成员的初始化
- 初始化顺序
  - 静态属性：static开头定义的属性
  - 静态方法快：static{}包起来的代码块
  - 普通属性
  - 普通方法快
  - 构造方法
  - 方法
- 数组的初始化  int[] a1; int a1[]; int array[4]={1,2,3,4}

#### 可变参数列表

- int... numbers

#### 对象的销毁

- 在 Java 中，我们不再需要手动管理对象的销毁，它是由 `Java 虚拟机`进行管理和销毁的。虽然我们不需要手动管理对象，但是你需要知道 `对象作用域` 这个概念。

#### this和super都是Java中的关键字

- this和构造函数一起使用，充当一个全局关键字的效果

  ```
  public class Apple {

      private int num;
      private String color;

      public Apple(int num){
          this(num,"红色");
      }

      public Apple(String color){
          this(1,color);
      }

      public Apple(int num, String color) {
          this.num = num;
          this.color = color;
      }

  }
  ```

  ​

- this必须放在构造函数第一行，否则编译不通过

- this可以理解为指向自身的引用，那么Super就是指向父类的一个引用

- super和this一样放在构造函数第一行，其他位置随意

- 可以使用super.对象来引用父类的成员

#### 访问控制权限（封装）

- 只对需要的类可见就行了
- JAVA中成员的访问控制权限一共为四种，分别为public,protected,default,private
- 同一类，同一包中的类，子类，其他包中的类

#### 继承（extends）

- 我们创建一个类就隐式继承自Object父类，只不过是没有指定
- 子类会调用父类的方法，重写

#### 多态

- 多态指同一行为具有不同的表现形式，封装和继承是多态的基础
- 如何实现多台
  - 继承
  - 重写父类的方法
  - 父类引用指向子类的对象（Father father = new Son(); father.eat()）

#### 组合

- 就是将对象引用置于新类中即可（private Soccer soccer;##通过引用Soccer类，来达到调用Soccer中的属性方法）
- 组合和继承的区别 ：组合双方是松耦合，继承是紧耦合，组合是运行时绑定，继承是编译期绑定

#### 代理（。。。难）

- 代理的大致描述是，A 想要调用 B 类的方法，A 不直接调用，A 会在自己的类中创建一个 B 对象的代理，再由代理调用 B 的方法。例如如下代码



### 向上转型

- 向上转型：通过子类转化为父类的对象，这种事自动完成的
- 向下转型：通过父类对象实例化子类的对象，这种不是自动完成的，需要强制指定

##### static

- static修饰的方法为静态方法，能够直接调用类型.方法名，static修饰的变量为静态成员变量，也成为类变量
- 除了修饰属性和方法外，还有静态代码块的功能，可用于类的初始化操作
  - 由于静态代码块是随着类的加载而执行，因此，很多时候会将只需要进行一次初始化的操作放在static代码块进行

##### final

- 修饰的类不能被继承，修饰的方法不能被子类重写
- 修饰变量分为两种情况，修饰的是基本数据类型的话，表示该数据类型的值不能被修改，修饰的是引用数据类型，表示对其初始化之后便不能再让其指向另一个对象

#### 接口和抽象类

- ```
  public interface GoodJob{
      void writeWell();
  }
  ```

  ​

- ```
  class Coding implements GoodJob{
      @Override
      public void writeWell(){
          System.out.println("Mewnenn is java");
      }
  }
  ```

- 接口不能被实例化，接口是一个完全抽象的类，如果在接口中定义构造方法会出错

- 接口的实现必须实现接口里面的全部方法，否则必须定义为抽象类

#### 抽象类

- ```
  public interface Dog {

      void FurColor();

  }

  abstract class WhiteDog implements Dog{

      public void FurColor(){
          System.out.println("Fur is white");
      }

      abstract void SmallBody();
  }
  ```

- 如果类中有抽象方法，那么这个类一定是抽象类，也就是说用abstract修饰的方法一定是抽象方法

- 抽象类不一定只有抽象方法，抽象中也可以具体的方法，可以自己考虑是否实现这些方法

- 抽象类和接口一样不能被实例化，但是可以在接口中有构造方法

#### 异常

- Java程序一般会出现两种两种问题，Java.lang.Exception,一种是java.lang.Error

- Exception位于java.lang包下，继承于Throwable类

- #####Throwable是exceptions和errors的父类，只有继承于Throwable的类或者子类才能够被抛出，还有就是Java中的@throw也可以抛出

- Throgwable也有父类Object,因此常用的方法还有继承父类的getClass()和

getName()

#### 与Exception有关的Java关键字

- ##### throws,throw,try,finally,catch

- ```
  static void cacheException() throws Exception{

    throw new Exception();

  }
  ```

  ​

- throw 语句用在方法体内，表示抛出异常，由方法体内的语句处理。 throws 语句用在方法声明后面，表示再抛出异常，由该方法的调用者来处理。

- #####try....catch....finally

#### 内部类

- ```
  public class OuterClass {
      private String name ;
      private int age;

      class InnerClass{
          public InnerClass(){
              name = "wen";
              age = 21;
          }
      }
  }
  ```

#### 集合

![](C:\Users\W\Pictures\Camera Roll\aHR0cHM6Ly9zMS5heDF4LmNvbS8yMDIwLzA1LzA4L1lLMEFFUS5wbmc.jpg)

#### 首先介绍iterator

- 实现此接口允许对象成为for-each循环的目标，也就是增强for循环

  ```
  List<Object> list = new ArrayList();
  for(Object obj:list){}
  ```

  ```
  Object[] list = new Object[]
  for(Object obj:list){}
  ```

- jdk1.8之前Iterator只有iterator一个方法

```
for(Iterator it = coll.iterator(); it.hasNext(); ){
    System.out.println(it.next());
}
```

#### 顶层接口

- Collection就是一个顶层接口，它主要用来定义集合的约定
- List接口也是一个顶层接口，它继承于Collection接口，同时也是ArrayList,LinkedList等集合元素的父类
- Set接口位于List接口同级的层次上，它同时也继承了Collection接口。Set接口提供了额外的归档，他对add、equal、hashCode方法提供了额外的标准
- Queue是和List，Set接口并列的Collection的三大接口之一。Queue的设计用来处理之前保持元素的访问次序，除了Collection基础操作之外，队列还提供了额外的插入，读取，检查操作。
- SortedSet接口直接继承于Set接口，使用Comparable对元素进行自然排序或者使用Comparator在创建时对元素提供定制的规则，set的迭代器将按升序顺序遍历集合
- Map是一个支持Key-value存储的对象，Map不能包含重复的key，每个键最多映射一个值，这个接口代替了Dictionary类，Dictionary是一个抽象类而不是一个接口

#### ArrayList

- ArrayList是实现了List接口的可扩容性数组，他的内部是基于数组实现的，它的具体定义为

  ```
  public class ArrayList<E> extends AbstractList<E> implements List<E> ,RandomAccess,Cloneable,java.io.Serialize{...}
  ```

  ​

- ArrayList可以实现所有可选择的列表操作，允许所有的元素，包括空值，ArrayList还提供了内部存储list的方法。它能够完全代替Vector，只有有一点例外，**ArrayList不是线程安全的容器**

- ArrayList不是线程安全的容器，如果多个线程至少有两个修改了ArrayList的结构的话就会导致线程安全问题，作为替代条件可以使用线程安全的List,应该使用Collections.synchronizedList.

  ```
  List list = Collections.synchronizedList(new ArrayList(...))
  ```

#### Vector

- Vector同ArrayList一样，都是基于数组实现的，只不过Vector是一个线程安全的容器，他对于内部的每个方法都是简单粗暴的上锁，避免多线程引起的安全性问题，都是通常这种同步的方式开销比较大，因此，访问元素的效率远远低于ArrayList

#### LinkedList类

LinkedList是一个双向链表，允许存储任何元素（包括null），它的主要特性：

- LinkedList所有的操作都是可以表现为双向的，索引到链表的操纵将遍历从头到尾

- 注意这个实现也不是线程安全的，如果多个线程访问链表，并且至少期中的一个线程修改了链表的结构，那么链表必须进行外部加锁，或者使用

  ```
  List  list = Collections.synchronizedList(new LinkedList(..))
  ```

  ​

#### Stack

堆栈是后入先出的容器，它继承于Vector类，提供了通常的push和pop操作，以及peek和empty方法

- 但是有一个更加完善的后进先出栈由Deque接口和它的实现提供，应该优先使用

  ```
  Deque<Integer> stack = new ArrayDequeue<Integer>()
  ```



#### HashSet

- HashSet是Set接口的实现类，HashSet实际上是HashMap的实例，他不能保证集合的迭代顺序，这个类允许null元素
  - 这个类的实现不是线程安全的。如果多线程并发访问HashSet,并且至少一个线程修改了Set,必须进行外部加锁，或者使用Collections.synchronizedSet()方法重写

#### TreeSet

- TreeSet是基于TreeMap的实现，这些元素使用他们的自然排序或者在创建时提供comparator进行排序，具体取决于使用的构造函数

  - add,remove和contains方法

  - 不是线程安全，如果至少一个修改必须外部加锁

    ```
    sortedSet s = Collections.synchronizedSortedSet(new TreeSet())
    ```

    ​

#### LinkedHashSet类

LinkHashSet继承于Set，是Set接口的Hash表和LinkedList的实现，同时他也 不是线程安全的



##### PriorityQueue

PriorityQueue是AbstractQueue的实现类，优先级队列的元素根据自然排序或者通过在构造函数的Comparator来排序，PriorityQueue不允许null元素



#### HashMap

HashMap 是一个利用哈希表原理来存储元素的集合，并且允许空的 key-value 键值对。HashMap 是非线程安全的，也就是说在多线程的环境下，可能会存在问题，而 Hashtable 是线程安全的容器。HashMap 也支持 fail-fast 机制。HashMap 的实例有两个参数影响其性能：初始容量 和加载因子。可以使用 `Collections.synchronizedMap(new HashMap(...))` 来构造一个线程安全的 HashMap。



#### TreeMap

一个基于 NavigableMap 实现的红黑树。这个 map 根据 key 自然排序存储，或者通过 Comparator 进行定制排序。

- TreeMap 为 containsKey,get,put 和 remove 方法提供了 log(n) 的时间开销。
- 注意这个实现不是线程安全的。如果多线程并发访问 TreeMap，并且至少一个线程修改了 map，必须进行外部加锁。这通常通过在自然封装集合的某个对象上进行同步来实现，或者使用 `SortedMap m = Collections.synchronizedSortedMap(new TreeMap(...))`。
- 这个实现持有 fail-fast 机制。

#### LinkedHashMap类

LinkedHashMap 是 Map 接口的哈希表和链表的实现。这个实现与 HashMap 不同之处在于它维护了一个贯穿其所有条目的双向链表。这个链表定义了遍历顺序，通常是插入 map 中的顺序。

- 这个类提供了所有可选择的 map 操作，并且允许 null 元素。由于维护链表的额外开销，性能可能会低于 HashMap，有一条除外：遍历 LinkedHashMap 中的 collection-views 需要与 map.size 成正比，无论其容量如何。HashMap 的迭代看起来开销更大，因为还要求时间与其容量成正比。
- LinkedHashMap 有两个因素影响了它的构成：初始容量和加载因子。
- 注意这个实现不是线程安全的。如果多线程并发访问 LinkedHashMap，并且至少一个线程修改了 map，必须进行外部加锁。这通常通过在自然封装集合的某个对象上进行同步来实现 `Map m = Collections.synchronizedMap(new LinkedHashMap(...))`。

#### Hashtable类

Hashtable 类实现了一个哈希表，能够将键映射到值。任何非空对象都可以用作键或值。

- 与新的集合实现不同，Hashtable 是线程安全的。如果不需要线程安全的容器，推荐使用 HashMap，如果需要多线程高并发，推荐使用 `ConcurrentHashMap`。



## Collections类

Collections是一个包装类，它的作用就是为了集合框架提供某些功能的实现，此类只包括静态方法操作或者返回collections

#### 同步包装

同步包装器将自动同步（线程安全性）添加到任意集合，六个核心集合接口（Collection,Set,List,Map,SortedSet和SortedMap）中的每一个都有静态工厂方法

```
public static  Collection synchronizedCollection(Collection c);
public static  Set synchronizedSet(Set s);
public static  List synchronizedList(List list);
public static <K,V> Map<K,V> synchronizedMap(Map<K,V> m);
public static  SortedSet synchronizedSortedSet(SortedSet s);
public static <K,V> SortedMap<K,V> synchronizedSortedMap(SortedMap<K,V> m);
```



## 泛型

没有泛型

```
List arrayList = new ArrayList();
arrayList.add("wen");
arrayList.add(100);

for(int i = 0; i< arrayList.size();i++){
    String item = (String)arrayList.get(i);
        System.out.println("test === ", item);
}
####发生错误，integer不能转为String类型
```

List<T> arraylist = new ArrayList<>()

#### 用泛型表示类

```
//此处 T 可以随便写为任意标识，常见的如 T、E、K、V 等形式的参数常用于表示泛型
public class GenericDemo<T>{ 
    //value 这个成员变量的类型为 T,T 的类型由外部指定  
    private T value;

    public GenericDemo(T value) {
        this.value = value;
    }

    public T getValue(){ //泛型方法 getKey 的返回值类型为 T，T 的类型由外部指定
        return value;
    }

     public void setValue(T value){
          this.value = value
    }
}
```



####用泛型表示接口

```
//定义一个泛型接口
public interface Generator<T> {
    public T next();
}
```

#### 泛型表示方法

```
public class GenericMethods {
  public <T> void f(T x){
    System.out.println(x.getClass().getName());
  }
}
```

#### 泛型通配符

```
public static void main(String[] args){
    List<String> name = new ArrayList<String>();
     List<Integer> age = new ArrayList<Integer>();
    List<Number> number = new ArrayList<Number>();
    name.add("wen");
    age.add(18);
    number.add(314);
    generic(name);
    generic(age);
    generic(number);
}
public static void generic(List<?> data) {
    System.out.println("Test wen :" + data.get(0));
}
```

**上界通配符** : <? extends ClassType> 该通配符为 ClassType 的所有子类型。它表示的是任何类型都是 ClassType 类型的子类。

**下界通配符**： <? super ClassType> 该通配符为 ClassType 的所有超类型。它表示的是任何类型的父类都是 ClassType。



## 反射

**Java反射机制是在程序运行过程中，对于任何一个类，都能够知道它的所有属性和方法，对于任意一个对象，都能够知道调用它的任意属性和方法，这种动态获取信息以及动态调用对象方法的功能成为Java的反射机制**

Java 反射机制主要提供了以下这几个功能

- 在运行时判断任意一个对象所属的类
- 在运行时构造任意一个类的对象
- 在运行时判断任意一个类所有的成员变量和方法
- 在运行时调用任意一个对象的方法

```
Class student = null
try{
    student = Class.forName("包名称);
}catch(Exception e){
    e.printStackTrace();
}
#获取所有公有属性
Field[] fields = student.getFields();   #获取所有的但是不包括继承的getDeclaredFields()


#获取公有方法
Method[] methods = student.getMethods();  #获取所有的方法不包括继承的getDeclaredMethod()

#获取构造方法
Constructor[] constructors = student.getConstructed() #getDeclaredConstructor


###创建实例
Class c = Class.forName("包名")
Student stu1 = (Student)c.newInstance();

#第一种方法，实例化默认构造方法
stu1.setAddress("河北石家庄");
 System.out.println(stu1);

// 第二种方法 取得全部的构造函数 使用构造函数赋值
Constructor<Student> constructor = c.getConstructor(String.class, 
                                                            int.class, String.class, String.class);
        Student student2 = (Student) constructor.newInstance("wen", 24, "ii班", "zao庄");
        System.out.println(student2);


    /**
        * 获取方法并执行方法
        */
        Method show = c.getMethod("showInfo");//获取 showInfo()方法
        Object object = show.invoke(stu2);//调用 showInfo()方法

    
```

## Class类

- toString () 
  - public String toString(){...}
- getName()  
  - 如果是引用类型，String.class.getName() -- >java.lang.string
  - 如果是基本数据类型  byte.class.getName() -- > byte
  - 如果是数组类型  java.lang.Object
- toGenericString()
  - 这个方法会返回类的全限定名称，包括**类的修饰符和参数信息**
- forName()
  - 根据类名获得一个Clas对象引用，这个方法会使类对象进行初始化
  - Class t  = Class.forName("java.lang.Thread")
  - 在JAVA中一共有三种获取实例的方法
    - Class.forName("java.lang.Thread")
    - Thread.class
    - thread.getClass()
- newInstance()
  - 初始化一个类的实例
- getClassLoader()
  - 获取类加载对象
- getMethods()
- getConstructors()
- getFields()
- 等等

#### ClassLoader类

反射中，还有一个非常重要的类就是 ClassLoader 类，类装载器是用来把`类(class)` 装载进 `JVM`的。ClassLoader 使用的是双亲委托模型来搜索加载类的，这个模型也就是双亲委派模型

#### enum

```
public enum Family {

    FATHER,
    MOTHER,
    SON,
    Daughter;

}

public class EnumUse {

    public static void main(String[] args) {
        Family s = Family.FATHER;
    }
}
```

## I/O

创建一个良好的I/O程序是复杂的，jdk开发人员编写了大量的类只为了能够创建一个良好的包

#### File类

File类是对文件系统中文件以及文件夹进行操作的类，可以通过面向对象的思想操作文件和文件夹

文件创建操作如下，主要涉及**文件创建、删除文件、获取文件描述符**

```
class FileDemo{
   public static void main(String[] args) {
       File file = new File("D:\\file.txt");
       try{
         f.createNewFile(); // 创建一个文件

         // File 类的两个常量
         //路径分隔符(与系统有关的）<windows 里面是 ; linux 里面是 ： >
        System.out.println(File.pathSeparator);  //   ;
        //与系统有关的路径名称分隔符<windows 里面是 \ linux 里面是/ >
        System.out.println(File.separator);      //  \

         // 删除文件
         /*
         File file = new File(fileName);
         if(f.exists()){
             f.delete();
         }else{
             System.out.println("文件不存在");
         }   
         */


       }catch (Exception e) {
           e.printStackTrace();
       }
    }
}
```

#### 基础 IO 类和相关方法

最基本的抽象类**InputStream、OutputStream、Reader、Writer**,最基本的方法就是read()和writer(）方法，其他刘都是上面四类流的子类，方法也是通过这两类方法衍生而成的



#### InputStream

InputStream 是一个定义了 Java 流式字节输入模式的抽象类。该类的所有方法在出错条件下引发一个 IOException 异常。它的主要方法定义如下

- public int available()
- public int read(byte b[],int off,int len)
  - 把第off位置读取len长度字节的数据放到byte数组中
- public abstract int read()
- public void close()

#### OutputStream

OutputStream 是定义了流式字节输出模式的抽象类。该类的所有方法返回一个 void 值并且在出错情况下引发一个 IOException 异常。它的主要方法定义如下

- void write(int b)
- void write(byte buffer[])  向输出流写入一个完整的字节数组
- void write(byte buffer[],int offset,int numBytes)
- void flush()   刷新缓冲区
- void close()   关闭输出流

##### Reader类

Reader 是 Java 定义的流式字符输入模式的抽象类。类中的方法在出错时引发 `IOException` 异常。

- int read()
- int read(buffer[])
- abstract int read(char buffer[],int offset,int numChars)
- boolean ready()

#### Writer类

Writer 是定义流式字符输出的抽象类。 所有该类的方法都返回一个 void 值并在出错条件下引发 IOException 异常

- void write(char buffer[])
- abstract void close()





四大类最常用的子类

- FileInputStream
- FileOutputStream
- FileReader
- FileWriter



## 注解

Java注解又称为元数据，它为代码中添加信息提供了 一种形式化的方法，公有7个，3个在java.lang中，剩下的4个在java.lang.annotation中

- 作用在代码中的注解有哦那个有三个，他们分别是
  - @Override：重写标记，一般用子类继承父类，标注在重写过后的子类方法上，如果发现其父类，或者是引用的接口中并没有该方法，会发成编译错误。
  - @Deprecated:用此注解注释代码已经过时，不再推荐使用
  - @SupressWarning:这个注解起到忽略编译器警告作用
- 元注解有四个，元注解就是来标志注解的注释，他们分别是
  - @Retention:标识如何存储，是只在代码中，当Java文件编译成class文件的时候，注解被遗弃
    - RetentionPolicy.SOURCE：注解只保留在源文件，当 Java 文件编译成 class 文件的时候，注解被遗弃；
    - RetentionPolicy.CLASS：注解被保留到 class 文件，但 jvm 加载 class 文件时候被遗弃，这是`默认的`生命周期；
    - RetentionPolicy.RUNTIME：注解不仅被保存到 class 文件中，jvm 加载 class 文件之后，仍然存在；
  - @Documented:标记这些注解是否包含在JavaDoc中
  - @Target:标记这个注解说明了Annotation所修饰的对象范围，Annotation可被用来package,types,类型成员，方法参数和本地变量
  - @Inherited:标记这个注解是继承于哪个注解类的
- 从jdk1.7之后，又添加了三个额外的注解，他们分别是
  - @SafeVarargs:在声明可变参数或方法时，Java编译器会报unchecked警告，使用@safeVarargs可以忽略这些警告
  - @FunctionalInterface:表明这个方法是一个函数世接口
  - @Repeatable:标识某注解可以在同一声明上使用多次