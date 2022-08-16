#!/usr/bin/env python
# coding: utf-8

# In[16]:


coords_12=[[16.786280373283, 80.8484567581661],[16.77707673761769, 80.87901248425977],[16.785951679686974, 80.95214023322553],
           [16.735983644360275, 81.06681003277286],[16.712309998280265, 81.09496249951084],[16.71837145861124, 81.11680646423024],
           [16.81567452392289, 81.24040265966536],[17.046897028606395, 81.53703352870959],[17.00356447351315, 81.80207870336486],
           [17.368556910786822, 82.54809239558186],[17.695930949195294, 83.21825843305217],[17.921202710285645, 83.18732627810975],
           [18.05182039722915, 83.31092247354485],[18.10795622237225, 83.3988131014098],[18.06471276650232, 83.52482474365247],[18.299562475462093, 83.86952078665469],[18.416868329515406, 84.04667532668371]]
coords_23=[[16.777076737330464, 80.87969912864854],[16.715598180531835, 81.02011813957343],[16.73466851904225, 81.06681003562666],
           [16.81041617259755, 81.24726911496731],[16.820932729406305, 81.56999251415895],[17.004877728633392, 81.80207870336486],
           [17.100984990755812, 82.23498203381295],[17.368556910786822, 82.55083897770264],[17.695930949195294, 83.21825843305217],
           [17.752563637980618, 83.21616539037794],[17.8833055281388, 83.30680260036367],[18.10795622237225, 83.3988131014098]]


# In[17]:


import folium 
from branca.element import Figure
fig234=Figure(height=550,width=750)
map9=folium.Map(location=[16.82365919254232, 80.83481632385855],tiles='cartodbpositron',zoom_start=10)
fig234.add_child(map9)
map9


# In[18]:


f7=folium.FeatureGroup("Vehicle 1")
f8=folium.FeatureGroup("Vehicle 2")


#Adding markers to the map
folium.Marker(location=[16.786280373283, 80.8484567581661],popup='Default popup Marker1',tooltip='University',icon=folium.Icon(color='red',prefix='fa',icon='university')).add_to(map9)
folium.Marker(location=[18.415565369381717, 84.04530203567575],popup='<strong>Marker2</strong>',tooltip='<strong>Home</strong>',icon=folium.Icon(color='green',prefix='fa',icon='home')).add_to(map9)
folium.Marker(location=[16.813045366487952, 81.24177595072571],popup='<h3 style="color:green;">Marker3</h3>',tooltip='<strong>Hospital</strong>',icon=folium.Icon(color='blue',prefix='fa',icon='medkit')).add_to(map9)
folium.Marker(location=[16.715598180531835, 81.02011813957343],popup='<h3 style="color:green;">Marker4</h3>',tooltip='<strong>shoping mall</strong>',icon=folium.Icon(color='blue',prefix='fa',icon='shopping-bag')).add_to(map9)
folium.Marker(location=[16.785951679686974, 80.95214023322553],popup='<h3 style="color:blue;">Marker7</h3>',tooltip='<strong>Bus stand</strong>',icon=folium.Icon(color='green',prefix='fa',icon='bus')).add_to(map9)
folium.Marker(location=[16.813045366487952, 81.24177595072571],popup='<h3 style="color:green;">Marker8</h3>',tooltip='<strong>clinic</strong>',icon=folium.Icon(color='blue',prefix='fa',icon='medkit')).add_to(map9)
folium.Marker(location=[16.999624652926148, 81.79933212124406],popup='<h3 style="color:green;">Marker9</h3>',tooltip='<strong>Railway station</strong>',icon=folium.Icon(color='orange',prefix='fa',icon='subway')).add_to(map9)
folium.Marker(location=[17.363314136503238, 82.5396386492195],popup='<h3 style="color:red;">Marker10</h3>',tooltip='<strong>cycle shop</strong>',icon=folium.Icon(color='pink',prefix='fa',icon='bicycle')).add_to(map9)
folium.Marker(location=[17.93960342600162, 83.18595493708847],popup='<h3 style="color:green;">Marker11</h3>',tooltip='<strong>car showroom</strong>',icon=folium.Icon(color='red',prefix='fa',icon='car')).add_to(map9)
folium.Marker(location=[17.69249880932916, 83.21891392253784],popup='<h3 style="color:green;">Marker12</h3>',tooltip='<strong>Air port</strong>',icon=folium.Icon(color='blue',prefix='fa',icon='plane')).add_to(map9)
folium.Marker(location=[17.886027843734464, 83.30405796828201],popup='<h3 style="color:blue;">Marker13</h3>',tooltip='<strong>charging station</strong>',icon=folium.Icon(color='blue',prefix='fa',icon='battery-full')).add_to(map9)
folium.Marker(location=[18.214792125905316, 83.69511282864163],popup='<h3 style="color:blue;">Marker13</h3>',tooltip='<strong>school</strong>',icon=folium.Icon(color='blue',prefix='fa',icon='fa-building')).add_to(map9)

# Adding lines to the different feature groups
line_1=folium.vector_layers.PolyLine(coords_12,popup='<b>Path of Vehicle_1</b>',tooltip='Vehicle_1',color='blue',weight=10).add_to(f7)
line_2=folium.vector_layers.PolyLine(coords_23,popup='<b>Path of Vehicle_2</b>',tooltip='Vehicle_2',color='red',weight=10).add_to(f8)
line_2=folium.vector_layers.PolyLine(coords_23,popup='<b>Path of Vehicle_2</b>',tooltip='Vehicle_2',color='red',weight=10).add_to(f8)
f7.add_to(map9)
f8.add_to(map9)
folium.LayerControl().add_to(map9)
map9


# In[1]:





# In[ ]:




