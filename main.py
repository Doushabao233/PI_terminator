import json
import random
import hashlib
import tkinter.messagebox as msgbox
from sys import exit, platform, version_info
from tkinter import *
from tkinter.ttk import *

'''
老天爷保佑，这个程序少出点BUG
'''
window = Tk()
window.resizable(False, False)
window.tk.call('source', 'sun-valley.tcl')
window.tk.call('set_theme', 'light')

# 圆周率
pi = 3.14

# 变量
current_version = '1.1.1'
python_version = '{0}.{1}.{2}'.format(
    version_info.major, 
    version_info.minor, 
    version_info.micro
)
cheat = False
question = StringVar()
float_number = 0 # 计算机在后台计算出的答案结果，这才是答案
random_int_list = [2, 3, 4, 5, 6, 8, 10, 20] # 每次出题时的一个因数 用它 * 3.14
factor = 0 # 从上面选择出来的因数
score = 0 # 玩家分数

# 读取设置文件
with open('settings.json', 'r', encoding='utf-8') as f:
    settings = json.loads(f.read())

# 读取语言文件
with open('languages\\' + settings['language_file'], 'r', encoding='utf-8') as f:
    lang = json.loads(f.read())
    # 如果版本号不匹配则自动报错
    if lang['version'] != current_version:
        window.withdraw()
        msgbox.showerror('错误', '程序的语言文件对应的软件版本不同，因此程序现在无法运行。\n你可以向软件的原始作者索要语言文件。同时，请不要擅自修改语言文件中的版本以免造成不可预知的后果。')
        msgbox.showerror('Error', 'The software version corresponding to the language file of the program is different, so the program cannot run now.\nYou can ask the original author of the software for the language file. At the same time, please do not modify the version in the language file without authorization to cause unpredictable consequences.')
        exit()

window.title(lang['gui']['title.1'])

# 创建菜单栏
def about():
    msgbox.showinfo(
        lang['message']['menubar']['msg6.title'], 
        lang['message']['menubar']['msg6.text'].format(platform, python_version)
    )
def version():
    msgbox.showinfo(lang['message']['menubar']['msg7.title'], lang['message']['menubar']['msg7.text'].format(current_version))

menubar = Menu(window)
menu_help = Menu(menubar, tearoff=0)
menubar.add_cascade(label=lang['gui']['menubar.help'], menu=menu_help)

menu_help.add_command(label=lang['gui']['menubar.help.about'], command=about)
menu_help.add_command(label=lang['gui']['menubar.help.version'], command=version)

window.config(menu=menubar)
def generate_question():
    # 出题

    # 这些变量在外面 所以需要使用global
    global float_number, random_int_list, factor
    factor = random.choice(random_int_list)

    question.set(lang['gui']['text.question'].format(factor))

    # 由于Python在浮点计算时会有精度问题
    # 而本程序的出题范围均在两位小数以内
    # 因此这里使用round函数避免问题
    # 此解决方案以后可能会修改，因为不是最佳方案
    float_number = round(factor * pi, 4)

def check_answer():
    # 当用户点击提交后的操作
    global score, pi_answer
    if cheat or pi_answer.get() == str(float_number):
        score += 1
        window.title(lang['gui']['title.2'].format(score))
        msgbox.showinfo(lang['message']['right']['msg1.title'], lang['message']['right']['msg1.text'].format(score))
        msgbox.showinfo(lang['message']['right']['msg2.title'], lang['message']['right']['msg2.text'])
    else:
        if (pi_answer.get() == ''):
            msgbox.showwarning(lang['message']['wrong']['msg3.title'], lang['message']['wrong']['msg3.text'])
        score -= 1
        window.title(lang['gui']['title.2'].format(score))
        msgbox.showerror(lang['message']['wrong']['msg4.title'].format(factor), lang['message']['wrong']['msg4.text'].format(float_number, score))
        msgbox.showerror(lang['message']['wrong']['msg5.title'], lang['message']['wrong']['msg5.text'].format(float_number))
    generate_question()

title = Label(text=lang['gui']['title.1'], font=('微软雅黑', 40))
title.grid(row=1, column=1, padx=15, pady=15)
question_label = Label(textvariable=question, font=('等线', 20))
question_label.grid(row=2, column=1, padx=15, pady=15)
button_finish = Button(text=lang['gui']['button.i_finish'], command=check_answer, width=43)
button_finish.grid(row=4, column=1, padx=15, pady=15)
pi_answer = Entry(width=30, font=('Comic Sans MS', 12)) # 答案输入框
pi_answer.grid(row=3, column=1, padx=15, pady=15)

# 开始时需初始化，生成一次问题
generate_question()

sha1 = hashlib.sha1(settings['secret_setting']['password'].encode('utf-8')).hexdigest()
if settings['secret_setting']['enabled'] and sha1 == '801c9aaf56fa2e0de84b40967625157a120cb5c7':
    cheat = True
    msgbox.showinfo('你发现了神奇的入口 You found the magic entrance!', '哇。看看那是什么！你打开了作弊模式？天哪！！\nWow. Look what that is! You turned on cheating mode? My God?')

window.mainloop()
