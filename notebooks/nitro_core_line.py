
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

opverhead = 20
optimal = []
#i+1 是核数
for i in range(len(data['nitro-LKM'])):
    total_throughput = data['nitro-LKM'][i]
    pps = total_throughput / (i+1)
    duration = 1e9/pps/1e6
    optimal_duration = duration - opverhead
    optimal_pps = 1e9/optimal_duration/1e6
    optimal_throughput = optimal_pps * (i+1)
    optimal.append(optimal_throughput)

styles = get_default_line_style_sheets()

labels = feature_nums

x_ticks = list(range(len(feature_nums)))

# 数据过于密集，调小marksize
marker_size = 10

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

line_config2 = {
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
        'xytext' : (0, 12),
        'family' : "Calibri"
        #"rotation" : 45
    }
}

line_config3= {
    'matplot_config' : {
        'color' : linecolor[2], 
        'linewidth' : line_width, 
        'label' : noinv,  
        'marker' : markers[2], 
        'markersize' : marker_size
    },
    'annotate_text_config' : {
        "color" : linecolor[2],
        "fontsize" : 30,
        "fontweight" : "bold",
        'ha' : 'center',
        'textcoords' : 'offset pixels',
        'xytext' : (0, -26),
        'family' : "Calibri"
        #"rotation" : 45
    }
}

line_config4= {
    'matplot_config' : {
        'color' : linecolor[3], 
        'linewidth' : line_width, 
        'label' : inv,  
        'marker' : markers[3], 
        'markersize' : marker_size
    },
    'annotate_text_config' : {
        "color" : linecolor[3],
        "fontsize" : 30,
        "fontweight" : "bold",
        'ha' : 'center',
        'textcoords' : 'offset pixels',
        'xytext' : (0, -26),
        'family' : "Calibri"
        #"rotation" : 45
    }
}

line_config6= {
    'matplot_config' : {
        'color' : linecolor[5], 
        'linewidth' : line_width, 
        'label' : optimal_str,  
        'marker' : markers[5], 
        'markersize' : marker_size
    },
    'annotate_text_config' : {
        "color" : linecolor[5],
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
        ax.plot(x_ticks, data["nitro-ebpf"], **line_config1["matplot_config"])
        ax.plot(x_ticks, data["nitro-LKM"], **line_config2["matplot_config"])
        ax.plot(x_ticks, data["nitro-noinv"], **line_config3["matplot_config"])
        ax.plot(x_ticks, data["nitro-inv"], **line_config4["matplot_config"])
        ax.plot(x_ticks, optimal, **line_config6["matplot_config"])
        # ax.plot(x_ticks, y_3, **line_config3["matplot_config"])

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_xlabel(fig_config['xlabel'],fontsize=label_size)
        ax.set_ylabel(fig_config['ylabel'],fontsize=27)

        ax.set_xticks(x_ticks)
        ax.set_xlim(0, len(labels) -1)  #设置 x轴范围
        ax.set_xticklabels(labels)

        #设置x轴刻度间隔
        for i, tick in enumerate(ax.get_xaxis().get_ticklabels()):
            if i == 0:
                tick.set_visible(True)
            elif (i+1) % 5 != 0:
                tick.set_visible(False)

        ax.set_ylim(0, 210)
        # ax.set_yscale('log', base = 10, subs = [10])

        #设置纵坐标轴
        ax.spines['left'].set_position(fig_config["spine_config"]["left"])
        ax.spines['right'].set_position(fig_config["spine_config"]["right"])

        ax.legend(prop={'size': legend_size})
        
        
        #ax.bar_label(rects1, padding=3)
        #ax.bar_label(rects2, padding=3)

        fig.tight_layout()
        fig.set_figheight(line_fig_height)
        save_figure('nitro_core_line')
        plt.show()
    
if __name__ == '__main__': 
    draw()