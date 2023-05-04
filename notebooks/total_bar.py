
# -*- coding: UTF-8 -*-
from cgitb import handler
from common import * 
import numpy as np 

## data 
feature_lens = [countmin_ebpf,countmin_lkm,
                unimon_ebpf,unimon_lkm,unimon_noinv,unimon_inv,
                nitro_ebpf,nitro_lkm,nitro_noinv,nitro_inv]

styles = get_default_bar_style_sheets()

# 选1核时测得的数据,pkt/s
data = get_data("exp_cores_pps.csv")


EBPF = [data["cm-ebpf"][0], data["unimon-ebpf"][0], data["nitro-ebpf"][0]]
LKM = [data["cm-LKM"][0], data["unimon-LKM"][0], data["nitro-LKM"][0]]
NOINV = [0, data["unimon-noinv"][0], data["nitro-noinv"][0]]
INV = [0, data["unimon-inv"][0], data["nitro-inv"][0]]

# total_data = [data["cm-ebpf"][0], data["cm-LKM"][0],
#               data["unimon-ebpf"][0], data["unimon-LKM"][0], data["unimon-noinv"][0], data["unimon-inv"][0],
#               data["nitro-ebpf"][0], data["nitro-LKM"][0], data["nitro-noinv"][0], data["nitro-inv"][0]
#               ]

total_data = [331,212,513,277,310,339,221,112,163,153]

for i in range(len(total_data)):
    total_data[i] = 1e9 / total_data[i] / 1e6

# 设置数据
labels = feature_lens


fig_config = {
    'xlabel' : 'Sketch',   #x轴标签名
    'ylabel' : 'Mpkts/s' , #y轴标签名
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
        
        set_hatch(**bar_config2["hatch_config"])
        bar1 = ax.bar(x, total_data, width, **bar_config2["matplot_config"])

        # Add some text for labels, title and custom x-axis tick labels, etc.
        #ax.set_ylim(1, 1e12)
        # ax.set_yscale('log', base = 10, subs = [10])
        # ax.set_ylim(bottom=1e6)
        ax.set_ylabel(fig_config['ylabel'])
        ax.set_xlabel(fig_config['xlabel'])
        ax.set_xticks(x)
        ax.set_xticklabels(labels,rotation=45,fontsize=15)



        # ax2 = ax.twinx()
        # line1 = ax2.plot(x + cal_bar_offset(1, 3, width), l_1, **line_config1["matplot_config"])
        # line2 = ax2.plot(x + cal_bar_offset(2, 3, width), l_2, **line_config2["matplot_config"])
        
        # ax2.set_ylim(1, 1000)
        # ax2.set_yscale('log', base = 10, subs = [10])
        # ax2.set_ylabel(fig_config['ylabel2'])

        # ax2.grid(False)
        
        # lines = line1 + line2

        
        
        # #在一个图层上展示 图例
        # #分开zhanshi 
        
        # l2 = plt.legend(lines, [l.get_label() for l in lines],loc = "upper right", framealpha = 0.6)
        # plt.gca().add_artist(l1)
        
        fig.tight_layout()

        save_figure('total_bar')
        plt.show()
    
if __name__ == '__main__': 
    draw()