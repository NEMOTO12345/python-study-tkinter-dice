import tkinter as tk
import tkinter.ttk as ttk
import dice

root = tk.Tk()



#タイトルバーを作る
root.title('サイコロゲーム')
#Windowサイズを設定
root.geometry('600x400') #xは半角英数字のエックス
#またはroot.minsize(400,300)と書いてもよい。
#ラベル(本文)
static1 = tk.Label(text='サイコロ対戦ゲーム')
static1.pack()

#　サイコロ選択
#セレクトボックス(コンボボックス)を作る
label = tk.Label(text='どのサイコロで勝負する？')
label.pack()
combo1 = ttk.Combobox(root, state='readonly')
# セレクトボックスの選択値を設定
combo1["values"] = ("4","6","8","12","20")
# デフォルトの値をA(index=0)に設定
combo1.current(0)
# コンボボックスの配置
combo1.pack()


# 回数
label = tk.Label(text='何回勝負する？')
label.pack()
combo2 = ttk.Combobox(root, state='readonly')
# セレクトボックスの選択値を設定
combo2["values"] = ("1","2","3")
# デフォルトの値をA(index=0)に設定
combo2.current(0)
# コンボボックスの配置
combo2.pack()



# 何回か？
entry1 = tk.Entry(width=40,justify=tk.CENTER)
entry1.pack()

# 判定
entry2 = tk.Entry(width=40,justify=tk.CENTER)
entry2.pack()

# 結果
entry3 = tk.Entry(width=40,justify=tk.CENTER)
entry3.pack()

cpu_point = tk.Text(width=10,height=2,)
user1_point = tk.Text(width=10,height=2)



def delete():
    cpu_point.delete('1.0', 'end')
    user1_point.delete('1.0', 'end')
    combo1.current(0)
    combo2.current(0)
    entry1.delete(0,tk.END)
    entry2.delete(0,tk.END)
    entry3.delete(0,tk.END)


def result():
    c = cpu_point.get('1.0', 'end -1c')
    cpu = 0
    user = 0
    u = user1_point.get('1.0', 'end -1c')
    for i in c:
        if i == '○':
            cpu += 1
        elif i == '●':
            cpu += -1
        else:
            cpu += 0
    for i in u:
        if i == '○':
            user += 1
        elif i == '●':
            user += -1
        else:
            user += 0
    cpu_point.delete('1.0', 'end')
    user1_point.delete('1.0', 'end')
    if user > cpu:
        user1_point.insert('1.0','勝利！！')
        cpu_point.insert('1.0','負け')
    elif user < cpu:
        user1_point.insert('1.0','負け')
        cpu_point.insert('1.0','勝利！！')
    else:
        user1_point.insert('1.0','引き分け')
        cpu_point.insert('1.0','引き分け')
    root.after(3000,delete)

# 勝負ボタン
button1 = tk.Button(text="勝負！！")
def get_value3():
    entry1.delete(0,tk.END)
    entry2.delete(0,tk.END)
    entry3.delete(0,tk.END)
    user_sai = combo1.get()
    round_num = combo2.get() 
    r = int(round_num)
    count = 3
    sai = dice.Dice(int(user_sai))
    entry1.delete(0,tk.END)
    entry1.insert(tk.END,f"第{count}回戦")
    cp_sai_num = sai.shot()
    user_sai_num = sai.shot()
    if cp_sai_num > user_sai_num:
        entry2.insert(tk.END,f'CP:{cp_sai_num},あなた:{user_sai_num}')
        entry3.insert(tk.END,"あなたの負け")
        user1_point.insert('2.0','●')
        cpu_point.insert('2.0','○')
    elif cp_sai_num < user_sai_num:
        entry2.insert(tk.END,f'CP:{cp_sai_num},あなた:{user_sai_num}')
        entry3.insert(tk.END,"あなたの勝ち")
        user1_point.insert('2.0','○')
        cpu_point.insert('2.0','●')
    elif cp_sai_num == user_sai_num:
        entry2.insert(tk.END,f'CP:{cp_sai_num},あなた:{user_sai_num}')
        entry3.insert(tk.END,"引き分け")
        user1_point.insert('2.0','-')
        cpu_point.insert('2.0','-')  
    root.after(3000,result)
    


def get_value2():
    entry1.delete(0,tk.END)
    entry2.delete(0,tk.END)
    entry3.delete(0,tk.END)
    user_sai = combo1.get()
    round_num = combo2.get() 
    r = int(round_num)
    count = 2
    sai = dice.Dice(int(user_sai))
    entry1.delete(0,tk.END)
    entry1.insert(tk.END,f"第{count}回戦")
    cp_sai_num = sai.shot()
    user_sai_num = sai.shot()
    if cp_sai_num > user_sai_num:
        entry2.insert(tk.END,f'CP:{cp_sai_num},あなた:{user_sai_num}')
        entry3.insert(tk.END,"あなたの負け")
        user1_point.insert('2.0','●')
        cpu_point.insert('2.0','○')
    elif cp_sai_num < user_sai_num:
        entry2.insert(tk.END,f'CP:{cp_sai_num},あなた:{user_sai_num}')
        entry3.insert(tk.END,"あなたの勝ち")
        user1_point.insert('2.0','○')
        cpu_point.insert('2.0','●')
    elif cp_sai_num == user_sai_num:
        entry2.insert(tk.END,f'CP:{cp_sai_num},あなた:{user_sai_num}')
        entry3.insert(tk.END,"引き分け")
        user1_point.insert('2.0','-')
        cpu_point.insert('2.0','-')  
    if r != count:
        root.after(3000,get_value3)
        user1_point.insert('2.0',' ')
        cpu_point.insert('2.0',' ')
    else:
        root.after(3000,result)
        



def get_value(event):
    user_sai = combo1.get()
    round_num = combo2.get()
    r = int(round_num)
    sai = dice.Dice(int(user_sai))
    entry1.delete(0,tk.END)
    entry1.insert(tk.END,f"第1回戦")
    cp_sai_num = sai.shot()
    user_sai_num = sai.shot()
    if cp_sai_num > user_sai_num:
        entry2.insert(tk.END,f'CP:{cp_sai_num},あなた:{user_sai_num}')
        entry3.insert(tk.END,"あなたの負け")
        user1_point.insert('2.0','●')
        cpu_point.insert('2.0','○')
    elif cp_sai_num < user_sai_num:
        entry2.insert(tk.END,f'CP:{cp_sai_num},あなた:{user_sai_num}')
        entry3.insert(tk.END,"あなたの勝ち")
        user1_point.insert('2.0','○')
        cpu_point.insert('2.0','●')
    elif cp_sai_num == user_sai_num:
        entry2.insert(tk.END,f'CP:{cp_sai_num},あなた:{user_sai_num}')
        entry3.insert(tk.END,"引き分け")
        user1_point.insert('2.0','-')
        cpu_point.insert('2.0','-')   
    if r != 1:
        root.after(3000,get_value2)
        user1_point.insert('2.0',' ')
        cpu_point.insert('2.0',' ')
    else:
        root.after(3000,result)




button1.bind('<Button-1>',get_value)
button1.pack()


cpu_label = tk.Label(text='CPU')
cpu_label.pack()
cpu_point.pack()

user_label = tk.Label(text='USER')
user_label.pack()
user1_point.pack()


root.mainloop()


# tkinterのTextウィジェットの使い方
# https://blog.narito.ninja/detail/100/