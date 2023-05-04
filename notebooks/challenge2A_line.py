
# -*- coding: UTF-8 -*-
from common import * 
import numpy as np 

## data 
# multicores
feature_nums = []
for i in range(1,41):
    feature_nums.append(i)
# exp_data
data = get_data("exp_cores.csv")

styles = get_default_line_style_sheets()

labels = feature_nums

x_ticks = list(range(len(labels)))


fig_config = {
    'ylabel' : y_label_cores,   #x轴标签名
    'xlabel' : x_label_cores , #y轴标签名
    'spine_config' : {
        "left" : ("data", 0),
        "right" : ("data", len(labels) - 1)
    }
}

line_config1 = {
    'matplot_config' : {
        'color' : linecolor[0], 
        'linewidth' : line_width, 
        'label' : ebpf,  
        'marker' : markers[0], 
        'markersize' : marker_size
    },
    'annotate_text_config' : {
        "color" : linecolor[0],
        "fontsize" : 30,
        "fontweight" : "bold",
        'ha' : 'center',
        'textcoords' : 'offset pixels',
        'xytext' : (0, 12),
        'family' : "Calibri"
        #"rotation" : 45
    }
}

line_config2= {
    'matplot_config' : {
        'color' : linecolor[1], 
        'linewidth' : line_width, 
        'label' : lkm,  
        'marker' : markers[1], 
        'markersize' : marker_size
    },
    'annotate_text_config' : {
        "color" : linecolor[1],
        "fontsize" : 30,
        "fontweight" : "bold",
        'ha' : 'center',
        'textcoords' : 'offset pixels',
        'xytext' : (0, -26),
        'family' : "Calibri"
        #"rotation" : 45
    }
}

start_line = {
    'matplot_config' : {
        'color' : 'grey', 
        'linewidth' : 2, 
        'linestyle' : '--'
    }
}
def draw(): 
    with plt.style.context(styles): 
        fig, ax = plt.subplots()
        ax.plot(x_ticks, data['cm-ebpf'], **line_config1["matplot_config"])
        ax.plot(x_ticks, data['cm-LKM'], **line_config2["matplot_config"])
        # ax.plot(x_ticks, y_3, **line_config3["matplot_config"])

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_xlabel(fig_config['xlabel'],fontsize=label_size)
        ax.set_ylabel(fig_config['ylabel'],fontsize=27)

        ax.set_xticks(x_ticks)
        ax.set_xlim(0, len(labels) -1)  #设置 x轴范围
        ax.set_xticklabels(labels)

        # ax.set_yticklabels(fontsize=tick_size)

        #设置x轴刻度间隔
        for i, tick in enumerate(ax.get_xaxis().get_ticklabels()):
            if i == 0:
                tick.set_visible(True)
            elif (i+1) % 5 != 0:
                tick.set_visible(False)

        ax.set_ylim(0, 125)
        # ax.set_yscale('log', base = 10, subs = [10])

        #设置纵坐标轴
        ax.spines['left'].set_position(fig_config["spine_config"]["left"])
        ax.spines['right'].set_position(fig_config["spine_config"]["right"])

        ax.legend(prop={'size': legend_size})

        fig.tight_layout()
        fig.set_figheight(line_fig_height)
        save_figure('challenge2A_line')
        plt.show()
    
if __name__ == '__main__': 
    draw()