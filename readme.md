# 圆周率终结者的介绍文档

欢迎使用圆周率终结者这款程序！

使用它，你可以：

- 快速记下 n 倍圆周率；
- ~~当作娱乐工具；~~
- 让你在计算圆的面积、体积是得心应手，省时省力。

当然，如果你愿意，它能做的，不止这些，你可以自行想象。

## 关于圆

---

我们在小学六年级上册会学到圆，圆的面积，圆的周长。

对于公式的具体推导过程，这里不再演示，你可以自行了解或在六年级上册的数学书中查看过程。

> 圆的周长公式为：`pi * d`
> 如果只有半径，则为：`2 * pi * r`
> 圆的面积公式为：`pi * r²`
> 如果只有直径，则为：`pi * (d / 2)²`

但，由于 pi 取 3.14 的原因，我们很难直接口算出结果。像是 `3.14 * 1` 还好，但如果是 `3.14 * 5` 呢？ `3.14 * 21` 呢？我们都不能口算出结果。

因此，这款软件应运而生了。

## 本软件使用教程

---

> *以下内容撰写于这个软件的 1.0.4版本，使用简体中文语言。*

打开目录后，你肯定就懵了，这都啥啊这是，看不懂。

别慌，我们只用打开一个就行了。

运行 `圆周率终结者.exe` 就好啦。打开后现在你应该会看到如下界面：

![主界面](https://s2.loli.net/2021/12/24/yEqencO59gPiU8G.png)

这便是他的主界面了。顾名思义，中间的就是题目，你只需要填入答案便可。

![答对后](https://s2.loli.net/2021/12/24/JBMIHmjxk8AdZgL.png)

当你答对了之后，会弹出如下框，并加一分。分数可以在点击了确定后标题栏中查看。

![答错了](https://s2.loli.net/2021/12/24/OMcJq8WFLfRuEIK.png)

若你答错了，则会减一分。此时，分数已经显示了。

上方的菜单栏也可以点击。点击后分别有两个选项。

每个选项的效果如下：

| 名字   | 作用                   |
| ------ | ---------------------- |
| 关于   | 关于本程序的信息       |
| 版本号 | 查看本程序目前的版本号 |

## 修改设置文件

---

如果你不想深入的玩儿这个程序，以下内容不用看了。

**Note**: If you are a foreign user, you might as well read it with the help of translation software. (however, will the software I make be used by foreigners??)

也许你看到了，程序目录中的一堆文件中有一个 `settings.json`。这是本程序的设置文件（我自己建的）。作者实在是懒得做设置页面了，就凑合着用吧。打开后，你能看到：

```json
{
    "language_file": "language-zh-cn.json",

    "secret_setting": {
        "enabled": false,
        "password": ""
    }
}
```

解释一下：

| 名字                | 作用                                         |
| ------------------- | -------------------------------------------- |
| `"language_file"` | 设置语言文件，关于什么是语言文件，后面会讲。 |

## 修改语言文件

---

语言文件是可以让软件改变显示文本的东西，作者内置了三种语言。

语言文件的目录是主程序下面的第一个文件夹，也就是那个 `pi_terminator\languages`。

做这个功能，其实豆沙包也不知道有啥用，就是图一乐……

内置的语言文件如下：

| 文件名                        | 语言                 |
| ----------------------------- | -------------------- |
| `language-en-us.json`       | 英文                 |
| `language-zh-cn.json`       | 中文                 |
| `language-heaven-meme.json` | 作者恶搞的中文，慎用 |

你喜欢哪个语言文件，就在 `settings.json` 里把 `language_file` 改成文件名就行。。比如 `language-zh-cn.json`。

# 结尾

就到这里啦，有问题可以咨询豆沙包。

—— Doushabao 2021/12/04
