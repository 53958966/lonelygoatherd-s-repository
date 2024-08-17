#%%引用自定义函数

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt   

def plot_wind_met(data_wind, data_wind_fruit, city_name, city_name_fruit):   
    n = 10     
    plt.rcParams['font.sans-serif'] = ['SimHei']
    fig = plt.figure(dpi=300,figsize=(12,8))
    #%%风向条形图
    plt.subplot(3,2,1)
    plt.bar(data_wind['风向'][0:n], np.array(data_wind['风向天数'][0:n]))
    plt.xticks(data_wind['风向'][0:n], data_wind['风向'][0:n], rotation=90)
    plt.xlabel('风向')
    plt.ylabel('天数')
    plt.title(city_name)
    plt.subplot(3,2,2)
    plt.bar(data_wind_fruit['风向'][0:n], np.array(data_wind_fruit['风向天数'][0:n]))
    plt.xticks(data_wind_fruit['风向'][0:n], data_wind_fruit['风向'][0:n], rotation=90)
    plt.xlabel('风向')
    plt.ylabel('天数')
    plt.title(city_name_fruit)
    #%%风速条形图
    plt.subplot(3,2,3)
    plt.bar(data_wind['风力'][0:n], np.array(data_wind['风力天数'][0:n]),color = 'red')
    plt.xticks(data_wind['风力'][0:n], data_wind['风力'][0:n], rotation=90)
    plt.xlabel('风力')
    plt.ylabel('天数')
    plt.title(city_name)
    plt.subplot(3,2,4)
    plt.bar(data_wind_fruit['风力'][0:n], np.array(data_wind_fruit['风力天数'][0:n]),color = 'red')
    plt.xticks(data_wind_fruit['风力'][0:n], data_wind_fruit['风力'][0:n], rotation=90)
    plt.xlabel('风力')
    plt.ylabel('天数')
    plt.title(city_name_fruit)

    #%%天气图
    met = pd.DataFrame(columns = [city_name, city_name_fruit],
                       index = ['晴','多云','阴','雨','雪','沙尘'])
    for i in range(len(met.index)):
        if len(data_wind[data_wind['天气'] == met.index[i]]) == 0:
            met.loc[met.index[i],city_name] = 0
        else:
            a = data_wind[data_wind['天气'] == met.index[i]].index[0]
            met.loc[met.index[i],city_name] = data_wind.loc[a,'天气天数']
        if len(data_wind_fruit[data_wind_fruit['天气'] == met.index[i]]) == 0:
            met.loc[met.index[i],city_name_fruit] = 0
        else:    
            b = data_wind_fruit[data_wind_fruit['天气'] == met.index[i]].index[0]
            met.loc[met.index[i],city_name_fruit] = data_wind_fruit.loc[b,'天气天数']
        
    plt.subplot2grid((3, 2), (2, 0), colspan=2)
    bar_width = 0.35
    x = np.arange(len(met))  
    plt.bar(x, met[city_name]
            , bar_width, align='center', color='#66c2a5', label=city_name)
    plt.bar(x+bar_width, met[city_name_fruit]
            , bar_width, align='center', color='#8da0cb', label=city_name_fruit)
    plt.xlabel('天气')
    plt.ylabel('天数')
    plt.xticks(x+bar_width/2, met.index)
    plt.legend()
    fig.subplots_adjust(left=0,right=1,top=1,bottom=0,
                        wspace=0.2,hspace=0.8)
    plt.savefig(city_name + city_name_fruit + '.png',bbox_inches = 'tight')
    plt.show()


