# 🩺 Medical Data Extraction Application

A powerful Python application designed to extract meaningful medical data from unstructured prescription text using rule-based parsing techniques. It offers both a backend API built with **FastAPI** and a sleek **Streamlit** frontend interface for healthcare practitioners, researchers, and developers to interact with.

---

## 📚 Table of Contents

- [About the Project](#about-the-project)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Architecture Overview](#architecture-overview)
- [Conclusion](#installation)

---

## 🧾 About the Project

Healthcare documents such as prescriptions often contain vital information scattered in free text. Extracting structured data like patient name, prescribed medications, dosage instructions, and doctor’s credentials manually is error-prone and inefficient.

This application automates that process, using Python and regular expressions to extract key information with high precision, making it easier to:
- Digitize paper prescriptions.
- Feed structured data into Electronic Health Records (EHR).
- Enable analytics and reporting.

---

## 🌟 Key Features

✅ Extracts:
- Patient name and address  
- Doctor’s name  
- Date of consultation  
- Medication names and dosages  
- Usage directions  
- Refill instructions  

✅ Modular regex-based extraction system  
✅ Clean and user-friendly web interface (Streamlit)  
✅ RESTful API for backend integration (FastAPI)  
✅ Easily customizable and extendable parser structure  

---

## 🛠️ Technology Stack

| Component   | Tech                         |
|------------|------------------------------|
| Backend     | FastAPI                      |
| Frontend    | Streamlit                    |
| Language    | Python 3.10+                 |
| Parsing     | Regular Expressions (re)     |
| Testing     | Pytest                       |
| OCR Support (Future) | pytesseract (planned) |

---

## 🏗️ Architecture Overview

The Medical Data Extraction app is structured into clearly separated backend and frontend components to enable modular development and deployment.


### Backend Component

The backend, built with FastAPI, contains all the document parsing logic. It exposes HTTP endpoints to accept raw medical text and return extracted information in JSON format. Core components include:

- **`extractor.py`** – Applies regular expressions to extract structured data such as patient details and medications.
- **`parser_generic.py`** – Abstract class for defining parsing templates that can be subclassed (e.g., for different regions or formats).
- **`api.py`** – FastAPI application with endpoints for real-time extraction.

### Frontend Component

The Streamlit frontend provides an easy-to-use interface for healthcare professionals or developers. It allows users to paste a medical note and view the extracted results instantly.

- Visualizes each parsed field clearly.
- Future enhancements can include OCR upload or batch file parsing.

---

## ✅ Conclusion

The Medical Data Extraction application offers a practical solution for converting unstructured prescription text into structured, usable medical data. With a focus on simplicity, modularity, and accuracy, this project is well-suited for healthcare digitization tasks, clinical data management, or as a base for larger EHR automation systems.

Whether you're a healthcare provider looking to streamline manual data entry or a developer aiming to build advanced healthcare tools, this project provides a clean starting point with extendable logic and modern web integration.

Feel free to fork, customize, and contribute to the project — together we can help make healthcare data smarter and more accessible.
