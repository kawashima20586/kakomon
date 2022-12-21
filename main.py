import streamlit as st
import gspread
import random


from google.oauth2.service_account import Credentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'API.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)


SP_SHEET_KEY = '11cJmn4lggpvbI3G4XfLLru8YJVjWINTIFAeyehjfYo0'

sh = gc.open_by_key(SP_SHEET_KEY)

st.title('機械保全学科試験過去問')

syutsudai = st.sidebar.selectbox(
    '番号順(1)orランダム(2)',
    list(range(1,3)))

if syutsudai == 1:

   nendo = st.sidebar.selectbox(
      '何年度の問題を実施しますか？',
      list(range(2014,2022)))


   if nendo == 2014:
      SP_SHEET = '2014'
   elif nendo == 2015:
      SP_SHEET = '2015'
   elif nendo == 2016:
      SP_SHEET = '2016'
   elif nendo == 2017:
      SP_SHEET = '2017'
   elif nendo == 2018:
      SP_SHEET = '2018'
   elif nendo == 2019:
      SP_SHEET = '2019'   
   elif nendo == 2020:
      SP_SHEET = '2020'
   elif nendo == 2021:
      SP_SHEET = '2021'

   worksheet = sh.worksheet(SP_SHEET)
   data = worksheet.get_all_values()

   st.write(nendo,'年度学科')

   for j in range(50):
      st.write(data[j+1][0])
      st.write(data[j+1][1])
      st.write('■選択肢')
      for i in range(4):
         st.write(data[j+1][i+2])

      expander = st.expander('★答え')
      expander.write(data[j+1][6])
      expander.write(data[j+1][7])

if syutsudai == 2:
   for j in range(50):

      nendo = random.randint(2014,2021)

      if nendo == 2014:
         SP_SHEET = '2014'
      elif nendo == 2015:
         SP_SHEET = '2015'
      elif nendo == 2016:
         SP_SHEET = '2016'
      elif nendo == 2017:
         SP_SHEET = '2017'
      elif nendo == 2018:
         SP_SHEET = '2018'
      elif nendo == 2019:
         SP_SHEET = '2019'   
      elif nendo == 2020:
         SP_SHEET = '2020'
      elif nendo == 2021:
         SP_SHEET = '2021'

      worksheet = sh.worksheet(SP_SHEET)
      data = worksheet.get_all_values()
      
      x = random.randint(1,50)
      st.write(data[x+1][0])
      st.write(data[x+1][1])
      st.write('■選択肢')
      for i in range(4):
         st.write(data[x+1][i+2])

      expander = st.expander('★答え')
      expander.write(data[x+1][6])
      expander.write(data[x+1][7])

#gspread==5.0.0
#gspread-dataframe==3.2.2