# wake_up
**基于DNN神经网络的简单语音唤醒**

关键词：**“hello，小瓜”**

## 运行要求：
1. 安装编译好htk工具并添加到环境变量。关于HTK的安装以及使用可以参考[
语音识别工具箱之HTK安装与使用](http://www.cnblogs.com/mingzhao810/archive/2012/08/03/2617674.html)

2. 安装好matlab2016b，并确保python可以调用它。

3. python3.5环境，安装好tensorflow。

## 流程：
1. 程序会录制四段音频，每段三秒，存在wav文件夹下。
2. HCopy函数会提取文件FBANK特征值，存在feature文件夹下。
3. 使用Python调用matlab模块（MATLAB中提供了供python调用的模块，这也是为什么要安装MATLAB的原因）读取.fbank文件并扩展，存在feature-translated文件夹下。
4. 最后网络从feature-translated文件夹下的文档中读取文件。

## 部分细节

- 在神经网络网络方面，选用的是两层的全连接神经网络，隐藏层的节点个数为128
- config.cfg和wav.scp为HTK提取特征时所需要的特征文件。关于HTK提的介绍可以观看[HTK官网](http://htk.eng.cam.ac.uk/)
- 文件名为2.\*的几个文件为tensorflow的文件，用于记录已经训练好的网络的权重、偏差、变量等信息。

## 不足之处
唤醒的延迟过长，主要是由于多次存取以及调用matlab，消耗的时间会有些长。
