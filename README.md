# auto_screenshot
基于Python的自动截图程序。
===
版本v1.2.0
---

===

·基本功能
===
调用PIL库ImageGrab()函数截图，每隔十五分钟截图一次，并且只在xx:00,xx:15,xx:30,xx:45进行截图，适合于天狼50软件数据记录分析。截图成功将发送邮件至指定邮箱（需要开启简单邮件传输协议（Simple Mail Transfer Protocol,SMTP）），具体操作百度解决。

===
·使用说明
===
日常使用（.exe）版本
---
下载.exe目录下的auth.json（必要！！）和软件本体（auto_screenshot.exe）并放置于同一目录下，在auth.json中模仿示例填入对应数据
.json文件使用说明：
	"From" : "你的邮箱地址", "SMTP" : "根据邮箱提供商而定，例如QQ邮箱为smtp.qq.com", "Pswd" : "开启SMTP服务时提供的授权码，例如QQ邮箱为16位，若未提供则可能为邮箱密码"， "To" : "可以填写与From栏相同的地址"

研究版本（.py）版本
---
与日常使用版本相同。
