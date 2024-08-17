import wind_met
import getdata
import corr_cal
from xpinyin import Pinyin
import pandas as pd
import warnings
import tkinter as tk
warnings.filterwarnings('ignore')
#%%
# 创建Tkinter窗口
window = tk.Tk()
window.title("天气农业系统")
window.geometry('500x200')
def go():
    Fruit_name = entry1.get()    #获取文本输入框的内容
    Fruit_city = entry2.get()
    City_name = entry3.get()
    #城市-水果键值对x
    City_Fruits = {Fruit_name:Fruit_city}
    year = '2022'
    city_name = City_name
    p = Pinyin ()
    city_name_fruit = p.get_pinyin(City_Fruits[Fruit_name],'')
    city = p.get_pinyin(city_name,'')
    #%%获取数据
    getdata.get_data(year, Fruit_city)
    getdata.get_data(year, city_name)
    try:
    # 可能会抛出异常的代码
        data_wind = getdata.get_wind_data(city)
        data_wind_fruit = getdata.get_wind_data(city_name_fruit)
    except ZeroDivisionError:
        # 忽略异常并继续执行
        pass
    # 程序将继续执行
    print("程序继续执行")
    #%%计算气温相关性
    Mete_goal_yt,Mete_sample_yt = corr_cal.get_data(City_name,City_Fruits,Fruit_name)
    Tem_min_rho ,Tem_max_rho ,Tem_mean_rho,Mete_goal_yt,Mete_sample_yt = corr_cal.corr(Mete_goal_yt,Mete_sample_yt)
    corr_cal.plot_line(Mete_goal_yt,Mete_sample_yt,City_name,City_Fruits,Fruit_name)
    corr_data = pd.DataFrame(columns = ['Tem_min_r','Tem_max_r','Tem_ave_r','result'],index=range(1))
    corr_data['Tem_min_r'][0] = Tem_min_rho
    corr_data['Tem_max_r'][0] = Tem_max_rho
    corr_data['Tem_ave_r'][0] = Tem_mean_rho
    if Tem_min_rho>0.95 and Tem_max_rho>0.95 and Tem_mean_rho>0.95:
        corr_data['result'][0] = '若只考虑气候因素，' +City_name+ '极大可能适合种植'+Fruit_name
    else:
        corr_data['result'][0] = '若只考虑气候因素，' +City_name+ '适合种植'+Fruit_name+'的可能性很小，需要投入更多的人为因素才能实现'
    print(corr_data.to_markdown())
    #%%展示风力、天气
    #data_wind:需要计算气候相似性的城市风、天气数据
    #data_wind_fruit:样本城市(诸城、东明、苍溪)风、天气数据
    wind_met.plot_wind_met(data_wind, data_wind_fruit, city_name, City_Fruits[Fruit_name])
    print(Fruit_name,Fruit_city,City_name)  # 获取文本框的内容打印
#创建单行可输入文本框
#输入命令提示
label_1 = tk.Label(window, text='输入优势水果：')
label_1.pack()
#在标题下方添加一个输入框
entry1 = tk.Entry(window)
entry1.pack()
#输入命令提示
label_2 = tk.Label(window, text='输入水果的优势产区：')
label_2.pack()
#在标题下方添加一个输入框
entry2 = tk.Entry(window)
entry2.pack()
#输入命令提示
label_3 = tk.Label(window, text='输入需要判断气候相似度的城市：')
label_3.pack()
#在标题下方添加一个输入框
entry3 = tk.Entry(window)
entry3.pack()
#创建Button按键
frequency = tk.Button(window, text='确认',command=go)     # 输入次数信息的Entry控件
frequency.pack()
# 启动Tkinter主事件循环
window.mainloop()

warnings.filterwarnings("ignore")
"""#%%主程序
Fruit_name = input('请输入目标水果：')
Fruit_city = input('请输入目标水果优势产区：')
City_name = input('请输入需要计算气候相似性的城市名称：')"""
