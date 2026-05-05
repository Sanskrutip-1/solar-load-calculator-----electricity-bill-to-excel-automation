import streamlit as st
import requests

st.title("⚡ Solar Load Calculator AI")

uploaded_file = st.file_uploader("Upload Electricity Bill", type=["jpg","png","pdf"])

if uploaded_file:

    if st.button("Process Bill"):
        
        files = {"file": uploaded_file.getvalue()}
        
        response = requests.post("http://127.0.0.1:8000/process/", files=files)

        if response.status_code == 200:
            st.success("✅ Processed Successfully!")

            with open("output.xlsx", "wb") as f:
                f.write(response.content)

            with open("output.xlsx", "rb") as f:
                st.download_button("Download Excel", f, file_name="solar_output.xlsx")