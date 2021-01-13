# Firewall Tester for IPv6

Firewall Tester for IPv6 用于测量防火墙对应的IPv6功能。

### 项目结构
本项目是以Client/Server架构为基础，测试它们之间防火墙的功能是否可以满足部分IPv6包过滤的功能。运行时可在Client端运行client.py文件，在Server端运行server.py文件。Client端运行设有Qt对应的用户图形界面，可清晰反映测试是否通过。

### 安装环境
本项目的运行环境要求如下：
* Python 2.7
```bash
apt-get install python2.7
```
* PyQt4
```bash
apt-get install python-qt4
```
* Scapy
```bash
pip install scapy==2.3.1
```

### 运行指南

##### Server端
在server端需要是用root权限运行代码，运行之后可根据命令行提示选择监听的IPv6地址与端口，请确保选择监听的端口没有被占用
##### Client端
client端代码运行之后，可在图形化界面填写server端地址，以及对应的开放端口，和作为对比的关闭端口。点击复选框选择需要运行的测试，再点击Start按钮即可运行测试。稍作等待可在右侧窗口处获得运行结果。
