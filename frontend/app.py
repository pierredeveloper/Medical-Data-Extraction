import streamlit as st
import requests
import tempfile

API_URL = "http://127.0.0.1:8000/extract_from_doc"

st.set_page_config(page_title="Medical Data Extractor", layout="centered")
st.title("📄 Medical Data Extraction")
st.subheader("Upload a medical document to extract structured information")

doc_type = st.radio("Document Type", options=["Prescription", "Patient Details"])
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    with open(tmp_file_path, "rb") as f:
        files = {"file": (uploaded_file.name, f, "application/pdf")}
        data = {"file_data": doc_type.lower().replace(" ", "_")}

        if st.button("🔍 Auto Extract"):
            with st.spinner("Extracting data..."):
                response = requests.post(API_URL, data=data, files=files)

            if response.status_code == 200:
                result = response.json()
                if "error" in result:
                    st.error(f"❌ Extraction error: {result['error']}")
                else:
                    st.success("✅ Data Extracted Successfully")
                    if doc_type == "Patient Details":
                        st.text_input("Name", result.get("patient_name", ""), disabled=True)
                        st.text_input("Phone Number", result.get("phone_number", ""), disabled=True)
                        st.text_area("Medical Conditions", result.get("medical_problem", ""), disabled=True)
                        st.radio("Hepatitis B Vaccine Status", ["Yes", "No"],
                                 index=0 if result.get("hepatitis_b_vaccination", "").lower() == "yes" else 1,
                                 disabled=True)
                    else:
                        st.text_input("Patient Name", result.get("patient_name", ""), disabled=True)
                        st.text_input("Patient Address", result.get("patient_address", ""), disabled=True)
                        st.text_area("Medications", result.get("medecines", ""), disabled=True)
                        st.text_area("Directions", result.get("directions", ""), disabled=True)
                        st.text_input("Refill", result.get("refill", ""), disabled=True)
                        st.text_input("Doctor Name", result.get("doctor_name", ""), disabled=True)
                        st.text_input("Consult Date", result.get("consult_date", ""), disabled=True)
            else:
                st.error(f"⚠️ API call failed with status code {response.status_code}")




# import streamlit as st
# import requests
# import json
#
# # FastAPI backend endpoint
# API_URL = "http://127.0.0.1:8000/extract_from_doc"
#
# st.set_page_config(page_title="Medical Data Extractor", layout="centered")
#
# st.title("📄 Medical Data Extraction App")
# st.write("Upload a document (PDF) and select the type to extract structured medical data.")
#
# # Upload form
# with st.form("upload_form"):
#     file_data = st.selectbox(
#         "Select document type:",
#         options=["prescription", "patient_details"]
#     )
#
#     uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
#
#     submitted = st.form_submit_button("Extract Data")
#
# if submitted:
#     if uploaded_file is None:
#         st.error("Please upload a PDF file.")
#     else:
#         with st.spinner("Extracting data..."):
#             # Prepare the request
#             files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
#             data = {"file_data": file_data}
#
#             try:
#                 response = requests.post(API_URL, data=data, files=files)
#                 result = response.json()
#
#                 if "error" in result:
#                     st.error(f"❌ Error: {result['error']}")
#                 else:
#                     st.success("✅ Extraction Successful")
#                     st.subheader("Extracted Information:")
#                     st.json(result)
#             except Exception as e:
#                 st.error(f"⚠️ Could not connect to the API. Error: {str(e)}")



