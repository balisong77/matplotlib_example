
# -*- coding: UTF-8 -*-
from cgitb import handler
from common import * 
import numpy as np 

## data 
# feature_lens = ['cm-LKM','unimon-LKM','unimon-noinv','unimon-inv','nitro-LKM','nitro-noinv','nitro-inv','concurrent-array','lpm']
feature_lens = [countmin_lkm,
                unimon_lkm,unimon_noinv,unimon_inv,
                nitro_lkm,nitro_noinv,nitro_inv,
                carray, lpm]
legend_label = ['Processing','Overhead']
styles = get_default_bar_style_sheets()

total = [212,277,310,339,112,163,153,110,290]
op = [20,20,40,50,20,20,50,20,20]
y_tick = []
total_partition = []
op_partition = []

for i in range(len(total)):
    total_partition.append(float(total[i]) /float(total[i]+op[i]))
for i in range(len(total)):
    op_partition.append(1-total_partition[i])


remaining = []


# 设置数据
labels = feature_lens

fig_config = {
    'xlabel' : '',   #x轴标签名
    'ylabel' : '% execution time' , #y轴标签名
    # 'ylabel2' : 'Speedup',
    'bar_width' : 0.20, #每一根柱子的宽度
}

bar_config1 = {
    "matplot_config" : {
        #'color' : '#74A9D0', 
        'color' : barcolor[0], 
        'edgecolor' : linecolor[0],
        'linewidth' : 3, 
        'label' : ebpf,   #如果为一个数是全局的，否则每一个条上都标注
        #tick_label : str or list of str, optional 设置是否在条上标注
        #xerr, yerrfloat or array-like of shape(N,) or shape(2, N), optional
        #ecolorc olor or list of color, default: 'black'
        'hatch' : '/'
    },
    "hatch_config" : {
        'color' : linecolor[0],
        'linewidth' : 2
    }
}

bar_config2 = {
    "matplot_config" : {
        #'color' : '#A1BA66', 
        'color' : barcolor[1],
        'edgecolor' : linecolor[1],
        'linewidth' : 3, 
        'label' : 'Data Struct',   #如果为一个数是全局的，否则每一个条上都标注
        #tick_label : str or list of str, optional 
        #xerr, yerrfloat or array-like of shape(N,) or shape(2, N), optional
        #ecolorc olor or list of color, default: 'black'
        'hatch' : 'x'
    },
    "hatch_config" : {
        'color' : linecolor[1],
        'linewidth' : 2
    }
}

bar_config3 = {
    "matplot_config" : {
        #'color' : '#A1BA66', 
        'color' : barcolor[2],
        'edgecolor' : linecolor[2],
        'linewidth' : 3, 
        'label' : noinv,   #如果为一个数是全局的，否则每一个条上都标注
        #tick_label : str or list of str, optional 
        #xerr, yerrfloat or array-like of shape(N,) or shape(2, N), optional
        #ecolorc olor or list of color, default: 'black'
        'hatch' : 'x'
    },
    "hatch_config" : {
        'color' : linecolor[2],
        'linewidth' : 2
    }
}

bar_config4 = {
    "matplot_config" : {
        #'color' : '#A1BA66', 
        'color' : barcolor[3],
        'edgecolor' : linecolor[3],
        'linewidth' : 3, 
        'label' : 'Overhead',   #如果为一个数是全局的，否则每一个条上都标注
        #tick_label : str or list of str, optional 
        #xerr, yerrfloat or array-like of shape(N,) or shape(2, N), optional
        #ecolorc olor or list of color, default: 'black'
        'hatch' : 'x'
    },
    "hatch_config" : {
        'color' : linecolor[3],
        'linewidth' : 2
    }
}

line_config1 = {
    'matplot_config' : {
        'color' : linecolor[1], 
        'linewidth' : 3, 
        'label' : 'Speedup over MCA',  
        'marker' : markers[0], 
        'markersize' : marker_size,
        'linestyle' : '-'
    }
}

line_config2 = {
    'matplot_config' : {
        'color' : linecolor[2], 
        'linewidth' : 3, 
        'label' : 'Speedup over HF',  
        'marker' : markers[1], 
        'markersize' : marker_size,
        'linestyle' : '-'
    }
}


def draw(): 
    with plt.style.context(styles): 
        x = np.arange(len(labels))  # the label locations
        width = fig_config['bar_width']
        
        fig, ax = plt.subplots()
        
        set_hatch(**bar_config2["hatch_config"])
        bar1 = ax.bar(x, total_partition, width, **bar_config2["matplot_config"])
        set_hatch(**bar_config4["hatch_config"])
        bar2 = ax.bar(x, op_partition, width,bottom=total_partition, **bar_config4["matplot_config"])

        y_tick.append(0)
        for i in range(6):
            y_tick.append(0.2*i)
        ax.set_yticks(y_tick)
        # plt.tick_params(axis='y', labelsize=20)

        ax.set_ylim(0,1)

        ax.set_xlabel(fig_config['xlabel'],fontsize=label_size)
        ax.set_ylabel(fig_config['ylabel'],fontsize=25)
        
        ax.set_xticks(x)
        ax.set_xticklabels(labels,rotation=45,fontsize=17)

        ax.legend(prop={'size': legend_size})

        fig.tight_layout()
        fig.set_figheight(4)

        save_figure('op_partition_bar')
        plt.show()
    
if __name__ == '__main__': 
    draw()