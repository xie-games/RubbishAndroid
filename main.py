# Copyright (c) 2026 XieGames
# This project includes PyQt5, which is licensed under GPLv3.

# 打包命令：
# pyinstaller main.py -i resources/icon.ico -D -w -n RubbishAndroid --add-data "resources;resources"

# 导入模块
import os
import re
import sys
import ctypes
import winsound
import threading
import subprocess

from PyQt5.QtCore import (
    QThread, pyqtSignal
)
from PyQt5.QtGui import (
    QIcon
)
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QCheckBox,
    QTextEdit, QPlainTextEdit
)

# 导入自定义库
import langdict

# 常量
APP_NAME = "Rubbish Android"
VERSION_NAME = "v0.0.2 α"
COMPANY_NAME = "XieGames"
ID_VERSION = "v0.0"
COLOR = "#A4C639"
BACKGROUND_COLOR = "#111"
HOVER_COLOR = "#333"
LAYOUT_STYLE = """
* {
    background-color: """+BACKGROUND_COLOR+""";
}
QCheckBox {
    color: """+COLOR+"""; 
    font-size: 13px
}
QComboBox, QLineEdit, QTextEdit, QPlainTextEdit {
    color: """+COLOR+"""; 
    border: 1px solid """+COLOR+""";
    font-size: 14px; 
    border-radius: 5px;
}
QComboBox QAbstractItemView {
    color: """+COLOR+"""; 
    border: 2px solid """+COLOR+""";
    font-size: 14px; 
}
#layout-widget {
    border: 2px solid """+COLOR+""";
    border-radius: 5px;
}
QLabel {
    color: """+COLOR+""";
    font-size: 14px;
}
QPushButton {
    color: """+COLOR+"""; 
    font-size: 16px;
    border: 1px solid """+COLOR+"""; 
    border-radius: 5px;
    padding: 8px;
}
QPushButton:hover {
    background-color: """+HOVER_COLOR+""";
}
"""

# 全局变量
adb_command = ["adb"]

# 函数区域

# 获取打包后的路径
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

# 检测文件路径是否合法
def check_file_path(path: str) -> bool:
    if not isinstance(path, str) or not path:
        return False
    if '\0' in path:
        return False
    if not path.isascii():
        return False
    for char in ' <>"|?*':
        if char in path:
            return False
    return True

# 打开窗口的函数
def open_adb_window():
    if not adb_window.isVisible():
        adb_window.show()
def open_packaging_window():
    if not packaging_window.isVisible():
        packaging_window.show()
def open_apktool_window():
    if not apktool_window.isVisible():
        apktool_window.show()

# 改变语言
def change_language(text):
    langdict.switch_language(text)

    ql0.setText(langdict.get_dict_word("QLabel", 0))
    ql1.setText(langdict.get_dict_word("QLabel", 1))
    ql2.setText(langdict.get_dict_word("QLabel", 2))
    ql3.setText(langdict.get_dict_word("QLabel", 3))
    ql_project_input.setText(langdict.get_dict_word("QLabel", 4))
    ql_language_choice.setText(langdict.get_dict_word("QLabel", 5))
    ql_command.setText(langdict.get_dict_word("QLabel", 6))
    ql_connect_command.setText(langdict.get_dict_word("QLabel", 7))
    ql_app_command.setText(langdict.get_dict_word("QLabel", 8))
    ql_command_app_apkpath_input.setText(langdict.get_dict_word("QLabel", 9))
    ql_package_name_input.setText(langdict.get_dict_word("QLabel", 10))
    ql_input.setText(langdict.get_dict_word("QLabel", 11))
    ql_control_button.setText(langdict.get_dict_word("QLabel", 12))
    ql_packaging_log.setText(langdict.get_dict_word("QLabel", 13))
    ql_command_log.setText(langdict.get_dict_word("QLabel", 13))
    ql_preview_command.setText(langdict.get_dict_word("QLabel", 14))
    ql_command_file.setText(langdict.get_dict_word("QLabel", 15))
    ql_push_input.setText(langdict.get_dict_word("QLabel", 16))
    ql_pull_input.setText(langdict.get_dict_word("QLabel", 17))
    ql_ls_input.setText(langdict.get_dict_word("QLabel", 18))
    ql_command_syslog.setText(langdict.get_dict_word("QLabel", 19))
    ql_interact_input.setText(langdict.get_dict_word("QLabel", 20))
    ql_keycode_input.setText(langdict.get_dict_word("QLabel", 21))
    ql_tap_coordinate.setText(langdict.get_dict_word("QLabel", 22))
    ql_swipe_input.setText(langdict.get_dict_word("QLabel", 23))
    ql_text_input.setText(langdict.get_dict_word("QLabel", 24))
    ql_apktool_note.setText(langdict.get_dict_word("QLabel", 25))
    ql26.setText(langdict.get_dict_word("QLabel", 26))
    ql27.setText(langdict.get_dict_word("QLabel", 27))
    ql_apktool_input.setText(langdict.get_dict_word("QLabel", 28))

    adb_button.setText(langdict.get_dict_word("QPushButton", 0))
    packaging_button.setText(langdict.get_dict_word("QPushButton", 1))
    apktool_button.setText(langdict.get_dict_word("QPushButton", 2))
    devices_button.setText(langdict.get_dict_word("QPushButton", 3))
    stop_button.setText(langdict.get_dict_word("QPushButton", 4))
    install_button.setText(langdict.get_dict_word("QPushButton", 5))
    root_button.setText((langdict.get_dict_word("QPushButton", 6)))
    uninstall_button.setText(langdict.get_dict_word("QPushButton", 7))
    start_packaging_button.setText(langdict.get_dict_word("QPushButton", 8))
    execute_command_button.setText(langdict.get_dict_word("QPushButton", 9))
    list_app_button.setText(langdict.get_dict_word("QPushButton", 10))
    transfer_button.setText(langdict.get_dict_word("QPushButton", 11))
    pull_button.setText(langdict.get_dict_word("QPushButton", 12))
    list_button.setText(langdict.get_dict_word("QPushButton", 13))
    logcat_button.setText(langdict.get_dict_word("QPushButton", 14))
    clear_button.setText(langdict.get_dict_word("QPushButton", 15))
    system_information_button.setText(langdict.get_dict_word("QPushButton", 16))
    battery_status_button.setText(langdict.get_dict_word("QPushButton", 17))
    app_memory_button.setText(langdict.get_dict_word("QPushButton", 18))
    activity_stack_button.setText(langdict.get_dict_word("QPushButton", 19))
    physical_key_button.setText(langdict.get_dict_word("QPushButton", 20))
    screen_tap_button.setText(langdict.get_dict_word("QPushButton", 21))
    swipe_button.setText(langdict.get_dict_word("QPushButton", 22))
    text_input_button.setText(langdict.get_dict_word("QPushButton", 23))
    screenshot_button.setText(langdict.get_dict_word("QPushButton", 24))
    start_screen_record_button.setText(langdict.get_dict_word("QPushButton", 25))
    stop_screen_record_button.setText(langdict.get_dict_word("QPushButton", 26))

    adb_window.setWindowTitle(langdict.get_dict_word("QPushButton", 0))
    packaging_window.setWindowTitle(langdict.get_dict_word("QPushButton", 1))
    apktool_window.setWindowTitle(langdict.get_dict_word("QPushButton", 2))

    reinstall_checkbox.setText(langdict.get_dict_word("QCheckBox", 0))
    downgrade_checkbox.setText(langdict.get_dict_word("QCheckBox", 1))
    keepdata_checkbox.setText(langdict.get_dict_word("QCheckBox", 2))
    grant_checkbox.setText(langdict.get_dict_word("QCheckBox", 3))
    test_packages_checkbox.setText(langdict.get_dict_word("QCheckBox", 4))

    serial_combobox.clear()
    serial_combobox.addItem(langdict.get_dict_word("QComboBox", 0))

    window.adjustSize()

# adb窗口函数

def check_adb_command(command: str) -> bool:
    if "adb" not in command:
        return False
    else:
        return True

# adb窗口的槽
def exec_command():
    if not check_adb_command(adb_command):
        command_log.setPlainText(langdict.get_dict_word("Other", 0))
        return 1
    if not check_adb_command(preview_command.text().split(' ')):
        command_log.setPlainText(langdict.get_dict_word("Other", 0))
        return 1

    # Todo: 这玩意得加进线程
    result = subprocess.run(adb_command, text=True, capture_output=True)

    if result.returncode != 0:
        result = subprocess.run(preview_command.text().split(' '), text=True, capture_output=True)
        if result.returncode != 0:
            command_log.setPlainText(langdict.get_dict_word("Other", 0))
            return 1

    if "devices" in adb_command:
        pass


def devices_button_slot():
    global adb_command
    adb_command = ["adb", "devices"]
    preview_command.setText(' '.join(adb_command))
def stop_button_slot():
    global adb_command
    adb_command = ["adb", "kill-server"]
    preview_command.setText(' '.join(adb_command))
def root_button_slot():
    global adb_command
    adb_command = ["adb", "root"]
    preview_command.setText(' '.join(adb_command))

def install_button_slot():
    global adb_command
    adb_command = ["adb", "install"]

    if check_file_path(apkpath_input.text()):
        adb_command.append(apkpath_input.text())

    if reinstall_checkbox.isChecked():
        adb_command.append("-r")
    if downgrade_checkbox.isChecked():
        adb_command.append("-d")
    if grant_checkbox.isChecked():
        adb_command.append("-g")
    if test_packages_checkbox.isChecked():
        adb_command.append("-t")
    preview_command.setText(' '.join(adb_command))
def uninstall_button_slot():
    global adb_command
    adb_command = ["adb", "uninstall"]
    if keepdata_checkbox.isChecked():
        adb_command.append("-k")
    preview_command.setText(' '.join(adb_command))
def list_app_button_slot():
    pass

# 任务栏图标
if sys.platform == "win32":
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        f"P{COMPANY_NAME}.{VERSION_NAME.replace(' ', '')}.{ID_VERSION}"
    )

ICON = resource_path("resources/icon.png")

app = QApplication(sys.argv)

# 主窗口
window = QWidget()
window.setStyleSheet(f"background: {BACKGROUND_COLOR};")
window.setWindowTitle(f"{APP_NAME} {VERSION_NAME}")
window.setWindowIcon(QIcon(ICON))

window_layout = QVBoxLayout()

main_widget = QWidget()
main_widget.setStyleSheet(LAYOUT_STYLE)
main_widget.setObjectName("layout-widget")
main_layout = QVBoxLayout()

word_widget = QWidget()
word_layout = QVBoxLayout()

ql_language_choice = QLabel(langdict.get_dict_word("QLabel", 5))
word_layout.addWidget(ql_language_choice)
language_choice = QComboBox()
language_choice.addItems(["English", "简体中文"])
language_choice.setCurrentText(langdict.language)
language_choice.currentTextChanged.connect(change_language)
word_layout.addWidget(language_choice)

ql0 = QLabel(langdict.get_dict_word("QLabel", 0))
word_layout.addWidget(ql0)
ql1 = QLabel(langdict.get_dict_word("QLabel", 1))
word_layout.addWidget(ql1)
ql2 = QLabel(langdict.get_dict_word("QLabel", 2))
word_layout.addWidget(ql2)
ql3 = QLabel(langdict.get_dict_word("QLabel", 3))
word_layout.addWidget(ql3)

word_widget.setLayout(word_layout)

func_widget = QWidget()
func_widget.setObjectName("layout-widget")
func_layout = QVBoxLayout()

f1_layout = QHBoxLayout()
adb_button = QPushButton(langdict.get_dict_word("QPushButton", 0))
adb_button.clicked.connect(open_adb_window)
f1_layout.addWidget(adb_button)
packaging_button = QPushButton(langdict.get_dict_word("QPushButton", 1))
packaging_button.clicked.connect(open_packaging_window)
f1_layout.addWidget(packaging_button)

f2_layout = QHBoxLayout()
apktool_button = QPushButton(langdict.get_dict_word("QPushButton", 2))
apktool_button.clicked.connect(open_apktool_window)
f2_layout.addWidget(apktool_button)

func_layout.addLayout(f1_layout)
func_layout.addLayout(f2_layout)
func_widget.setLayout(func_layout)
main_layout.addWidget(word_widget)
main_layout.addWidget(func_widget)
main_widget.setLayout(main_layout)
window_layout.addWidget(main_widget)
window.setLayout(window_layout)

window.show()

# ADB命令图形界面工具窗口
adb_window = QWidget()
adb_window.setStyleSheet(LAYOUT_STYLE)
adb_window.setWindowTitle(langdict.get_dict_word("QPushButton", 0))
adb_window.setWindowIcon(QIcon(ICON))

adb_window_layout = QHBoxLayout()

command_widget = QWidget()
command_widget.setObjectName("layout-widget")
command_layout = QVBoxLayout()
ql_command = QLabel(langdict.get_dict_word("QLabel", 6))
command_layout.addWidget(ql_command)

# 基础连接命令
command_connect_widget = QWidget()
command_connect_widget.setObjectName("layout-widget")
command_connect_layout = QVBoxLayout()
ql_connect_command = QLabel(langdict.get_dict_word("QLabel", 7))
command_connect_layout.addWidget(ql_connect_command)
# 按钮布局
command_connect_button_widget = QWidget()
command_connect_button_widget.setObjectName("layout-widget")
command_connect_button_layout = QHBoxLayout()

devices_button = QPushButton(langdict.get_dict_word("QPushButton", 3))
devices_button.clicked.connect(devices_button_slot)
command_connect_button_layout.addWidget(devices_button)
stop_button = QPushButton(langdict.get_dict_word("QPushButton", 4))
stop_button.clicked.connect(stop_button_slot)
command_connect_button_layout.addWidget(stop_button)
root_button = QPushButton(langdict.get_dict_word("QPushButton", 6))
root_button.clicked.connect(root_button_slot)
command_connect_button_layout.addWidget(root_button)

command_connect_button_widget.setLayout(command_connect_button_layout)
# 选择框布局
command_connect_combobox_widget = QWidget()
command_connect_combobox_widget.setObjectName("layout-widget")
command_connect_combobox_layout = QHBoxLayout()

serial_combobox = QComboBox()
serial_combobox.addItem(langdict.get_dict_word("QComboBox", 0))
command_connect_combobox_layout.addWidget(serial_combobox)

command_connect_combobox_widget.setLayout(command_connect_combobox_layout)

command_connect_layout.addWidget(command_connect_button_widget)
command_connect_layout.addWidget(command_connect_combobox_widget)
command_connect_widget.setLayout(command_connect_layout)

# 应用管理命令
command_app_widget = QWidget()
command_app_widget.setObjectName("layout-widget")
command_app_layout = QVBoxLayout()
ql_app_command = QLabel(langdict.get_dict_word("QLabel", 8))
command_app_layout.addWidget(ql_app_command)
# 按钮布局
command_app_button_widget = QWidget()
command_app_button_widget.setObjectName("layout-widget")
command_app_button_layout = QHBoxLayout()

install_button = QPushButton(langdict.get_dict_word("QPushButton", 5))
install_button.clicked.connect(install_button_slot)
command_app_button_layout.addWidget(install_button)
uninstall_button = QPushButton(langdict.get_dict_word("QPushButton", 7))
uninstall_button.clicked.connect(uninstall_button_slot)
command_app_button_layout.addWidget(uninstall_button)
list_app_button = QPushButton(langdict.get_dict_word("QPushButton", 10))
list_app_button.clicked.connect(list_app_button_slot)
command_app_button_layout.addWidget(list_app_button)

command_app_button_widget.setLayout(command_app_button_layout)
# 勾选框布局
command_app_checkbox_widget = QWidget()
command_app_checkbox_widget.setObjectName("layout-widget")
command_app_checkbox_layout = QHBoxLayout()

reinstall_checkbox = QCheckBox(langdict.get_dict_word("QCheckBox", 0))
command_app_checkbox_layout.addWidget(reinstall_checkbox)
downgrade_checkbox = QCheckBox(langdict.get_dict_word("QCheckBox", 1))
command_app_checkbox_layout.addWidget(downgrade_checkbox)
keepdata_checkbox = QCheckBox(langdict.get_dict_word("QCheckBox", 2))
command_app_checkbox_layout.addWidget(keepdata_checkbox)
grant_checkbox = QCheckBox(langdict.get_dict_word("QCheckBox", 3))
command_app_checkbox_layout.addWidget(grant_checkbox)
test_packages_checkbox = QCheckBox(langdict.get_dict_word("QCheckBox", 4))
command_app_checkbox_layout.addWidget(test_packages_checkbox)

command_app_checkbox_widget.setLayout(command_app_checkbox_layout)
# 输入框布局
command_app_input_widget = QWidget()
command_app_input_widget.setObjectName("layout-widget")
command_app_input_layout = QVBoxLayout()

ql_command_app_apkpath_input = QLabel(langdict.get_dict_word("QLabel", 9))
command_app_input_layout.addWidget(ql_command_app_apkpath_input)
apkpath_input = QLineEdit()
command_app_input_layout.addWidget(apkpath_input)
ql_package_name_input = QLabel(langdict.get_dict_word("QLabel", 10))
command_app_input_layout.addWidget(ql_package_name_input)
package_name_input = QLineEdit()
command_app_input_layout.addWidget(package_name_input)

command_app_input_widget.setLayout(command_app_input_layout)

command_app_layout.addWidget(command_app_button_widget)
command_app_layout.addWidget(command_app_checkbox_widget)
command_app_layout.addWidget(command_app_input_widget)

command_app_widget.setLayout(command_app_layout)
# 文件管理命令
command_file_widget = QWidget()
command_file_widget.setObjectName("layout-widget")
command_file_layout = QVBoxLayout()

ql_command_file = QLabel(langdict.get_dict_word("QLabel", 15))
command_file_layout.addWidget(ql_command_file)

# 按钮布局
command_file_button_widget = QWidget()
command_file_button_widget.setObjectName("layout-widget")
command_file_button_layout = QHBoxLayout()

transfer_button = QPushButton(langdict.get_dict_word("QPushButton", 11))
command_file_button_layout.addWidget(transfer_button)
pull_button = QPushButton(langdict.get_dict_word("QPushButton", 12))
command_file_button_layout.addWidget(pull_button)
list_button = QPushButton(langdict.get_dict_word("QPushButton", 13))
command_file_button_layout.addWidget(list_button)

command_file_button_widget.setLayout(command_file_button_layout)

# 输入框布局
command_file_input_widget = QWidget()
command_file_input_widget.setObjectName("layout-widget")
command_file_input_layout = QVBoxLayout()

ql_push_input = QLabel(langdict.get_dict_word("QLabel", 16))
command_file_input_layout.addWidget(ql_push_input)
push_input = QLineEdit()
command_file_input_layout.addWidget(push_input)
ql_pull_input = QLabel(langdict.get_dict_word("QLabel", 17))
command_file_input_layout.addWidget(ql_pull_input)
pull_input = QLineEdit()
command_file_input_layout.addWidget(pull_input)
ql_ls_input = QLabel(langdict.get_dict_word("QLabel", 18))
command_file_input_layout.addWidget(ql_ls_input)
ls_input = QLineEdit()
command_file_input_layout.addWidget(ls_input)

command_file_input_widget.setLayout(command_file_input_layout)

command_file_layout.addWidget(command_file_button_widget)
command_file_layout.addWidget(command_file_input_widget)
command_file_widget.setLayout(command_file_layout)

# 中间的命令布局
command2_widget = QWidget()
command2_widget.setObjectName("layout-widget")
command2_layout = QVBoxLayout()

# 日志与系统信息命令
command2_syslog_widget = QWidget()
command2_syslog_widget.setObjectName("layout-widget")
command2_syslog_layout = QVBoxLayout()

ql_command_syslog = QLabel(langdict.get_dict_word("QLabel", 19))
command2_syslog_layout.addWidget(ql_command_syslog)

# 按钮布局
command2_log_button_widget = QWidget()
command2_log_button_widget.setObjectName("layout-widget")
command2_log_button_layout = QHBoxLayout()

logcat_button = QPushButton(langdict.get_dict_word("QPushButton", 14))
command2_log_button_layout.addWidget(logcat_button)
clear_button = QPushButton(langdict.get_dict_word("QPushButton", 15))
command2_log_button_layout.addWidget(clear_button)

command2_log_button_widget.setLayout(command2_log_button_layout)

command2_sys_button_widget = QWidget()
command2_sys_button_widget.setObjectName("layout-widget")
command2_sys_button_layout = QVBoxLayout()
command2_sys_button_layout_top = QHBoxLayout()
command2_sys_button_layout_bottom = QHBoxLayout()

command2_sys_button_layout.addLayout(command2_sys_button_layout_top)
command2_sys_button_layout.addLayout(command2_sys_button_layout_bottom)

system_information_button = QPushButton(langdict.get_dict_word("QPushButton", 16))
command2_sys_button_layout_top.addWidget(system_information_button)
battery_status_button = QPushButton(langdict.get_dict_word("QPushButton", 17))
command2_sys_button_layout_top.addWidget(battery_status_button)
app_memory_button = QPushButton(langdict.get_dict_word("QPushButton", 18))
command2_sys_button_layout_bottom.addWidget(app_memory_button)
activity_stack_button = QPushButton(langdict.get_dict_word("QPushButton", 19))
command2_sys_button_layout_bottom.addWidget(activity_stack_button)

command2_sys_button_widget.setLayout(command2_sys_button_layout)

command2_syslog_layout.addWidget(command2_log_button_widget)
command2_syslog_layout.addWidget(command2_sys_button_widget)
command2_syslog_widget.setLayout(command2_syslog_layout)

# 交互输入布局
command2_interact_input_widget = QWidget()
command2_interact_input_widget.setObjectName("layout-widget")
command2_interact_input_layout = QVBoxLayout()

ql_interact_input = QLabel(langdict.get_dict_word("QLabel", 20))
command2_interact_input_layout.addWidget(ql_interact_input)

command2_interact_input_button_widget = QWidget()
command2_interact_input_button_widget.setObjectName("layout-widget")
command2_interact_input_button_layout = QHBoxLayout()

physical_key_button = QPushButton(langdict.get_dict_word("QPushButton", 20))
command2_interact_input_button_layout.addWidget(physical_key_button)
screen_tap_button = QPushButton(langdict.get_dict_word("QPushButton", 21))
command2_interact_input_button_layout.addWidget(screen_tap_button)
swipe_button = QPushButton(langdict.get_dict_word("QPushButton", 22))
command2_interact_input_button_layout.addWidget(swipe_button)
text_input_button = QPushButton(langdict.get_dict_word("QPushButton", 23))
command2_interact_input_button_layout.addWidget(text_input_button)

command2_interact_input_button_widget.setLayout(command2_interact_input_button_layout)

command2_interact_input_button2_widget = QWidget()
command2_interact_input_button2_widget.setObjectName("layout-widget")
command2_interact_input_button2_layout = QHBoxLayout()

screenshot_button = QPushButton(langdict.get_dict_word("QPushButton", 24))
command2_interact_input_button2_layout.addWidget(screenshot_button)
start_screen_record_button = QPushButton(langdict.get_dict_word("QPushButton", 25))
command2_interact_input_button2_layout.addWidget(start_screen_record_button)
stop_screen_record_button = QPushButton(langdict.get_dict_word("QPushButton", 26))
command2_interact_input_button2_layout.addWidget(stop_screen_record_button)

command2_interact_input_button2_widget.setLayout(command2_interact_input_button2_layout)
# 行输入框布局
command2_interact_input_line_edit_widget = QWidget()
command2_interact_input_line_edit_widget.setObjectName("layout-widget")
command2_interact_input_line_edit_layout = QVBoxLayout()

ql_keycode_input = QLabel(langdict.get_dict_word("QLabel", 21))
command2_interact_input_line_edit_layout.addWidget(ql_keycode_input)
keycode_input = QLineEdit()
command2_interact_input_line_edit_layout.addWidget(keycode_input)
ql_tap_coordinate = QLabel(langdict.get_dict_word("QLabel", 22))
command2_interact_input_line_edit_layout.addWidget(ql_tap_coordinate)
tap_coordinate_input = QLineEdit()
command2_interact_input_line_edit_layout.addWidget(tap_coordinate_input)
ql_swipe_input = QLabel(langdict.get_dict_word("QLabel", 23))
command2_interact_input_line_edit_layout.addWidget(ql_swipe_input)
swipe_input = QLineEdit()
command2_interact_input_line_edit_layout.addWidget(swipe_input)
ql_text_input = QLabel(langdict.get_dict_word("QLabel", 24))
command2_interact_input_line_edit_layout.addWidget(ql_text_input)
text_input = QLineEdit()
command2_interact_input_line_edit_layout.addWidget(text_input)

command2_interact_input_line_edit_widget.setLayout(command2_interact_input_line_edit_layout)

# 命令预览布局
command2_preview_widget = QWidget()
command2_preview_widget.setObjectName("layout-widget")
command2_preview_layout = QVBoxLayout()

ql_preview_command = QLabel(langdict.get_dict_word("QLabel", 14))
command2_preview_layout.addWidget(ql_preview_command)
preview_command = QLineEdit("adb")
command2_preview_layout.addWidget(preview_command)
execute_command_button = QPushButton(langdict.get_dict_word("QPushButton", 9))
execute_command_button.clicked.connect(exec_command)
command2_preview_layout.addWidget(execute_command_button)

command2_preview_widget.setLayout(command2_preview_layout)

command2_interact_input_layout.addWidget(command2_interact_input_button_widget)
command2_interact_input_layout.addWidget(command2_interact_input_button2_widget)
command2_interact_input_layout.addWidget(command2_interact_input_line_edit_widget)
command2_interact_input_widget.setLayout(command2_interact_input_layout)

command2_layout.addWidget(command2_syslog_widget)
command2_layout.addWidget(command2_interact_input_widget)
command2_layout.addWidget(command2_preview_widget)
command2_widget.setLayout(command2_layout)

# adb命令预览执行布局
adb_command_widget = QWidget()
adb_command_widget.setObjectName("layout-widget")
adb_command_layout = QVBoxLayout()

# 命令输出布局
command_log_widget = QWidget()
command_log_widget.setObjectName("layout-widget")
command_log_layout = QVBoxLayout()

ql_command_log = QLabel(langdict.get_dict_word("QLabel", 13))
command_log_layout.addWidget(ql_command_log)
command_log = QPlainTextEdit()
command_log_layout.addWidget(command_log)

command_log_widget.setLayout(command_log_layout)

adb_command_layout.addWidget(command_log_widget)
adb_command_widget.setLayout(adb_command_layout)

command_layout.addWidget(command_connect_widget)
command_layout.addWidget(command_app_widget)
command_layout.addWidget(command_file_widget)

command_widget.setLayout(command_layout)
adb_window_layout.addWidget(command_widget)
adb_window_layout.addWidget(command2_widget)
adb_window_layout.addWidget(adb_command_widget)
adb_window.setLayout(adb_window_layout)

# Android项目打包成APK窗口
packaging_window = QWidget()
packaging_window.setStyleSheet(f"background-color: {BACKGROUND_COLOR};")
packaging_window.setWindowTitle(langdict.get_dict_word("QPushButton", 1))
packaging_window.setWindowIcon(QIcon(ICON))
packaging_window.setStyleSheet(LAYOUT_STYLE)
packaging_window_layout = QHBoxLayout()

# 左布局
packaging_left_widget = QWidget()
packaging_left_widget.setObjectName("layout-widget")
packaging_left_layout = QVBoxLayout()

# 右布局
packaging_right_widget = QWidget()
packaging_right_widget.setObjectName("layout-widget")
packaging_right_layout = QVBoxLayout()

# 输入布局
input_widget = QWidget()
input_widget.setObjectName("layout-widget")
input_layout = QVBoxLayout()

ql_input = QLabel(langdict.get_dict_word("QLabel", 11))
input_layout.addWidget(ql_input)
ql_project_input = QLabel(langdict.get_dict_word("QLabel", 4))
input_layout.addWidget(ql_project_input)
project_input = QLineEdit()
input_layout.addWidget(project_input)

input_widget.setLayout(input_layout)
# 按钮布局
button_widget = QWidget()
button_widget.setObjectName("layout-widget")
button_layout = QVBoxLayout()

ql_control_button = QLabel(langdict.get_dict_word("QLabel", 12))
button_layout.addWidget(ql_control_button)

start_packaging_button = QPushButton(langdict.get_dict_word("QPushButton", 8))
button_layout.addWidget(start_packaging_button)

button_widget.setLayout(button_layout)
# 日志布局
packaging_log_widget = QWidget()
packaging_log_widget.setObjectName("layout-widget")
packaging_log_layout = QVBoxLayout()

ql_packaging_log = QLabel(langdict.get_dict_word("QLabel", 13))
packaging_log_layout.addWidget(ql_packaging_log)
packaging_log = QPlainTextEdit()
packaging_log_layout.addWidget(packaging_log)

packaging_log_widget.setLayout(packaging_log_layout)

packaging_left_layout.addWidget(input_widget)
packaging_left_layout.addWidget(button_widget)
packaging_right_layout.addWidget(packaging_log_widget)

packaging_left_widget.setLayout(packaging_left_layout)
packaging_right_widget.setLayout(packaging_right_layout)

packaging_window_layout.addWidget(packaging_left_widget)
packaging_window_layout.addWidget(packaging_right_widget)
packaging_window.setLayout(packaging_window_layout)

# 解包/逆向窗口
apktool_window = QWidget()
apktool_window.setStyleSheet(LAYOUT_STYLE)
apktool_window.setWindowIcon(QIcon(ICON))
apktool_window.setWindowTitle(langdict.get_dict_word("QPushButton", 2))

apktool_window_layout = QHBoxLayout()

# 注意布局
apktool_note_widget = QWidget()
apktool_note_widget.setObjectName("layout-widget")
apktool_note_layout = QVBoxLayout()

ql_apktool_note = QLabel(langdict.get_dict_word("QLabel", 25))
apktool_note_layout.addWidget(ql_apktool_note)
ql26 = QLabel(langdict.get_dict_word("QLabel", 26))
apktool_note_layout.addWidget(ql26)
ql27 = QLabel(langdict.get_dict_word("QLabel", 27))
apktool_note_layout.addWidget(ql27)

ql_apktool_note_input_widget = QWidget()
ql_apktool_note_input_widget.setObjectName("layout-widget")
ql_apktool_note_input_layout = QVBoxLayout()

ql_apktool_input = QLabel(langdict.get_dict_word("QLabel", 28))
ql_apktool_note_input_layout.addWidget(ql_apktool_input)
apktool_input = QLineEdit()
ql_apktool_note_input_layout.addWidget(apktool_input)

ql_apktool_note_input_widget.setLayout(ql_apktool_note_input_layout)

apktool_note_layout.addWidget(ql_apktool_note_input_widget)
apktool_note_widget.setLayout(apktool_note_layout)

apktool_window_layout.addWidget(apktool_note_widget)
apktool_window.setLayout(apktool_window_layout)

sys.exit(app.exec_())
