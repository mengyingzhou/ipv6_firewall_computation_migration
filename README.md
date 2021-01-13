# 目录

- [1. 基于IPv6的移动边缘计算网络服务系统](#1-基于ipv6的移动边缘计算网络服务系统)
- [2. IPv6防火墙](#2-ipv6防火墙)
  - [2.1. Webwall for iptables/ipv6tables setting](#21-webwall-for-iptablesipv6tables-setting)
    - [2.1.1. 安装环境](#211-安装环境)
    - [2.1.2. 运行指南](#212-运行指南)
  - [2.2. Firewall Tester for IPv6](#22-firewall-tester-for-ipv6)
    - [2.2.1. 项目结构](#221-项目结构)
    - [2.2.2. 安装环境](#222-安装环境)
    - [2.2.3. 运行指南](#223-运行指南)
      - [2.2.3.1. Server端](#2231-server端)
      - [2.2.3.2. Client端](#2232-client端)
- [3. 计算迁移](#3-计算迁移)
  - [3.1. server](#31-server)
  - [3.2. client](#32-client)



# 1. 基于IPv6的移动边缘计算网络服务系统
本课题希望通过在IPv6网络基础设施中引入微云(cloudlet，即几个或几十个服务器组成的计算集群)，利用云计算与虚拟 化技术，构建一个针对移动边缘计算的网络服务平台。这一平台可以帮助移动互联网服务提供商和网络应用提供商 在网络基础设施当中部署不同类型的网络服务。在纯IPv6环境中支持防火墙管理和计算迁移功能。


# 2. IPv6防火墙
## 2.1. Webwall for iptables/ipv6tables setting
本项目方便用户使用web界面进行iptables/ip6tables设置。iptables是非常强大的个人用防火墙，而且还完全免费。但是iptables复杂的规则设置使得普通用户望而却步，本项目将iptables的设置通过web界面呈现，并且提供了部分常用功能的简化版本，方便用户进行设置。

### 2.1.1. 安装环境
为了方便用户进行环境安装，项目组编写了部分bash代码，存储在scripts文件夹下
* 放置文件夹，将webwall文件夹放置到/opt文件夹下
* 运行安装核心功能，
```bash
cd firewall/webwall
bash scripts/install-core.sh
```
* 运行安装web功能
```bash
bash scripts/install-web.sh
```

### 2.1.2. 运行指南
运行安装web功能完成后，web界面即可访问，访问地址为[ip地址]:37001, 第一次访问会要求设置用户名密码，后续访问即可使用设置的用户名密码登录


## 2.2. Firewall Tester for IPv6

Firewall Tester for IPv6 用于测量防火墙对应的IPv6功能。

### 2.2.1. 项目结构
请先进入```firewall/ft6```文件夹中。

本项目是以Client/Server架构为基础，测试它们之间防火墙的功能是否可以满足部分IPv6包过滤的功能。运行时可在Client端运行client.py文件，在Server端运行server.py文件。Client端运行设有Qt对应的用户图形界面，可清晰反映测试是否通过。

### 2.2.2. 安装环境
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

### 2.2.3. 运行指南

#### 2.2.3.1. Server端
在server端需要是用root权限运行代码，运行之后可根据命令行提示选择监听的IPv6地址与端口，请确保选择监听的端口没有被占用
#### 2.2.3.2. Client端
client端代码运行之后，可在图形化界面填写server端地址，以及对应的开放端口，和作为对比的关闭端口。点击复选框选择需要运行的测试，再点击Start按钮即可运行测试。稍作等待可在右侧窗口处获得运行结果。


# 3. 计算迁移
## 3.1. server
```bash
cd computation_migration/distComuputing
python manage.py migrate
python manage.py runserver --ipv6 [::]:8000
```
## 3.2. client
```bash
cd computation_migration/client
cpulimit -l 50 python main.py
```