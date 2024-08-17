import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%读取数据函数
def get_data(City_name,City_Fruits,Fruit_name):
    #读取目标城市的气象数据
    Mete_goal = pd.read_csv(City_name + '2022.csv')
    Mete_goal. drop (columns= Mete_goal.columns [0], axis= 1 , inplace= True )
    #读取产业园的气象数据
    Mete_cal = pd.read_csv(City_Fruits[Fruit_name] + '2022.csv')
    Mete_cal. drop (columns= Mete_cal.columns [0], axis= 1 , inplace= True )

    return Mete_goal,Mete_cal
#%%提取计算相关性的数据
def corr(Mete_goal,Mete_sample):
    Mete_goal['Tem_min_goal'] = 0
    Mete_goal['Tem_max_goal'] = 0
    Mete_goal['Tem_mean_goal'] = 0
    Mete_sample['Tem_min_sample'] = 0
    Mete_sample['Tem_max_sample'] = 0
    Mete_sample['Tem_mean_sample'] = 0
    for i in range(len(Mete_goal)):    
        Mete_goal['Tem_min_goal'][i] =int(Mete_goal['最低温度'][i].split('℃')[0])
        Mete_goal['Tem_max_goal'][i] =int(Mete_goal['最高温度'][i].split('℃')[0])
        Mete_goal['Tem_mean_goal'][i] = 0.5*(Mete_goal['Tem_min_goal'][i] + Mete_goal['Tem_max_goal'][i])
    for i in range(len(Mete_sample)):    
        Mete_sample['Tem_min_sample'][i] =int(Mete_sample['最低温度'][i].split('℃')[0])
        Mete_sample['Tem_max_sample'][i ] =int(Mete_sample['最高温度'][i].split('℃')[0])   
        Mete_sample['Tem_mean_sample'][i] = 0.5*(Mete_sample['Tem_min_sample'][i] + Mete_sample['Tem_max_sample'][i])
    
    Tem_min_rho = np.corrcoef( Mete_goal['Tem_min_goal'], Mete_sample['Tem_min_sample'])[0,1]
    Tem_max_rho = np.corrcoef( Mete_goal['Tem_max_goal'], Mete_sample['Tem_max_sample'])[0,1]
    Tem_mean_rho = np.corrcoef( Mete_goal['Tem_mean_goal'], Mete_sample['Tem_mean_sample'])[0,1]
    #print('最低温度相关性:'+str(Tem_min_rho))
    #print('最高温度相关性:'+str(Tem_max_rho))
    #print('平均温度相关性:'+str(Tem_mean_rho))
    
    return Tem_min_rho,Tem_max_rho,Tem_mean_rho,Mete_goal,Mete_sample
#%%折线图
def plot_line(Mete_goal,Mete_sample,City_name,City_Fruits,Fruit_name):
    plt.rcParams['font.sans-serif']=['SimHei']#用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False#用来正常显示负号
    Date_list = pd.date_range(start="20220101", end="20221231", freq="D")
    #最低气温
    plt.figure(dpi=300,figsize=(7,9))
    plt.subplot(3,1,1)
    plt.plot(Date_list, 
             Mete_goal['Tem_min_goal'], 
             'b', 
             alpha=0.5, 
             linewidth=1, 
             label=City_name)
    plt.plot(Date_list, 
             Mete_sample['Tem_min_sample'], 
             'r', 
             alpha=0.5, 
             linewidth=1, 
             label=City_Fruits[Fruit_name])
    plt.legend()
    plt.xlabel('日期')
    plt.ylabel('最低温度(℃)')
    #最高气温
    plt.subplot(3,1,2)
    plt.plot(Date_list, 
             Mete_goal['Tem_max_goal'], 
             'b', 
             alpha=0.5, 
             linewidth=1, 
             label=City_name)
    plt.plot(Date_list, 
             Mete_sample['Tem_max_sample'], 
             'r', 
             alpha=0.5, 
             linewidth=1, 
             label=City_Fruits[Fruit_name])
    plt.legend()
    plt.xlabel('日期')
    plt.ylabel('最高温度(℃)')
    #平均气温
    plt.subplot(3,1,3)
    plt.plot(Date_list, 
             Mete_goal['Tem_mean_goal'], 
             'b', 
             alpha=0.5, 
             linewidth=1, 
             label=City_name)
    plt.plot(Date_list, 
             Mete_sample['Tem_mean_sample'], 
             'r', 
             alpha=0.5, 
             linewidth=1, 
             label=City_Fruits[Fruit_name])
    plt.legend()
    plt.xlabel('日期')
    plt.ylabel('平均温度(℃)')
    plt.savefig(City_name + '温度(℃).png' )
    plt.show()



