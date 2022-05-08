# mastodon_bot 长毛象机器人

# English Summary:

CaoCao (Fuck*2 in Chinese) is an autoresponder bot project for mastodon. The functions are: accept sentences from users to write a sonnet solitaire, drift bottle, find a random work in ao3, find a random poem online, accept two character names to return a random story, etc. 

All the texts involved are Chinese. If you are a newbie like me and working on build your own bot, I (strongly) recommend <a href="https://www.youtube.com/watch?v=sKSxBd56H70">this tutorial</a>.

# 以下为中文介绍
长毛象机器人：<a rel="me" href="https://bgme.me/@ciao">操操</a>

mastodon即长毛象，是一个去中心化的社交平台。操操是长毛象平台的自动回复机器人项目。

艾特操操，并在文本中提问关键词，操操就会用你选择的可见范围回复你。

关注操操，操操会发一条嘟文感谢。

有些特别词语可以触发操操的特定回复，bot.js中均有标注。


-------以下是不需要特殊格式的功能-------


【喜欢/点赞】 -> 我会给你的嘟文点赞

【转发/转嘟 】-> 我会转嘟

【幸运数/lucky】 -> 我会回复你一个0~99之间的幸运数

【poem/诗】-> 我会按照太阳的启示，返回你一首近现代诗。来源于http://www.chinapoesy.com

【找文/抽文/随机文】 -> 我会按照月亮的启示，从ao3总库中为你甄选一篇作品

【AU/paro/梗 】-> 我会建议你今晚可以写点什么男男操屁股


--------以下是需要特殊格式的功能--------


【奇遇/冒险+换行两次写两个主人公】 -> 我会立刻观测附近平行宇宙中这两个人的奇遇并向你汇报！

          [注意：用换行隔开两个人]
          示例嘟文格式为：
          @操操 奇遇
          角色1
          角色2
          
【加一句/来一句/写一句/你好/接龙+换行写一句话】 -> 您的句子将被操操记录，与广大象友的话接龙成一首诗，视云端收到的句子数目每晚推送。一次投稿多次换行默认记录最后一行！

          示例嘟文格式为：
          @操操 你好
          Hello World!
          
 【抽卡/抽牌+换行写一个人名】 -> 生成这个人的卡牌，SSR掉率10%有三个技能，SR与R技能书递减概率递增具体多少在random_card里调整

          示例嘟文格式为：
          @操操 抽卡
          路人甲
          
  【扔瓶子/丢瓶子+换行写一段话】 -> 在/letter这个文件夹中生成一个txt文档，里面储存的是经过base64加密的这些话

          示例嘟文格式为：
          @操操 扔瓶子
          第一句话
          第二句话
          第三句话
          ……
          
【捡瓶子/收瓶子】 -> 从/letter中随机取一个文档，以嘟文格式回复
          
【grammar/LanguageTool】 -> 您的英语作文将被发送至开源自动校对项目languagetool检查可能存在的语法错误


# 逻辑

bot.js持续监听长毛象API，通过bot.js或fork python程序完成指令，bot.js向用户发嘟文返回结果

python程序对应：

LanguageTool|grammar -> grammar_check.py

paro|AU|梗 -> AU.py

奇遇|冒险 -> adventure.py

诗|poem -> poem.py

找文|抽文|随机文 -> random_fanfic.py

加一句|来一句|写一句|你好|接龙 -> write_poem.py

抽卡|抽牌 -> random_card.py

扔瓶子|丢瓶子 -> write_letter.py

捡瓶子|收瓶子 -> read_letter.py

# 为了跑这些代码，你需要

1. nodejs[14.16.1]（library文件里包含了）

2. python[3.7.4]（以下是需要的library）

   ----- requests

   ----- bs4

3. 服务器跑额外需要pm2

# 环境布置好后启动程序

1. 在自己电脑跑：打开一个terminal，输入【node bot.js】启动即可。关机会停止工作

2. 在服务器：ssh到服务器，输入【pm2 start bot.js】启动即可

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

我在尝试的过程中发现启动后第一次通知往往收不到（可能是我连接的问题？）多艾特一次就好了
