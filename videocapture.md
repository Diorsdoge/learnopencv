### VideoCapture类

用于从视频文件或摄像机捕获视频.该类提供了用于从摄像机捕获视频或者读取视频文件的C++ API。

> 注意：在C API中使用黑和结构CvCapture来代替VideoCapture。

#### 构造函数

VideoCapture::VideoCapture()       
VideoCapture::VideoCapture(const string& filename)//filename – 文件名       
VideoCapture::VideoCapture(int device)//device – 捕获视频的编号. 如果只有一个设备，默认编号为0       

#### open函数 - 打开视频文件或捕获设备进行视频捕获

bool VideoCapture::open(const string& filename)//filename – 文件名      
bool VideoCapture::open(int device)//device – 捕获视频的编号. 如果只有一个设备，默认编号为0

#### isopened函数 - 如果视频捕获已经初始化，则返回true。

bool VideoCapture::isOpened()

#### release函数 - 关闭视频文件或捕获设备

void VideoCapture::release()

#### grap函数 - 从视频文件或捕获设备中捕获下一帧

bool VideoCapture::grab()

#### retrieve函数 - 解码并返回抓取的视频帧

bool VideoCapture::retrieve(Mat& image, int channel=0)

#### read函数 - 抓取，解码并返回下一个视频帧

bool VideoCapture::read(Mat& image)

#### get函数 - 返回指定的VideoCapture属性

double VideoCapture::get(int propId)//propId - 属性标识符

CV_CAP_PROP_POS_MSEC - 视频文件的当前位置（以毫秒为单位）或视频捕获时间戳。
CV_CAP_PROP_POS_FRAMES - 下一个要解码/捕获的帧的基于0的索引。
CV_CAP_PROP_POS_AVI_RATIO - 视频文件的相对位置：0 - 电影的开始，1 - 电影的结束。
CV_CAP_PROP_FRAME_WIDTH - 视频流中帧的宽度。
CV_CAP_PROP_FRAME_HEIGHT - 视频流中帧的高度。
CV_CAP_PROP_FPS - 帧速率。
CV_CAP_PROP_FOURCC - 编解码器的4个字符代码。
CV_CAP_PROP_FRAME_COUNT - 视频文件中的帧数。
CV_CAP_PROP_FORMAT -  retrieve()返回的Mat对象的格式。
CV_CAP_PROP_MODE - 指示当前捕获模式的后端特定值。
CV_CAP_PROP_BRIGHTNESS - 图像的亮度（仅适用于相机）。
CV_CAP_PROP_CONTRAST - 图像的对比度（仅适用于相机）。
CV_CAP_PROP_SATURATION - 图像的饱和度（仅适用于相机）。
CV_CAP_PROP_HUE - 图像的色调（仅适用于摄像机）。
CV_CAP_PROP_GAIN - 图像的增益（仅适用于摄像机）。
CV_CAP_PROP_EXPOSURE - 曝光（仅适用于相机）。
CV_CAP_PROP_CONVERT_RGB - 指示图像是否应转换为RGB的布尔标志。
CV_CAP_PROP_WHITE_BALANCE - 目前不支持
CV_CAP_PROP_RECTIFICATION - 立体相机的校正标志（注意：目前仅由DC1394 v 2.x后端支持）

#### set函数 - 设置VideoCapture中的属性。

bool VideoCapture::set(int propertyId, double value)//propId - 属性标识符，同get；value - 属性的值。
