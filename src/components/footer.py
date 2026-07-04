# import streamlit as st

# def footer_home():
#     logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"

#     st.markdown(f"""
#         <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center;">
#             <p style="font-weight:bold; color:white;">Created by</p>
#             <img src='{logo_url}' style='max-height:25px;' />
#         </div>
#     """, unsafe_allow_html=True)

import streamlit as st

def footer_home():
    st.markdown("""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center;">
            <p style="font-weight:bold; color:white;">Created by Gaurav Manjhi</p>
        </div>
    """, unsafe_allow_html=True)

footer_home()

def footer_dashboard():
    st.markdown("""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center;">
            <p style="font-weight:bold; color:black;">Created by Gaurav Manjhi</p>
        </div>
    """, unsafe_allow_html=True)

footer_dashboard()