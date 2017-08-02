# wake_up
基于神经网络的简单语音唤醒

关键词：“hello，小瓜”

# 运行要求：
1.安装编译好htk工具并添加到环境变量；
2.安装好matlab2016b，并确保python可以调用它；
3.python3.5环境，安装好tensorflow；

# 流程：
首先程序会录制四段音频，每段三秒，存在wav文件夹下。然后HCopy函数会提取文件FBANK特征值，存在wake-up-word文件夹下。之后调用matlab函数读取.fbank文件并扩展，存在txt文件夹下。最后网络从txt文件夹下的文档中读取文件。由于多次存取以及调用matlab，消耗的时间会有些长。
