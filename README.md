# auto_screenshot
基于Python的自动截图程序。
版本v1.2.0
调用PIL进行截图，每隔十五分钟进行一次截图，截图保存至与程序同一目录下。截图成功则发送邮件至指定邮箱（需发送者开启SMTP服务）。
要求输入的密码为授权码，不是邮箱的登陆密码！！这里可以自行百度
目前提供.py格式和.exe格式，前者供研究用，后者供日常使用。若选用前者，Linux及Mac用户请按系统要求在文件开头添加必要注释。
