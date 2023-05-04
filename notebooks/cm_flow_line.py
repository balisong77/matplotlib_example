
# -*- coding: UTF-8 -*-
from common import * 
import numpy as np 

## data 
# multiflows
feature_nums = []
for i in range(0,11):
    feature_nums.append(2**i)
# throughput
data = get_data("exp_flows.csv")

core_num = 20
opverhead = 20
optimal = []
#i+1 是核数
for i in range(len(data['cm-LKM'])):
    total_throughput = data['cm-LKM'][i]
    pps = total_throughput / core_num
    duration = 1e9/pps/1e6
    optimal_duration = duration - opverhead
    optimal_pps = 1e9/optimal_duration/1e6
    optimal_throughput = optimal_pps * core_num
    optimal.append(optimal_throughput)

styles = get_default_line_style_sheets()

labels = feature_nums

x_ticks = list(range(len(labels)))


fig_config = {
    'ylabel' : y_label_flows,   #y轴标签名
    'xlabel' : x_label_flows , #x轴标签名
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
        ax.plot(x_ticks, data['cm-ebpf'], **line_config1["matplot_config"])
        ax.plot(x_ticks, data['cm-LKM'], **line_config2["matplot_config"])
        ax.plot(x_ticks, optimal, **line_config6["matplot_config"])

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_xlabel(fig_config['xlabel'],fontsize=label_size)
        ax.set_ylabel(fig_config['ylabel'],fontsize=27)

        ax.set_xticks(x_ticks)
        ax.set_xlim(0, len(labels) -1)  #设置 x轴范围
        ax.set_xticklabels(labels)
        
        ax.set_ylim(0, 150)
        # ax.set_yscale('log', base = 10, subs = [10])

        #设置纵坐标轴
        ax.spines['left'].set_position(fig_config["spine_config"]["left"])
        ax.spines['right'].set_position(fig_config["spine_config"]["right"])

        ax.legend(prop={'size': legend_size})
        
        
        #ax.bar_label(rects1, padding=3)
        #ax.bar_label(rects2, padding=3)

        fig.tight_layout()
        fig.set_figheight(line_fig_height)
        save_figure('cm_flow_line')
        plt.show()
    
if __name__ == '__main__': 
    draw()