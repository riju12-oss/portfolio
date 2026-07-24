import streamlit as st
st.set_page_config(page_title="My Webpage",page_icon=":tada:",layout="wide")
st.subheader("Hi,I am Saptorshi :wave:")
st.title("A data analyst from India")
st.write("I am passionate about finding new skills using python")

st.write("""


I am passionate about:
- 📊 Data Analytics
- 🐍 Python Programming
- 📈 Data Visualization
- 🤖 Machine Learning
""")

st.header("🛠 Skills")
st.write("""
- Python
- SQL
- Excel
- Power BI
- Pandas
- NumPy
- Streamlit
""")

st.header("📂 Projects")

st.success("✔ Sales Dashboard using Power BI")
st.info("✔ Data Analysis using Python")
st.warning("✔ Customer Segmentation Project")

st.header("📞 Contact")

st.write("📧 Email: youremail@gmail.com")
st.write("🔗 LinkedIn: https://linkedin.com/in/your-profile")
st.write("💻 GitHub: https://github.com/your-username")

st.button("Hire Me")
st.balloons()
st.success("Thank you for visiting my portfolio!")
