# MediTruth-AI
AI-powered medical misinformation detection system using NLP, TF-IDF, cosine similarity and OCR.
# 🩺 MediTruth AI

### An Intelligent System for Medical Misinformation Detection

MediTruth AI is an AI-powered web application designed to analyze medical information and help identify potentially misleading or unverified medical content.

The system accepts both **text-based medical information** and **images containing medical text**. It uses Natural Language Processing (NLP), TF-IDF vectorization, cosine similarity, and Optical Character Recognition (OCR) to process and analyze the submitted content.

> ⚠️ **Disclaimer:** MediTruth AI is a supportive information-screening tool. It does not provide medical diagnosis, treatment recommendations, or professional medical advice.

---

## 📌 Project Overview

The rapid growth of social media, websites, messaging platforms, and online health content has increased the spread of medical misinformation.

MediTruth AI was developed to provide an automated method for analyzing medical content and helping users identify potentially unreliable information.

The system allows users to:

- Paste medical news or health-related text
- Upload an image containing medical information
- Extract text from images using OCR
- Preprocess the extracted or entered text
- Analyze the content using TF-IDF and cosine similarity
- Display the prediction result
- Provide a Google search option for further verification

The project is intended to promote responsible information sharing and encourage users to verify medical information through trusted sources.

---

## 🎯 Objectives

The main objectives of MediTruth AI are:

- To develop an intelligent system for analyzing medical content
- To detect potentially misleading or unverified medical information
- To process both text and image-based medical content
- To use NLP techniques for text preprocessing
- To use TF-IDF for text feature representation
- To use cosine similarity for content comparison
- To provide an easy-to-use web interface
- To support further verification through external search

---

## ✨ Features

### 📝 Medical Text Analysis
Users can directly paste medical news, articles, or health-related claims into the application.

### 🖼️ Image-Based Analysis
Users can upload an image containing medical information such as a screenshot, poster, or social-media message.

### 🔍 OCR Text Extraction
Tesseract OCR is used to extract readable text from uploaded images.

### 🧹 NLP Preprocessing
The system preprocesses text by:

- Converting text to lowercase
- Removing unwanted characters
- Removing stopwords
- Applying stemming

### 📊 TF-IDF Vectorization
TF-IDF converts processed text into numerical feature vectors for analysis.

### 📐 Cosine Similarity
Cosine similarity is used to measure the similarity between text representations.

### 🔎 Further Verification
The application provides a **Know More** option that allows users to search the analyzed medical content for additional verification.

---

## 🧠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Web application framework |
| HTML | Frontend structure |
| CSS | Interface styling |
| JavaScript | Client-side interaction |
| NLTK | Natural Language Processing |
| Scikit-learn | Machine learning and similarity calculation |
| TF-IDF | Text feature extraction |
| Cosine Similarity | Text similarity analysis |
| Tesseract OCR | Text extraction from images |
| PyTesseract | Python interface for Tesseract |
| Pillow | Image processing |
| Joblib | Model loading |
| Pandas | Data processing |

---

## 🔄 System Workflow

```text
User Input
    │
    ├── Medical Text
    │
    └── Medical Image
            │
            ▼
        OCR Extraction
            │
            ▼
     Text Preprocessing
            │
            ▼
      TF-IDF Vectorization
            │
            ▼
      Similarity Analysis
            │
            ▼
        Classification
            │
            ▼
       Result Display
            │
            ▼
      Further Verification
