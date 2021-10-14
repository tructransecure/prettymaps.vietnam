#
#Khai báo các tham số hệ thống và gọi thư viện
#

import sys
sys.path.append('../')

import vsketch
from prettymaps import *
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt

#
#Thông tin chung
#

palette = ['#FFC857', '#E9724C', '#C5283D']

#
#Thiết lập tham số
#

fig, ax = plt.subplots(figsize = (20, 20), constrained_layout = True)

backup = plot(
	#
	#Tọa độ vị trí trên Google Maps hoặc tên địa điểm kèm bán kính (tính bằng mét)
    #Nếu trong quá trình xử lý bị "Killed" thì giảm bán kính lại nhỏ hơn
    #
	
	(10.7744704,106.7019512), radius = 1000,
    
    ax = ax,
    
    layers = {
            'perimeter': {},
            'streets': {
                'width': {
                    'motorway': 5,
                    'trunk': 5,
                    'primary': 4.5,
                    'secondary': 4,
                    'tertiary': 3.5,
                    'residential': 3,
                    'living_street': 2,
                    'pedestrian': 1,
                    'footway': 1,
                    'track': 1,
                    'bridleway': 1
                }
            },
			
			#
			#Tùy biến các tham số tag theo tài liệu hướng dẫn của OpenStreetMaps để phù hợp các lớp địa hình
			#
			
            'building': {'tags': {'building': True, 'landuse': 'construction'}, 'union': False},
            'water': {'tags': {'natural': ['water','lake'],'waterway':['river','riverbank','canal','lagoon']}},
            'green': {'tags': {'landuse': ['grass','farmland','farmyard','reservoir','forest'], 'natural': ['island', 'wood'], 'leisure': 'park'}},
            'scrub': {'tags': {'natural': 'scrub'}},
            'walls': {'tags': {'manmade': 'embankment'}},
        },
        
        #
        #Thiết lập màu sắc cho các layer đã tùy biến
        #
        
        drawing_kwargs = {
            'background': {'fc': '#000080', 'ec': '#dadbc1', 'hatch': 'ooo...', 'zorder': -1},
            'perimeter': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'lw': 0, 'hatch': 'ooo...',  'zorder': 0},
            'green': {'fc': '#D0F1BF', 'ec': '#2F3737', 'hatch_c': '#b3cfa5', 'hatch': 'ooo...', 'lw': 1, 'zorder': 1},
            'scrub': {'fc': '#89d689', 'ec': '#2F3737', 'hatch_c': '#75bd75', 'hatch': 'ooo...', 'lw': 1, 'zorder': 1},
            'water': {'fc': '#a1e3ff', 'ec': '#2F3737', 'lw': 1, 'zorder': 2},
            'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 3},
            'walls': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 3},
            'building': {'palette': palette, 'ec': '#2F3737', 'lw': .5, 'zorder': 4},
        },

        osm_credit = {'color': '#2F3737'}
)

#
#Lưu bản đồ ra tập tin ảnh & vector
#

plt.savefig('/home/tructt/sg.png')
plt.savefig('/home/tructt/sg.svg')