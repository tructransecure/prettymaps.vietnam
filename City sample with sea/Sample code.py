#
#Khai báo các tham số hệ thống và gọi thư viện
#

from prettymaps import *
from matplotlib import pyplot as plt

def postprocessing(layers):
    layers['perimeter'] = layers['perimeter'].buffer(10)
    return layers

#
#Thông tin chung
#
    
palette = ['#FFC857', '#E9724C', '#C5283D']

dilate = 100
circle=False

#
#Thiết lập tham số
#

figsize=(20,20)
fig, ax = plt.subplots(figsize = figsize, constrained_layout = True)

# Plot
layers = plot(
    #
	#Tọa độ vị trí trên Google Maps hoặc tên địa điểm kèm bán kính (tính bằng mét)
    #Nếu trong quá trình xử lý bị "Killed" thì giảm bán kính lại nhỏ hơn
    #
    
    (16.0493665,108.2166648),
    radius=8000,
    ax = ax,
    
    layers = {
            'perimeter': {'circle': circle, 'dilate': dilate},
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
                    'bridleway': 4
                }
            },
            
            #
			#Tùy biến các tham số tag theo tài liệu hướng dẫn của OpenStreetMaps để phù hợp các lớp địa hình
			#            
            
            'building': {'tags': {'building': True, 'building':['home','house','family_house','residential','apartments','detached','villa','manor'],'landuse': ['construction','retail','industrial','commercial','education','port','depot']}, 'union': False},
            'water': {'tags': {'natural': ['water','lake','river','bay','habour','marina'],'waterway':['river','riverbank','canal','lagoon']}},
            'sea': {'tags': {'natural':['coastline','bay','shoal','beach','marina','sea','habour','ocean'],'place':['sea','ocean']}},
            'green': {'tags': {'landuse': ['grass','farmland','farmyard','reservoir','forest','allotments','flowerbed','meadow','orchard','greenfield'], 'natural': ['island', 'wood','forest','tree','tree_row'],'leisure': ['park','beach_resort','garden','golf_course','nature_reserve']}},
            'scrub': {'tags': {'natural': ['scrub','sand','dune','hill']}},
            'walls': {'tags': {'manmade': 'embankment'}},
            #
            #Giải nén tập tin water_polygons.shp để thiết lập đường dẫn phù hợp
            #
            'coastline': {'file_location':'/home/tructt/Desktop/Maps.BH/MapData/water/water_polygons.shp','buffer':100000,'circle':circle },
        
        },
        
        #
        #Thiết lập màu sắc cho các layer đã tùy biến
        #
        
        drawing_kwargs = {
        
            'background': {'fc': '#274e13', 'ec': '#c27ba0', 'hatch': 'ooo...', 'zorder': -1},
            'perimeter': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'lw': 0, 'hatch': 'ooo...',  'zorder': 0},
            'green': {'fc': '#D0F1BF', 'ec': '#2F3737', 'hatch_c': '#b3cfa5', 'hatch': 'ooo...', 'lw': 1, 'zorder': 1},
            'scrub': {'fc': '#89d689', 'ec': '#2F3737', 'hatch_c': '#75bd75', 'hatch': 'ooo...', 'lw': 1, 'zorder': 1},
            'water': {'fc': '#a1e3ff', 'ec': '#2F3737', 'lw': 1, 'zorder': 2},
            'sea': {'fc': '#44A7C4', 'ec': '#000080', 'lw': 1, 'zorder': 1},
            'coastline': {'fc': '#a8e1e6', 'ec': '#2F3737', 'hatch_c': '#9bc3d4', 'hatch': 'ooo...', 'lw': 1, 'zorder': 2},
            'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 3},
            'walls': {'fc': '#990000', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 3},
            'building': {'palette': palette, 'ec': '#FF0000', 'lw': .5, 'zorder': 4},
        },

        osm_credit = {'color': '#3b4545'}
)

#
#Lưu bản đồ ra tập tin ảnh & vector
#

plt.savefig('/home/tructt/Desktop/Maps.BH/DaNang.png')
plt.savefig('/home/tructt/Desktop/Maps.BH/DaNang.svg')
