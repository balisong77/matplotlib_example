
# -*- coding: UTF-8 -*-
from cgitb import handler
from common import * 
import numpy as np 

## data 
# feature_lens = [countmin_ebpf,countmin_lkm,
#                 unimon_ebpf,unimon_lkm,unimon_noinv,unimon_inv,
#                 nitro_ebpf,nitro_lkm,nitro_noinv,nitro_inv]

feature_lens = [countmin, unimon, nitro]

styles = get_default_bar_style_sheets()

# 选1核时测得的数据,pkt/s
data = get_data("exp_single_core.csv")


# EBPF = [data["cm-ebpf"][0], data["unimon-ebpf"][0], data["nitro-ebpf"][0]]
# LKM = [data["cm-LKM"][0], data["unimon-LKM"][0], data["nitro-LKM"][0]]
# NOINV = [0, data["unimon-noinv"][0], data["nitro-noinv"][0]]
# INV = [0, data["unimon-inv"][0], data["nitro-inv"][0]]
EBPF = [data["cm-ebpf"][0], data["unimon-ebpf"][0], data["nitro-ebpf"][0]]
LKM = [data["cm-LKM"][0], data["unimon-LKM"][0], data["nitro-LKM"][0]]
NOINV = [0, data["unimon-noinv"][0], data["nitro-noinv"][0]]
INV = [0, data["unimon-inv"][0], data["nitro-inv"][0]]

# total_data = [data["cm-ebpf"][0], data["cm-LKM"][0],
#               data["unimon-ebpf"][0], data["unimon-LKM"][0], data["unimon-noinv"][0], data["unimon-inv"][0],
#               data["nitro-ebpf"][0], data["nitro-LKM"][0], data["nitro-noinv"][0], data["nitro-inv"][0]
#               ]

# total_data = [3.11,5.05,1.88,3.70,3.31,4.76,9.01,6.62,3.10,6.58]

# for i in range(len(total_data)):
#     total_data[i] = 1e9 / total_data[i] / 1e6

# 设置数据
labels = feature_lens


fig_config = {
    'xlabel' : '',   #x轴标签名
    'ylabel' : y_label_cores , #y轴标签名
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
        'hatch' : 'x'
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
        'label' : lkm,   #如果为一个数是全局的，否则每一个条上都标注
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
        'label' : inv,   #如果为一个数是全局的，否则每一个条上都标注
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



def draw(): 
    with plt.style.context(styles): 
        x = np.arange(len(labels))  # the label locations
        width = fig_config['bar_width']
        
        fig, ax = plt.subplots()
        
        set_hatch(**bar_config1["hatch_config"])
        set_hatch(**bar_config2["hatch_config"])
        set_hatch(**bar_config3["hatch_config"])
        set_hatch(**bar_config4["hatch_config"])
        bar1 = ax.bar(x + cal_bar_offset(0, 4, width), EBPF, width, **bar_config1["matplot_config"])
        bar2 = ax.bar(x + cal_bar_offset(1, 4, width), LKM, width, **bar_config2["matplot_config"])
        bar3 = ax.bar(x + cal_bar_offset(2, 4, width), NOINV, width, **bar_config3["matplot_config"])
        bar4 = ax.bar(x + cal_bar_offset(3, 4, width), INV, width, **bar_config4["matplot_config"])

        # Add some text for labels, title and custom x-axis tick labels, etc.
        #ax.set_ylim(1, 1e12)
        # ax.set_yscale('log', base = 10, subs = [10])
        # ax.set_ylim(bottom=1e6)
        ax.set_xlabel(fig_config['xlabel'],fontsize=label_size)
        ax.set_ylabel(fig_config['ylabel'],fontsize=23)

        ax.set_xticks(x)
        ax.set_xticklabels(labels,fontsize=25)



        # ax2 = ax.twinx()
        # line1 = ax2.plot(x + cal_bar_offset(1, 3, width), l_1, **line_config1["matplot_config"])
        # line2 = ax2.plot(x + cal_bar_offset(2, 3, width), l_2, **line_config2["matplot_config"])
        
        # ax2.set_ylim(0, 125)
        # ax2.set_yscale('log', base = 10, subs = [10])
        # ax2.set_ylabel(fig_config['ylabel2'])

        # ax2.grid(False)
        
        # lines = line1 + line2

        bars = [bar1, bar2, bar3, bar4]
        
        # #在一个图层上展示 图例
        # #分开zhanshi 
        
        # l2 = plt.legend(lines, [l.get_label() for l in lines],loc = "upper right", framealpha = 0.6)
        # plt.gca().add_artist(l1)
        l1 = plt.legend(bars, [b.get_label() for b in bars], loc = "upper left", framealpha = 0.6, prop={'size': legend_size})
        fig.tight_layout()

        fig.set_figheight(4)
        # fig.set_figheight(line_fig_height)
        save_figure('total_bar')
        plt.show()
    
if __name__ == '__main__': 
    draw()