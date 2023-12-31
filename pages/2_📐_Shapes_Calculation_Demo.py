import streamlit as st
import time#مكتبة الوقت بدي اياها مشان اخلي المشروع يتاخر شوي واجرب السبينير




st.set_page_config(page_title="HELLO",page_icon="💻",layout="centered")

st.header("Shapes Calculations")
st.sidebar.title("Configuration")#بعرف سايد بار

with st.sidebar:#هاي بتعني انو اي اشي تحتها بدو يدخل داخل السايد بار انا هان اعطيتو بس الشايبس او السيليكت بوكس فقط
#اذا بعطي السيليكت بوكس او القائمه لمتغير بقدر اخذ هاذ المتغير واطبعو وهو بطبع مباشر اختيار المستخدم
     shape = st.selectbox("Choose shape:",["Circle","Rectangle"])

#print(shape)

if shape == 'Circle':
    radius = st.number_input('Radius:',min_value=0.0,max_value=100.0,step=0.01)
    area = radius*radius *3.14 #مساحة الدائره
    perimeter = 2* 3.14 *radius# محيط الدائره
    #area = pow(radius,2)*3.14

elif shape == 'Rectangle':

    width = st.number_input('Width:',0.,step=0.1)
    height = st.number_input('Height', 0., step=0.1)
    area = width * height
    perimeter =2*(width+height)

compute_btn = st.button("Compute Area and Perimeter")
if compute_btn:
   '''
   في اكثر من طريقه لتعريف الباتين داخل المشروع
   '''
   with st.spinner(".........قيد الحساب "):
        time.sleep(2)# تعمل تاخير للتنفيذ مدة ثانيتين مشان اشوف السبينير
        st.write(area)
        st.write(perimeter)
   
   
#if st.button("Compute Area and Perimeter2"):
#   st.write(f"Area = {area}")
#   st.write("Perimeter ="+str(perimeter))
#   st.write(f"Perimeter ={perimeter}")

