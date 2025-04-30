import streamlit as st
import os as os;



# Set Page Config
st.set_page_config(
    page_title="Real Estate Price Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Title with Image/Icon
st.title("🏠 Real Estate Price Predictor")
st.markdown("Welcome to **Real Estate Price Predictor** – A machine learning-powered web app to estimate property prices.")

# Introduction Section
st.subheader("What is this app?")
st.markdown("""
This web app helps you estimate property prices based on features like area, location, and amenities. It also allows you to:
- **Add New Cities**: Dynamically extend the dataset with properties from new cities.
- **Price Prediction**: Input property details and predict an estimated price.
- **Analytics**: Visualize data insights like area-price trends and location clusters.
""")

# Features Section
st.subheader("Features")
st.markdown("""
- **Price Prediction** for Residential Apartments, Rental Apartments, Independent Floors, Independent Houses, and Residential Houses.
- **Analytics Page**: Explore interesting insights regarding real estate in various cities or localities.
- **Add a New City**: Add property data from your city and get price predictions and analytics.
- **Download Resources**: Download datasets and ML models used in this project.
""")

# Tech Stack with Icons
st.subheader("Tech Stack")
tech_stack = {
    "Programming Language": "Python",
    "Version Control": "Git & GitHub",
    "Data Analysis": "Pandas, Numpy",
    "Visualization": "Matplotlib, Seaborn, Plotly",
    "Machine Learning": "Scikit-Learn",
    "Frontend & Backend": "Streamlit",
    "Extra": "Pydantic"
}

# Display Tech Stack with Icons
col1, col2 = st.columns(2)
with col1:
    st.write("**Programming Language:** Python")
    st.write("**Data Analysis:** Pandas, Numpy")
    st.write("**Visualization:** Matplotlib, Seaborn, Plotly")
    st.write("**Machine Learning:** Scikit-Learn")
    st.write("**Frontend & Backend:** Streamlit")

with col2:
    st.write("**Version Control:** Git & GitHub")
    st.write("**Extra:** Pydantic")

# Installation Instructions Section
st.subheader("Installation")
st.markdown("""
To get started with the project, follow these steps:

1. Clone this repo to your local system.
2. Create a virtual environment and install the project dependencies using the command:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the Streamlit app with the following command:
    ```sh
    streamlit run Real_Estate_Project.py
    ```
""")

# Acknowledgements Section
st.subheader("Acknowledgements")
st.markdown("""
- **[99acres.com](https://99acres.com/)**: Used this website to gather data for the project.
- **[CampusX DSMP](https://learnwith.campusx.com)**: Inspiration from the course's Capstone Project.
""")

# License Section
st.subheader("License")
st.markdown("[MIT License](https://choosealicense.com/licenses/mit/)")

# Disclaimer Section
st.warning("""
**Disclaimer:** The data used in this project is gathered from 99acres.com and is used solely for educational purposes.
""")

# Footer with Call to Action
st.markdown("---")
st.markdown("💡 **Get started with price prediction and explore insights for your city!**")
