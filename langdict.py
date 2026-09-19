language = "简体中文"
lang_dict = {
    "English": {
        "QLabel" : """<h1>Any Android will eventually <i style="color:red;">explode</i>!</h1>|
This software contains some features about Android and APK|
Need to rely on other tools such as Java (add PATH environment variable)|
The software is just like shit, roast that there is no reward!|
Project path|Language|<h2>ADB command</h2>|Basic connect commands|Application management commands|The APK path to install|
The package name to uninstall|<h2>Input</h2>|<h2>Action Button</h2>|<h2>Log output</h2>|<h2>Command preview</h2>|
File management commands|File path to push|File path to pull|Device folder to view|Log and system information commands|
Simulate interaction and input, record|Physical key KEYCODE|Tap Coordinate (x,y)|Swipe parametersENTER(x1,y1,x2,y2,seconds)|
Text input content|<h2>Note:</h2>|Only versions above 3.0.1 are supported!|Requires Java and apktool.jar|apktool.jar path|
""".replace("\n", '').replace('ENTER', '\n'),
        "QPushButton": """ADB Command GUI Tool|Android Project Packaging|ApkTool Unpacking/Reverse APK|Check devices|
Stop ADB|Install APK|Restart ADB (root) privileges|Uninstall APK|One-click package|Execute command|
List all package names|Push files|Pull files|View device files|Logcat|Clear log buffer|Service information|
Battery status|App memory usage|Activity stack information|Physical key|Screen tap|Swipe|Text input|Screenshot|
Start screen rec|Stop screen rec|
""".replace('\n', ''),
        "QCheckBox": """Reinstall|Downgrade install|Keep data|Grant all|Allow test packages|

""".replace('\n', ''),
        "QComboBox": """No devices connected|
""".replace("\n", ''),
        "Other": """Error
""".replace('\n', ''),
    },
    "简体中文": {
        "QLabel": """<h1>任何Android终将<i style="color:red;">爆炸</i>！</h1>|该软件包含关于Android和apk的一些功能|
需要依赖其他工具比如Java（需添加PATH环境变量）|软件做的跟屎一样，吐槽没奖励|项目路径|语言|<h2>ADB命令</h2>|基础连接命令|应用管理命令|
要安装的APK的路径|要卸载的应用的包名|<h2>输入</h2>|<h2>操作按钮</h2>|输出|命令预览|文件管理命令|传送的文件的地址|拉取的文件的地址|
要查看内容的设备文件夹|日志与系统信息命令|模拟交互与输入，录制|物理按键的KEYCODE|点击屏幕的坐标（x,y）|滑动所需要的信息ENTER（x1,y1,x2,y2,seconds）|
文本输入内容（不支持中文）|<h2>注意：</h2>|仅支持3.0.1以上的版本|依赖Java和apktool.jar|apktool.jar路径|
""".replace("\n", '').replace('ENTER', '\n'),
        "QPushButton": """ADB命令图形界面工具|Android项目打包|ApkTool解包/逆向APK|查看连接设备|停止ADB进程|安装APK|
root权限重启ADB|卸载APK|一键打包|执行命令|列出所有已安装应用包名|电脑传送文件|手机拉取文件|查看设备文件夹内容|实时输出设备系统日志|
清除设备日志缓冲区|设备系统服务信息|设备电池状态|应用的内存占用|Activity栈信息|物理按键|屏幕点击|滑动|文本输入|截屏|开始录屏|停止录屏
""".replace("\n", ''),
        "QCheckBox": """覆盖安装|降级安装|保留数据|授予所有运行时权限|允许测试包|

""".replace('\n', ''),
        "QComboBox": """暂无连接设备|
""".replace('\n', ''),
        "Other": """错误|
""".replace('\n', ''),
    }
}

def switch_language(lang):
    global language
    language = lang

def get_dict_word(key, value):
    return lang_dict[language][key].split('|')[value]
