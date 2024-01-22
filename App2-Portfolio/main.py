import streamlit as st

# this is to set configuration of streamlit page on website exto increase container size to fit text etc
st.set_page_config(layout="wide")

# this method 'columns' of st module will return 2 column objects. we assign we object to a variable
col1, col2 = st.columns(2)

# width in below will reduce the image size on th streamlit website

with col1:
    st.image("images/photo.jpg", width=450)

with col2:
    st.title("Sai Krishna Samudrala")
    content = """With over a decade of experience in data analysis, predictive analytics, and data visualization, 
    I am a Certified Data Analytics Consultant proficient in Azure, Alteryx, PowerBI, Tableau, SQL, and Python. I 
    specialize in transforming raw data into meaningful insights to help solve complex business problems and have a 
    proven track record with Fortune 500 companies like Schneider Electric and Nestlé. My goal is to deliver 
    innovative data-driven solutions that benefit both clients and society"""

    # # we can use st.write(content) as well but st.info(content) makes it looks prettier on website(background color)
    st.info(content)
