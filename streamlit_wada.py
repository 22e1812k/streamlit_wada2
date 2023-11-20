import streamlit as st
import time

st.title("長野県のおすすめキャンプ場")
st.write("和田です")
text = st.text_input("あなたの名前を教えてください")
st.write("あなたの名前は"+text+"です")
option = st.selectbox('希望する地域を教えてください',list(['長野市周辺','松本市周辺','上田市周辺','伊那市周辺']))
'あなたが選択したのは,',option,'です'
st.sidebar.write('プログレスバーの表示')
'Start!'

latest_iteration=st.empty()
bar = st.progress(0)

for i in range(100):
   latest_iteration.text(f'lteration{i+1}')
   bar.progress(i+1)
   time.sleep(0.01)
'Done!!!'

if option == "長野市周辺":
   print("戸隠キャンプ場")

elif option == "松本市周辺":
   print("高ボッチキャンプ場")

elif option == "上田市周辺":
   print("菅平キャンプ場")

else :
   print("銀河もみじキャンプ場")  



left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
   right_column.write("ここは右カラムです")

from PIL import Image 
img = Image.open('aiga-.jpg')
st.image(img, caption='アイガー北壁',use_column_width=True)

import pandas as pd
import numpy as np
df = pd.DataFrame(
   np.random.rand(100,2)/[50,50] + [35.69,139.70],
   columns = ['lat','lon',]
)
st.map(df)
df = pd.DataFrame(
   np.random.rand(20,3),   
   columns = ['a','b','c']
)
st.table(df.style.highlight_max(axis=0))
st.bar_chart(df)
