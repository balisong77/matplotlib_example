
# -*- coding: UTF-8 -*-
from cgitb import handler
from common import * 
import numpy as np 

## data 
feature_lens = ['NOINV-lookup', 'NOINV-update','INV-AC-0','INV-AC-1','INV-AC-2','INV-AC-3','INV-AC-4','INV-AC-5','INV-AS-0','INV-AS-1','INV-AS-2','INV-AS-3','INV-AS-4','INV-AS-5']

styles = get_default_bar_style_sheets()

data = [20,21,32,35,29,31,29,33,32,32,35,31,31,32]



# 设置数据
labels = feature_lens

fig_config = {
    'xlabel' : '',   #x轴标签名
    'ylabel' : 'Time (ns)' , #y轴标签名
    # 'ylabel2' : 'Speedup',
    'bar_width' : 0.50, #每一根柱子的宽度
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
        x = np.arange(len(labels))  # the label locations
        width = fig_config['bar_width']
        
        fig, ax = plt.subplots()
        
        set_hatch(**bar_config4["hatch_config"])
        bar1 = ax.bar(x, data, width, **bar_config4["matplot_config"])
        # set_hatch(**bar_config2["hatch_config"])
        # bar2 = ax.bar(x + cal_bar_offset(1, 4, width), y_2, width, **bar_config2["matplot_config"])
        # set_hatch(**bar_config3["hatch_config"])
        # bar3 = ax.bar(x + cal_bar_offset(2, 4, width), y_3, width, **bar_config3["matplot_config"])
        # set_hatch(**bar_config4["hatch_config"])
        # bar4 = ax.bar(x + cal_bar_offset(3, 4, width), y_4, width, **bar_config4["matplot_config"])
        
        # Add some text for labels, title and custom x-axis tick labels, etc.
        # ax.set_ylim(1, 1e12)
        # ax.set_yscale('log', base = 10, subs = [10])
        # ax.set_ylim(bottom=1e6)
        ax.set_ylabel(fig_config['ylabel'],fontsize=label_size)
        ax.set_xlabel(fig_config['xlabel'],fontsize=label_size)
        ax.set_xticks(x)
        ax.set_xticklabels(labels,rotation=45,fontsize=17)


        
        fig.tight_layout()
        fig.set_figheight(line_fig_height)

        save_figure('frame_bar')
        plt.show()
    
if __name__ == '__main__': 
    draw()