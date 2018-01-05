# Wechat_Jump_Game

### 一个自己写的玩跳一跳的脚本

### 需要：

- adb
- 一台Android手机（或模拟器）
- Python 下的PIL和numpy库

### 具体步骤：

- 用USB链接电脑和手机，开启USB调试。或者使用BlueStacks模拟器


- ~~~bash
  adb kill-server
  adb devices
  adb connect [ip]:[port]
  #ip是手机的ip或者127.0.0.1（模拟器），端口号在adb devices的返回结果中有
  ~~~

- 开始跳一跳游戏

- ~~~bash
  python jump.py
  ~~~

