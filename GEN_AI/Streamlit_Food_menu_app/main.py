import streamlit as st
import langchainhelper
st.title('Restaurant name generator')
cuisine=st.sidebar.selectbox("Pick a cuisine",('Indian',"Italian","Rusian","American","Mexican","Arabic"))

if cuisine:
    response=langchainhelper.generate_restraunt_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items=response['menu_items'].strip().split(",")
    st.write('Menu Items ')
    for item in menu_items:
        st.write("",item)