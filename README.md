# mastodon_bot

长毛象机器人

# 为了跑这些代码，你需要

1. nodejs[14.16.1]（library文件里包含了）

2. python[3.7.4]（以下是需要的library）

   ----- requests

   ----- bs4

   ----- sqlalchemy

3. 服务器跑额外需要pm2

# 边学边做的保姆级教学

https://www.youtube.com/watch?v=sKSxBd56H70

我没有node基础，全程是看这个教程做的，讲得很细致（对于做一个bot足够用）

# 用法

1. 在自己电脑跑：打开一个terminal，输入【node bot.js】启动即可。关机会停止工作

2. 在服务器：ssh到服务器，输入【pm2 bot.js】启动即可

# 如果你不太熟悉代码且真的想跑这个机器人的教程

（以下所有步骤针对干净如纸纯洁善良未历世事的windows，如果你35块买了个xx云服务器，就按自己服务器系统搜一下各种安装的对应命令，比如搜“linux安装python”（相信会买服务器的同学也不用看这段教程）直接在终端输入各种命令下载.tar.gz 安装包解压安装）

### 1. 安装python

https://www.bilibili.com/read/cv13671309

### 2. 安装node

https://blog.csdn.net/qq_45752401/article/details/122299475

### 3. 检查装没装好

打开一个cmd（win+r,cmd,回车）输入

python --version 回车

node --version 回车

分别回复给你相应版本号就行了（版本比上边写的高就行了，低一点应该也问题不大？）

### 4. 安装 python library。在命令行里输入

pip install requests 回车

pip install bs4 回车

pip install sqlalchemy 回车

### 4. 下载 github 提供的该项目打包文件

解压，打开解压的文件（此时你看到了乱七八糟一堆后缀.py和.json和.js之类的文件），复制目录

比如说 user/me/desktop/mastodon_bot（是个意思，在下面粘你复制好的你的目录不要粘我的）。在cmd里输入

cd user/me/desktop/mastodon_bot 回车，然后把这个窗口放一边备用

### 5. 获取你的长毛象应用接口（高级说法API）

长毛象主页左下角那一堆平时没人看的东西里有一个“开发”，选创建应用，起个名，权限按她默认的勾选不用动即可，之后会得到三个乱码。把三个乱码填进

.env-example

这个文件，把乱码粘到等于号后边

应用ID 对应 CLIENT_KEY

应用密钥 对应 CLIENT_SECRET

你的访问令牌 对应 ACCESS_TOKEN 【这个必须贴对，上边这俩我一开始好像贴反了，不影响用】

API_URL=https://bgme.me/api/v1/ 这里操操在bgme，如果你在别的站点就把bgme.me换成你的站点

然后把这个文件重命名，去掉-example，变成

.env

### 6. 拿出刚才准备好的，cd到指定目录的窗口，输入

node bot.js 回车

发现屏幕上出现一行Mastodon Bot starting...就可以了！

我在尝试的过程中发现启动后第一次通知往往收不到（可能是我连接的问题？）多艾特一次就好了

如果没有这行字而是报错了！！可以在这里找我！ -> miantiao07@bgme.me（虽然我也不一定能解决你的问题！）
