import streamlit as st
import pandas as pd



#st.session_state.yousef =1# هاي بس طريق مشان احط قيمه داخل السيشن ستايت

labels = ['name']

#بعرف مصفوفه وبضعها في السيشن ستاتي مشان احفظها من الري رن كل مره واحفظ قيمتها 
if 'text_list' not in st.session_state:
 st.session_state.text_list = []
 #st.session_state["yousef"] = ['name']
 


st.header("Session Project: ")
"---"
"###"
#كل ما اضغط على زر داخل المشروع بعمل رن للمشروع من جديد واليست عندي بتصير فارغه وبرجع بحط القيم جديده بس بتكون رجعت من الصفر وانا هان بدي احل المشكله


user_input = st.text_input('Enter text her:',placeholder='names')

if st.button('Append'):
    st.session_state.text_list.append(user_input)
if st.button('Clear'):
    st.session_state.text_list = []#خلص نظف الليست رجعها فاضيه   

st.write('Text List',st.session_state.text_list)
"---"
st.write("Session state",st.session_state)#الهدف منها انو لو عملت ري رن للمشروع تبقي الحاله كما هي في اللست 
"###"
"---"



#--------------------
df1 = pd.DataFrame.from_dict(st.session_state.text_list)
df2 = pd.DataFrame.from_records(st.session_state.text_list)
#df3 = pd.DataFrame.from_records(st.session_state.text_list,columns=labels)
st.write('panda read the list',df1)

"---"
st.write(df2)
#st.write(df3)