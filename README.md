### Công cụ tạo bản đồ đặc biệt sử dụng các thư viện Python kết hợp dữ liệu từ OpenStreetMap

------

#### Hướng dẫn cài đặt trên hệ điều hành Ubuntu 21.04 x64

<u>Chuẩn bị</u>

> sudo apt update && sudo apt upgrade
>
> sudo apt install git

> sudo apt install python3-pip

> sudo pip install --upgrade pip

> sudo pip install --upgrade setuptools

<u>Cài đặt PrettyMaps</u>

> cd home

> sudo pip install git+[https://github.com/abey79/vsketch#egg=vsketch](https://github.com/abey79/vsketch?fbclid=IwAR28fcSTp24Msj_5tKxQfYyz425wUSsd81M85XDVzXUGgHbF_o4AYz3A378#egg=vsketch) --no-warn-script-location

> sudo pip install git+[https://github.com/marceloprates/prettymaps.git...](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Fmarceloprates%2Fprettymaps.git%3Ffbclid%3DIwAR01EJ30-cufU-zn9oiU65XYK_pWVEeD1VYC6blG3QMyykbyYvcrIZCHMIk%23egg%3Dprettymaps&h=AT1FABcHyCJmNKZQP-m6zfKOd9R7bsvR10227ureLGgIuovUd03hRIwPFL0zGYwvqYCd1CyLoNe9nkZBFno8WhR9dEbojuQJ9htWiZHmF5kJ9Z78BbwPTuAD_zPfFwlAnA&__tn__=-UK-R&c[0]=AT36OOYYttC4ajlwj2PngwdcIwVb6gQjjp2zvscMcGr3iyKOvU28JdFJ2Yd0h2nFNYmtsxKkk9VspYhsLM70Bce-I8z-MRUNxrfaKb4-VMkZMhnQdhHjgpSIta667zT0H746dMXKT7bbjE3V3Gn-283c0goV6dXlXRg) --no-warn-script-location

> sudo mkdir ../prints

> sudo mkdir ../assets

> sudo mkdir ../assets/Permanent_Marker

> sudo wget -O ../assets/Permanent_Marker/PermanentMarker-Regular.ttf [https://github.com/.../Perman.../PermanentMarker-Regular.ttf](https://github.com/marceloprates/prettymaps/raw/main/assets/Permanent_Marker/PermanentMarker-Regular.ttf?fbclid=IwAR0KP6NSvPd6wnM6lJAvWxkXkQVaoscm3mzBx_FjfoGs9_DgKUAwtgFQDZo)

Sau khi cài đặt hoàn tất thì mọi người sẵn sàng để tùy biến bản đồ thông qua các code mẫu (python) có sẵn trong repo github

------

<u>Lưu ý:</u>

Để có thể thể hiện phần biển và các thành phần liên quan cần thiết bổ sung thư viện "water-polygons-split" có thể được tải về từ link sau

> https://osmdata.openstreetmap.de/download/water-polygons-split-4326.zip

<u>Code mẫu</u>

```python
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
```

<u>Ảnh sample</u>



------

<u>Credit</u>: [marceloprates](https://github.com/marceloprates)/**[prettymaps](https://github.com/marceloprates/prettymaps)**

