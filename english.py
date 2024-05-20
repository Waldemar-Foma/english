from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Food&Health')
root.geometry("350x600")
root.attributes("-alpha", 0.9)
root["bg"] = "LightSteelBlue"

label = ttk.Label(text="Выбор диалога:",
                  foreground="black",
                  background="LightSteelBlue",
                  font="Arial 10 bold roman")
label.pack()


def click_1():
    window = Tk()
    window.title("table queen")
    window.geometry("700x200")
    window.attributes("-alpha", 0.9)
    window["bg"] = "LightSteelBlue"
    label = ttk.Label(window, text="-Have you noticed how John always takes forever to pick a table at restaurants?\n"
                                   "-Oh yeah, he's a real table queen, always wants the best spot.\n"
                                   "-It's kind of amusing, though. He treats it like a mission.\n"
                                   "-Definitely. But hey, at least we end up with a great table every time!\n"
                                   "-True, true. Can't argue with that.",
                      font="Arial 14 normal roman",
                      foreground="black",
                      background="LightSteelBlue")
    label.pack(anchor=CENTER, expand=1)


button1 = ttk.Button(root, text="table queen", command=click_1)
button1.pack(anchor="nw", padx=135, pady=30)


def click_2():
    window = Tk()
    window.title("biohacking")
    window.geometry("500x200")
    window.attributes("-alpha", 0.9)
    window["bg"] = "LightSteelBlue"
    label = ttk.Label(window, text="- Have you heard about biohacking before?\n"
                                   "- Yes, I read about it in a magazine recently.\n"
                                   "- What do you think about the concept?\n"
                                   "- It sounds intriguing, but also a bit controversial.\n"
                                   "- Definitely, biohacking opens up a whole new world\n"
                                   "of possibilities and ethical questions.",
                      font="Arial 14 normal roman",
                      foreground="black",
                      background="LightSteelBlue")
    label.pack(anchor=CENTER, expand=1)


button2 = ttk.Button(root, text="biohacking", command=click_2)
button2.pack(anchor="nw", padx=135, pady=30)


def click_3():
    window = Tk()
    window.title("lukewarm")
    window.geometry("450x200")
    window.attributes("-alpha", 0.9)
    window["bg"] = "LightSteelBlue"
    label = ttk.Label(window, text="- How was the soup you ordered?\n"
                                   "- It was lukewarm, not as hot as I expected.\n"
                                   "- Would you like me to heat it up for you?\n"
                                   "- No, thanks. I'll just have it as it is.\n"
                                   "- Alright, just let me know if you need anything else.",
                      font="Arial 14 normal roman",
                      foreground="black",
                      background="LightSteelBlue")
    label.pack(anchor=CENTER, expand=1)


button3 = ttk.Button(root, text="lukewarm", command=click_3)
button3.pack(anchor="nw", padx=135, pady=30)


def click_4():
    window = Tk()
    window.title("refrigerator rights")
    window.geometry("650x250")
    window.attributes("-alpha", 0.9)
    window["bg"] = "LightSteelBlue"
    label = ttk.Label(window, text="Why does Sarah always raid our refrigerator whenever she comes over?\n"
                                   "-Oh, she's got refrigerator rights.\n"
                                   "-Refrigerator rights?\n"
                                   "-Yeah, it means she's so close to us, she feels like our fridge is hers too.\n"
                                   "-I guess that's a sign of true friendship.\n"
                                   "-Definitely, it's like she's part of the family.\n"
                                   "-Well, at least we know what to expect when she visits.",
                      font="Arial 14 normal roman",
                      foreground="black",
                      background="LightSteelBlue")
    label.pack(anchor=CENTER, expand=1)


button4 = ttk.Button(root, text="refrigerator rights", command=click_4)
button4.pack(anchor="nw", padx=135, pady=30)


def click_5():
    window = Tk()
    window.title("takeaway food")
    window.geometry("650x200")
    window.attributes("-alpha", 0.9)
    window["bg"] = "LightSteelBlue"
    label = ttk.Label(window, text="-Hey, I'm starving. Do you want to grab something to eat?\n"
                                   "-Yeah, let's get some takeaway food. I'm in the mood for pizza.\n"
                                   "-Sounds good to me. Should we pick it up or have it delivered?\n"
                                   "-Let's just pick it up on the way home. I don't feel like waiting for delivery.\n"
                                   "-Alright, I'll place the order while you grab your coat.",
                      font="Arial 14 normal roman",
                      foreground="black",
                      background="LightSteelBlue")
    label.pack(anchor=CENTER, expand=1)


button5 = ttk.Button(root, text="takeaway food", command=click_5)
button5.pack(anchor="nw", padx=135, pady=30)

root.mainloop()
