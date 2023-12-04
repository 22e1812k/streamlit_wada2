import streamlit as st
import pandas as pd
st.markdown(
     """
     <style>
     .reportview-container {
         background-image: url(C:\\Users\\wadari\\Desktop\\情報基礎実習\\camp.jpg) center;
         background-size: cover;
     }
     </style>
     """,
     unsafe_allow_html=True
)     

import time
from PIL import Image

st.title("信大生向けおすすめキャンプ場")
option = st.selectbox('希望する地域を教えてください',list(['選択','長野市周辺','松本市周辺','上田市周辺','伊那市周辺',]))
import time
st.sidebar.write('プログレスバーの表示')
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
     bar.progress(i+1)
     time.sleep(0.01)

if option == "選択":
     st.write("　　")
        
elif option == "長野市周辺":
     st.write("戸隠キャンプ場") 
     img = Image.open('togakusi.jpg')
     st.image(img, caption='がっしり、、どっしり、、',use_column_width=True)
     show_details = False
     if st.button('詳細'):
        show_details = True
     if show_details:
          text_with_paragraphs = "場所：長野県長野市戸隠3694\n\n基本料金：一人1500円\n\n時間：チェックイン10:00～チェックアウト～10:00\n\nおすすめポイント：動物と触れ合える牧場がある"
          st.write(text_with_paragraphs)

     bookings = pd.DataFrame(columns=['Name', 'Date', 'Time'])

     st.title('予約ページ')

     name = st.text_input('お名前')
     date = st.date_input('日付')
     time = st.time_input('時間')

     if st.button('予約する'):
          new_booking = pd.DataFrame({'Name': [name], 'Date': [date], 'Time': [time]})
          bookings = pd.concat([bookings, new_booking], ignore_index=True)
          st.success('予約が完了しました。ご予約ありがとうございます。')

     st.subheader('予約一覧')  
     st.write(bookings)   


       
elif option == "松本市周辺":
     st.write("高ボッチキャンプ場")
     img = Image.open('takabotti.jpg')
     st.image(img, caption='ここは天空',use_column_width=True)
     show_details = False
     if st.button('詳細'):
        show_details = True
     if show_details:
          text_with_paragraphs = "場所：長野県塩尻市片丘\n\n基本料金：一人1000円\n\n時間：チェックイン10:00～チェックアウト～10:00\n\nおすすめポイント：運が良ければ雄大な雲海も見られる"
          st.write(text_with_paragraphs)

     bookings = pd.DataFrame(columns=['Name', 'Date', 'Time'])

     st.title('予約ページ')

     name = st.text_input('お名前')
     date = st.date_input('日付')
     time = st.time_input('時間')

     if st.button('予約する'):
          new_booking = pd.DataFrame({'Name': [name], 'Date': [date], 'Time': [time]})
          bookings = pd.concat([bookings, new_booking], ignore_index=True)
          st.success('予約が完了しました。ご予約ありがとうございます。')

     st.subheader('予約一覧')  
     st.write(bookings)

elif option == "上田市周辺":
     st.write("SENKO TINY CAMP")
     img = Image.open('senko.jpg')
     st.image(img, caption='贅沢やわー',use_column_width=True)
     show_details = False
     if st.button('詳細'):
        show_details = True
     if show_details:
          text_with_paragraphs = "場所：長野県上田市真田町長6423‐2\n\n基本料金：一人5500円\n\n時間：チェックイン14:30～チェックアウト～10:00\n\nおすすめポイント：一日一組限定の超贅沢キャンプ"
          st.write(text_with_paragraphs)

     bookings = pd.DataFrame(columns=['Name', 'Date', 'Time'])

     st.title('予約ページ')

     name = st.text_input('お名前')
     date = st.date_input('日付')
     time = st.time_input('時間')

     if st.button('予約する'):
          if (bookings['Date'] == date).any():
               st.warning('その日の予約は終了しております。申し訳ございません')
          else:     
              new_booking = pd.DataFrame({'Name': [name], 'Date': [date], 'Time': [time]})
              bookings = pd.concat([bookings, new_booking], ignore_index=True)
              st.success('予約が完了しました。ご予約ありがとうございます。')

     st.subheader('予約一覧')  
     st.write(bookings)

else :
     st.write("銀河もみじキャンプ場") 
     img = Image.open('ginga.jpg')
     st.image(img, caption='日本一の星空ですわ',use_column_width=True) 
     bookings = pd.DataFrame(columns=['Name', 'Date', 'Time'])
     show_details = False
     if st.button('詳細'):
        show_details = True
     if show_details:
          text_with_paragraphs = "場所：長野県下伊那郡阿智村浪合1711-1\n\n基本料金：一人3000円\n\n時間：チェックイン13:00～チェックアウト～10:00\n\nおすすめポイント：日本一きれいな阿智村の星空を一望できる"
          st.write(text_with_paragraphs)
     

     st.title('予約ページ')

     name = st.text_input('お名前')
     date = st.date_input('日付')
     time = st.time_input('時間')

     if st.button('予約する'):
          if (bookings['Date'] == date).any():
               st.warning('その日の予約は終了しております。申し訳ございません')
          new_booking = pd.DataFrame({'Name': [name], 'Date': [date], 'Time': [time]})
          bookings = pd.concat([bookings, new_booking], ignore_index=True)
          st.success('予約が完了しました。ご予約ありがとうございます。')

     st.subheader('予約一覧')  
     st.write(bookings)

from datetime import datetime

chat_log = []
st.title('チャット')
st.write('ここでキャンプ好き信大生とはなそうよ')

message = st.text_input("メッセージを入力してください:")

if st.button("送信"):
     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     chat_log.append(f"{current_time} - You: {message}")
st.header("チャットログ")
for msg in chat_log:
     st.write(msg)


