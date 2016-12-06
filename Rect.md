### Rect类

Rect类中，成员变量x、y、width、height，分别为左上角点坐标和矩形的宽和高。

- area()函数 - 返回rect的面积
- size()函数 - 返回rect的尺寸
- tl()函数 - 返回左上顶点坐标
- br()函数 - 返回右下顶点坐标
- width()函数 - 返回宽度
- height()函数 - 返回高度
- contain(Point(x,y))函数 - 返回点(x,y)是否在rect内
- 两个矩形交集：Rect rect = rect1 & rect2
- 两个矩形并集：Rect rect = rect1 | rect2
- 平移：Rect rect = rect + Point(x,y) //对左上顶点坐标进行操作
- 缩放：Rect rect = rect + Size(width, height) //对宽高进行操作
