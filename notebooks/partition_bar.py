
# -*- coding: UTF-8 -*-
from cgitb import handler
from common import * 
import numpy as np 

## data 
feature_lens = [countmin, nitro, unimon, load_balancer]
legend_label = ['Data Structure Operation','Packet Processing']
styles = get_default_bar_style_sheets()

data = [0.8977, 0.8185, 0.9128, 0.7069]
remaining = []


# 设置数据
labels = feature_lens

fig_config = {
    'xlabel' : 'Different applications',   #x轴标签名
    'ylabel' : '% execution time' , #y轴标签名
    # 'ylabel2' : 'Speedup',
    'bar_width' : 0.40, #每一根柱子的宽度
}

bar_config1 = {
    "matplot_config" : {
        #'color' : '#74A9D0', 
        'color' : barcolor[0], 
        'edgecolor' : linecolor[0],
        'linewidth' : 3, 
        'label' : 'eBPF',   #如果为一个数是全局的，否则每一个条上都标注
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
        'label' : 'LKM',   #如果为一个数是全局的，否则每一个条上都标注
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
        'label' : 'NOINV',   #如果为一个数是全局的，否则每一个条上都标注
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
        'label' : 'INV',   #如果为一个数是全局的，否则每一个条上都标注
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
        for i in data:
            remaining.append(1-i)

        x = np.arange(len(labels))  # the label locations
        width = fig_config['bar_width']
        
        fig, ax = plt.subplots()
        
        set_hatch(**bar_config2["hatch_config"])
        bar1 = ax.bar(x, data, width, **bar_config2["matplot_config"])
        set_hatch(**bar_config4["hatch_config"])
        bar2 = ax.bar(x, remaining, width,bottom=data, **bar_config4["matplot_config"])

        
        ax.set_ylim(0,1)
        ax.set_ylabel(fig_config['ylabel'],fontsize=27)
        ax.set_xlabel(fig_config['xlabel'],fontsize=27)
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend(legend_label)
        fig.tight_layout()
        fig.set_figheight(4)
        save_figure('partition_bar')
        plt.show()
    
if __name__ == '__main__': 
    draw()