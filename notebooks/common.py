# -*- coding: UTF-8 -*-
import os 
from matplotlib import pyplot as plt
import matplotlib as mpl
from matplotlib import axes
import pandas

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
STYLE_SHEET_DIR = os.path.join(ROOT_DIR, 'styles')
DEFAULT_SAVE_DIR = os.path.join(ROOT_DIR, 'images')

DEFAULT_BASE_STYLE = os.path.join(STYLE_SHEET_DIR, 'base.mplstyle')
DEFAULT_HEAP_MAP_STYLE = os.path.join(STYLE_SHEET_DIR, 'heapmap.mplstyle')
DEFAULT_BAR_STYLE = os.path.join(STYLE_SHEET_DIR, 'bargraph.mplstyle')
DEFAULT_LINE_STYLE = os.path.join(STYLE_SHEET_DIR, 'linegraph.mplstyle')

# 本次实验同一变量
markers = ['^', '*', 'o', 's', 'v', 'p']
# linecolor = ["green","blue","purple","orange", "brown"]
# barcolor = ["lightgreen","cornflowerblue","thistle","peachpuff"]
linecolor = ["green","blue","purple","orange", "brown", "olive"]
barcolor = ["lightgreen","cornflowerblue","thistle","peachpuff", "olivedrab"]
hatch_style = ['x', '+', '/', '-', 'o', 'O', '.', '*']
y_label_cores = "Packet rate (Mpkts/s)"
x_label_cores = "# CPU cores"
y_label_flows = "Packet rate (Mpkts/s)"
x_label_flows = "# Flows"
marker_size = 15
line_width = 3

label_size = 29
tick_size = 27

line_fig_height = 5

legend_size = 25

countmin = 'Count-Min'
nitro = 'Nitro Sketch'
unimon = 'UnivMon Sketch'
load_balancer = 'Load Balancer'

countmin_ebpf = 'Count-Min-eBPF'
countmin_lkm = 'Count-Min-BASE'

nitro_ebpf = 'Nitro-eBPF'
nitro_lkm = 'Nitro-BASE'
nitro_inv = 'Nitro-INV'
nitro_noinv = 'Nitro-NOINV'

unimon_ebpf = 'UnivMon-eBPF'
unimon_lkm = 'UnivMon-BASE'
unimon_inv = 'UnivMon-INV'
unimon_noinv = 'UnivMon-NOINV'

optimal_str = 'Optimal'

carray = 'Carray'
carray_ebpf = 'Carray-eBPF'
carray_hyper = 'Carray-HyperCom'

lpm = 'LPM'
lpm_ebpf = 'LPM-eBPF'
lpm_hyper = 'LPM-HyperCom'

ebpf = 'eBPF'
lkm = 'BASE'
inv = 'INV'
noinv = 'NOINV'
hypercom = 'BASE'

spinlock = 'Spinlock'

def get_default_heapmap_style_sheets():
    return [DEFAULT_BASE_STYLE, DEFAULT_HEAP_MAP_STYLE]

def get_default_bar_style_sheets():
    return [DEFAULT_BASE_STYLE, DEFAULT_BAR_STYLE]

def get_default_line_style_sheets():
    return [DEFAULT_BASE_STYLE, DEFAULT_LINE_STYLE]

def cal_bar_offset(index, num, width, align_mode = "center"): 
    '''
        calculate offset to x of groub bars
        @param: 
            index: index of the bar start with 0
            num: the number of bars in group 
            width: witdth of each bar(should be the same)
        @return: 
            return offset 
    '''
    assert align_mode in ['center'] and "unsupported align mode %s"%align_mode 
    return (2*index + 1 - num)*width / 2

def save_figure(name):
    if not os.path.exists(DEFAULT_SAVE_DIR):
        os.mkdir(DEFAULT_SAVE_DIR)
    plt.savefig(os.path.join(DEFAULT_SAVE_DIR, name))
    
def set_hatch(*, color, linewidth): 
    plt.rcParams["hatch.color"] = color
    plt.rcParams["hatch.linewidth"] = linewidth

# cm_ebpf = []
# cm_LKM = []
# unimon_ebpf = []
# unimon_LKM = []
# unimon_noinv = []
# unimon_inv = []
# nitro_ebpf = []
# nitro_LKM = []
# nitro_noinv = []
# nitro_inv = []

# 获取csv文件中的数据，以dict['实验名']:[数据1，数据2]的形式返回
def get_data(file_name='data.csv'):
    df = pandas.read_csv("./raw_data/" + file_name)
    data = {}
    for column_name, column_data in df.items():
        data[column_name] = column_data.values.tolist()
    return data
