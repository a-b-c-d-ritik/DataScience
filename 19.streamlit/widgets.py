import streamlit as st;
st.set_page_config(page_title='Rust in Streamlit', page_icon='🦀', layout='wide')
#st.set_page_config(page_title="Arrangers",page_icon="dp.jpg",page_color="white")
st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #FFA421 0%, #F0F0F0 100%);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

if st.button(" event karaiye"):
    st.success("event boook ho gaya apka")
    st.balloons()
    st.checkbox("")
#else:
    #st.image("dp.jpg")
rb1=st.radio("desert:",["rasgulla","icecream","jalebi"])
#st.succes(f"{rb1}")
rb2=st.radio("main course:",["chicken","mutton","rice","dal"])
#st.fragment()