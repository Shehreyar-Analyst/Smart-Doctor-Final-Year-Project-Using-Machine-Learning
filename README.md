# 🩺 Smart Doctor – Disease Prediction Using Machine Learning

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)  
[![License](https://img.shields.io/badge/License-Academic-green)](#license)

---

## 📌 Project Overview

**Smart Doctor** is a desktop-based disease prediction system developed using **Python** and **PyQt5** that leverages machine learning algorithms to predict possible diseases based on user-input symptoms. The system uses three major ML models — Naïve Bayes, Decision Tree, and Random Forest — trained on a curated dataset of 40+ diseases and 100+ unique symptoms.

This project aims to reduce the cost and time of medical diagnosis by allowing users to get a preliminary prediction of potential diseases from their symptoms without immediately visiting a doctor. The user-friendly graphical interface makes it accessible even for non-technical users.

---

## 🚀 Features

- **Multiple Machine Learning Algorithms:**  
  Naïve Bayes, Decision Tree, Random Forest for improved prediction accuracy.

- **Extensive Disease Database:**  
  Over 40 diseases with 100+ symptoms including common illnesses like malaria, flu, diabetes, etc.

- **User-Friendly GUI:**  
  Built with PyQt5, simple symptom selection and disease prediction interface.

- **Voice Output:**  
  System can read out disease details using Windows SAPI.voice API.

- **Offline Functionality:**  
  Does not require internet connection after setup.

- **Excel-Based Dataset:**  
  Dataset stored in Excel format for easy modifications and updates.

---

## 🎯 Objectives

- Provide a **cost-effective** tool for preliminary disease diagnosis.  
- Save users' **time** by predicting diseases based on symptoms.  
- Assist healthcare professionals with a quick symptom-based prediction tool.  
- Develop an **intuitive interface** usable by non-technical people.  

---

## 🧰 Tech Stack & Libraries

| Technology | Purpose                           |
|------------|---------------------------------|
| Python 3.9+| Core development language        |
| PyQt5      | Desktop GUI framework            |
| Scikit-learn| Machine learning algorithms      |
| Pandas     | Data processing and management  |
| NumPy      | Numerical operations             |
| Excel      | Dataset storage                  |
| SAPI.voice | Voice synthesis (Windows only)  |

---

## 🏗️ System Architecture

The system follows a modular architecture:

1. **Data Preprocessing:**  
   Raw symptom and disease data from Excel is cleaned and formatted.

2. **Model Training:**  
   Three ML models are trained on the dataset — Naïve Bayes, Decision Tree, and Random Forest.

3. **GUI Interface:**  
   PyQt5-based interface allows users to enter their name, select symptoms, and get predictions.

4. **Prediction & Output:**  
   Models predict diseases based on selected symptoms; results with descriptions and precautions are displayed and optionally read aloud.

---

## 📷 Screenshots

![image](https://github.com/user-attachments/assets/d322840d-18e7-45ff-a358-8e652c47ff21)
![image](https://github.com/user-attachments/assets/86c6be98-8120-463f-8ba3-2b792feab388)
![image](https://github.com/user-attachments/assets/21741033-2de0-4013-85f3-2d557c6d5fca)
![image](https://github.com/user-attachments/assets/3fdd3c88-2d37-4849-bc98-a8b67df163bd)





---

## 🔧 Installation & Setup

### Prerequisites

- Python 3.9 or higher installed.  
- Windows OS (recommended for SAPI.voice functionality).  
- Basic Python packages: PyQt5, scikit-learn, pandas, numpy.

### Steps

1. Clone the repository:

```bash
git clone https://github.com/Shehreyar-Analyst/Smart-Doctor-Final-Year-Project-Using-Machine-Learning.git
cd Smart-Doctor-Final-Year-Project-Using-Machine-Learning
