import streamlit as st
import pandas as pd #مكتبه لقرائة الملفات
import plotly.express as px#مكتبه للرسومات البيانيه
import numpy as np# مكتبه للارقام بدي اياها مشان احدد الاعمده الي فيها ارقام بس
import matplotlib.pyplot as plt #كتبه بدها ترسم رسم بياني


@st.cache_data #عند تشغيل المره الاولى برفع البيانات بس ما بدي كل ما اشغل ارفع البيانات لانو ما تغير الملف

def load_data(file):# هاذ فنكشن بسيط بس يقرا الداتا
  return pd.read_csv(file)
  
file = st.file_uploader("Upload file",type=["csv"])

if file is not None:

    #df = pd.read_csv(file)بدون استخدام الكاش
    df = load_data(file)# مع استخدام الكاش لكن هو ما راح يتنفذ لاني بحمل الملف كل مره بزبط لما يكون عندي لنك ثابت يعني مش انا الي بحمل الملف المستخدم
   
   
    #st.write(df)

    n_rows = st.slider('Choose number of rows to display',min_value=1,max_value=len(df),step=1)
    column_to_show = st.multiselect("## Select columns to show:",df.columns.to_list(),default = df.columns.to_list())
    
    numerical_columns = df.select_dtypes(include=np.number).columns.to_list()#هاذ بجيبلي بس القيم او الاعمده الرقميه في الاعمده يعني مش سترنج


    st.write(df[:n_rows][column_to_show]) 

    tab1 , tab2 = st.tabs(["📈 Plo","🧰 Histogram"])
    
    
    with tab1:
     col1, col2, col3 = st.columns(3)
      
     with col1:
       x_column = st.selectbox('Select on x:',numerical_columns)
     with col2:
       y_column = st.selectbox('Select y:',numerical_columns)
     with col3:
       color = st.selectbox('Select color:',df.columns)
    

   
       #fig_scatter = px.scatter(df,x = 'Age',y = 'Sex')#بحدد معلومات الرسمه وبخزنها في متغير مشان استخدمو
    
     fig_scatter = px.scatter(df,x = x_column,y=y_column,color=color)
     st.plotly_chart(fig_scatter)

      #----------------
     "---"
     st.subheader("Line Plot:")
     fig = plt.figure(figsize=(18,5))
     plt.plot(df[x_column], df[y_column],color ='#66a3ff',lw = 5, marker = '*',markersize=10,ls='--')
     plt.title("بيانات البيع" , fontsize = 20)
     plt.xlabel("العمر")
     plt.ylabel("الجنس")
    
     st.pyplot(fig)

     #--------------------
     "---"
    with tab2:
     histogram_feature = st.selectbox('Select feature to histgrame',numerical_columns)
     fig_hist = px.histogram(df, x = histogram_feature)
     #fig_hist = px.histogram(df, x='Age')#نوع اخر من الرسم البياني
     st.plotly_chart(fig_hist)

