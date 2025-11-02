import tkinter as tk
import random
import time

#多样化文本内容
messages = [
    '瑶瑶过的开心吗？','瑶瑶多喝水哦','瑶瑶今天天气很好','瑶瑶多晒晒太阳','瑶瑶多微笑要自信','瑶瑶你超棒的','愿你今晚有个好梦',
    '瑶瑶要多吃水果','瑶瑶早点休息哦！','午饭要记得吃','我爱你瑶瑶','瑶瑶早点休息','想你了瑶瑶','瑶瑶好好爱自己'
]

#随机颜色生成
def get_random_color():
    colors = ['pink','lightblue','lightgreen','lightyellow','lavender','mistyrose','paleturquoise','peachpuff']
    return random.choice(colors)


def create_float_window(root):
    #创建顶级窗口，制定主窗口为父级
    window = tk.Toplevel(root)

    #获取屏幕尺寸
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()


    #随机初始位置
    x = random.randrange(0, width - 200)
    y = random.randrange(0, height - 100)
    window.geometry(f"+{x}+{y}")

    message = random.choice(messages)
    color = get_random_color()

    tk.Label(window,
             text=message,
             bg=color,
             font=('楷体',18),
             width=20,
             height=4).pack()

def create_windows_periodically(root,count=100,delay=50):
    if count>0:
        create_float_window(root)
        #递归调用，每隔delay毫秒创建一个新窗口
        root.after(delay,create_windows_periodically,root,count - 1,delay)

if __name__ == "__main__":
    #创建窗口（隐藏）
    root = tk.Tk()
    root.title("瑶瑶")
    root.withdraw()

    #开始创建浮动窗口
    create_windows_periodically(root,200,70)

    #启动住时间循环必须在主线程
    root.mainloop()