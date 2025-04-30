import streamlit as st
from pathlib import Path


# ----- PAGE CONFIG -----
st.set_page_config(page_title="👨‍💻 Developer Info", page_icon="👨‍💻", layout="centered")

# ----- DEVELOPER PAGE CONTENT -----
st.markdown("<h1 style='text-align: center; color: #2196F3;'>👨‍💻 Developer Information</h1>", unsafe_allow_html=True)
st.markdown("---")

# About Developer
st.markdown("""
### Hello! I'm Aaradhy Seth

- 🛠️ Passionate about Machine Learning and Data Science.
- 📚 Currently pursuing B.Tech from Jaypee University of Engineering and Technology
- 🌍 Interested in real-world applications of AI and Data.
- 📫 Reach out to me via: [sethaaradhy@gmail.com](sethaaradhy@gmail.com)
""")

# Download Resume Button
resume_path = Path("assets/Resume.pdf")  # <-- Make sure your resume is saved here
with open(resume_path, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="📄 Download My Resume", data=PDFbyte, file_name="Resume.pdf", mime="application/pdf")

# Footer
st.markdown("---")
st.markdown("Connect with me on [LinkedIn](https://www.linkedin.com/in/aaradhy-seth-399029267/) | [GitHub](https://github.com/AARADHY0612)", unsafe_allow_html=True)
