import streamlit as st
import langchain_helper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American","other"))

if cuisine == "other":
    cuisine = st.sidebar.text_input("Enter your cuisine:")
else:
    cuisine = cuisine

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.markdown(
    "<h3 style='font-weight:100;'>{f}</h3>".format(f=response['restaurant_name'].strip()), 
    unsafe_allow_html=True
)
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)

