# mastodon_bot 长毛象机器人

# English Summary:

CaoCao (Fuck*2 in Chinese) is an autoresponder bot project for mastodon. The functions are: accept sentences from users to write a sonnet solitaire, drift bottle, find a random work in ao3, find a random poem online, accept two character names to return a random story, etc. 

All the texts involved are Chinese. If you are a newbie like me and working on build your own bot, I (strongly) recommend <a href="https://www.youtube.com/watch?v=sKSxBd56H70">this tutorial</a>.

# 项目中文简介

长毛象机器人：<a rel="me" href="https://bgme.me/@ciao">操操</a>

mastodon即长毛象，是一个去中心化的社交平台。操操是长毛象平台的自动回复机器人项目。

本项目运行逻辑为bot.js持续监听长毛象API，通过bot.js本体或fork python程序完成指令，bot.js向用户发嘟文返回结果

每个功能对应的py文件请在bot.js里ctrl+F吧……实在记不清了233

# 以下为截止 2022/11/02 操操的所有功能

【poem/诗】-> 按照太阳的启示，返回一首汉语现代诗

【找文/抽文/随机文】 -> 按照月亮的启示，从ao3总库中为你甄选一篇中文作品

【AU/paro/梗 】 -> 今晚可以搞点什么

【点拨】 -> 若有烦心事可以试试看

【spirit animal/灵魂动物】 -> 检测你的灵魂动物（也可能是奇怪的东西）

【奇遇/冒险】+换行两次写两个主人公 -> 我会立刻观测附近平行宇宙中这两个人的奇遇并向你汇报！

          示例嘟文格式为：
          @操操 奇遇
          角色1
          角色2

【写一句/你好/接龙】+换行写一句话 -> 我会记录您的句子，与广大网友的话接龙成一首诗，每十四行一篇自动推送！（目前每人每天限投一句）

          示例嘟文格式为：
          @操操 你好
          Hello World!

【抽卡】+换行写人物名字 -> 我会为该角色抽卡，ssr掉率高达百分之十！

          示例嘟文格式：
          @操操 抽卡
          人物名字

【扔瓶子/丢瓶子】 -> 该条嘟文的文本将被扔进大海中！我不会记录投递人的账号信息，如果需要，您可以自行留在文本中。务必注意！嘟文中可以换行，但不要有空行（不限行数）！

          示例嘟文格式：
          @操操 扔瓶子
          第一句话
          第二句话
          第三句话

【捡瓶子/收瓶子】 -> 我会为你从大海里捡一个来自陌生人的瓶子！

【加儿/儿化音】+换行写一句话 -> 我会为换行中的内容加儿化音！

          嘟文示例：
          @操操 儿化音
          我在这，你在哪呢

【菜谱】 -> 我会建议你今晚可以吃点什么（黑暗料理）！

【小名】 -> 我会根据你提供的名字（但愿）起个小名！

          嘟文示例：
          @操操 小名
          空条徐伦

【转发/转嘟 】 -> 我会转嘟（若无紧急情况，请务必不要使用）！

【lucky/幸运数】 -> 我会回复你一个0~99之间的幸运数！

【日文名】 -> 我会回复你一个日文名！

【出国/属地】 -> 我会回复你世界上的某个城镇！（数据是我妈从维基扒的）

【宠物】 -> 要不要签订契约，成为赛博宠物？

【出家】 -> 赛博出家

【法号】 -> 来个法号

【还俗】 -> 一键还俗

【绕口令】 -> 来个绕口令

【abo】 -> 操操的abo测试是，一场豪赌

          示例：
          @操操 abo
          角色1
          角色2

【分院帽】 -> 入学霍格沃茨！

【全职】 -> 全职高手平行宇宙中你的游戏职业

【独角兽】 -> 千分之一的概率找到独角兽，届时会广播

【绕口令】 -> 来个绕口令

【饿了】 -> 馋你一下

【拉郎】 -> 操操会在给出的一群人中找出天注定相性最好的一对的佳人

          示例：
          @操操 拉郎
          角色1
          角色2
          角色3
          ……

英文名|英语名|英語名

替身|sutando

酱|醬

joke|笑話|笑话

猫语|貓語

登基|登机

驾崩|駕崩

谥号|謚號

入宫|入宮

江湖|拜入

妖怪|原形

钓鱼|釣魚

种瓜|種瓜

偷瓜|偷菜

林克|link

守望|特工

方舟|干员|幹員

挖矿|挖礦|矿工|礦工

海鸥|海鷗

旋律|主题曲|主題曲

结婚|結婚|婚礼|婚禮

睡操操|睡觉|睡覺

忏悔|懺悔

快递|快遞

          示例：
          @ciao 快递
          allthestar@alive.bar（改为您快递收件人的完整地址，开头不要有@符号）
          包裹中的内容写在第三行


# Requirements

1. nodejs[14.16.1]（library文件里包含了）

2. python[3.7.4]（以下是需要的library）

   ----- requests

   ----- bs4

3. 服务器跑额外需要pm2

# 环境布置好后启动程序

1. 在自己电脑跑：打开一个terminal，输入【node bot.js】启动即可。关机会停止工作

2. 在服务器：ssh到服务器，输入【pm2 start bot.js】启动

# 边学边做的保姆级教学

<a href="https://www.youtube.com/watch?v=sKSxBd56H70">油管up主：The Coding Train</a>

我没有node基础，全程是看这个教程做的，讲得很细致（对于做一个bot足够用）

# 如果你不太熟悉代码且不想学且真的想跑这个机器人的教程（会有这种勇士吗）

以下所有步骤针对干净如纸纯洁善良未历世事的windows，如果你35块买了个xx云服务器，就按自己服务器系统搜一下各种安装的对应命令，比如搜“linux安装python”（相信会买服务器的同学也不用看这段教程）直接在终端输入各种命令下载 .tar.gz 安装包解压安装

### 1. <a href="https://www.bilibili.com/read/cv13671309">安装python</a>

### 2. <a href="https://blog.csdn.net/qq_45752401/article/details/122299475">安装node</a>

### 3. 检查装没装好

打开一个cmd（win+r,cmd,回车）输入

python --version 回车

node --version 回车

分别回复给你相应版本号就行了（版本比上边写的高就行了，低一点应该也问题不大？）

### 4. 安装 python library。在命令行里输入

pip install requests 回车

pip install bs4 回车

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

# Freetalk（够了，你以为这是同人本吗！）

我在尝试的过程中发现启动后第一次通知往往收不到（可能是我连接的问题？）多艾特一次就好了

如果有时候网页收得到提醒但console没log东西，比较可能是丢包，ping一下您的站点试试 ;-)