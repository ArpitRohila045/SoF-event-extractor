# SoF-Event-Extractor

**Event extractor from PDFs/Words**

---

## 📌 Project Overview

**SoF-Event-Extractor** is a Django-based web application designed to automate the **extraction of structured events from Statement of Facts (SOF) documents**. These documents often contain complex, unstructured data that needs to be transformed into machine-readable formats for further analysis, reporting, or integration with downstream systems.

The platform supports:  
- Secure user authentication & document uploads.  
- File management for PDFs and Word documents.  
- Automated extraction pipeline integrating OCR & NLP models.  
- Linking each upload and extracted dataset to the corresponding user.  

---

## ✨ Key Features

- **🔐 User Authentication** — Sign-up, login, and session management.  
- **📂 Document Upload** — Upload and manage SOF documents in PDF or Word formats.  
- **👤 User Tracking** — Each uploaded file and extracted dataset is linked to the uploading user.  
- **⚙️ Extraction Pipeline** — OCR & NLP pipeline to parse unstructured text into structured data.  
- **🗄️ Data Models**  
  - **SOFDocument**: Stores uploaded files, file type, timestamp, and uploader.  
  - **SOFData**: Stores extracted and parsed event information.  
---

## 📊 Workflow: Event Extraction Pipeline

The **data pipeline** is structured as follows:

### 1. **Document Upload**
- User uploads a **PDF or Word** file.  
- Metadata (file type, uploader, timestamp) is stored in the `SOFDocument` model.  

### 2. **OCR & Text Extraction**
- For **scanned PDFs**, we use **Tesseract OCR** to convert images into text.  
  - Purpose: Extract raw text from image-based documents.  
- For **digital PDFs or Word files**, text is extracted directly.  

### 3. **Document Parsing & Preprocessing**
- Clean text (remove noise, normalize formatting).  
- Segment into sections (e.g., date, events, remarks).  

### 4. **Entity Extraction with NLP**
- Apply **LayoutLMv3** (a Transformer-based Document Understanding Model).  
  - Purpose: Extract **key entities and structured data** while leveraging both text and layout (spatial positioning).  
  - Example Entities: Timestamps, vessel details, cargo info, port activities.  

### 5. **Data Storage**
- Structured output saved in **SOFData** model.  
- Linked back to the source `SOFDocument` and the uploading `User`.  

### 6. **Visualization & Export** *(future roadmap)*
- Extracted events can be visualized in tables, timelines, or exported as CSV/JSON for analytics.  

---

## 🧠 Pipeline Components

| Stage                 | Tool/Model       | Purpose                                                                 |
|------------------------|-----------------|-------------------------------------------------------------------------|
| **OCR**               | Tesseract OCR   | Convert scanned PDFs/images into machine-readable text.                  |
| **NLP for SOF Parsing** | LayoutLMv3      | Transformer model that leverages text + layout for key entity extraction.|
| **Framework**         | Django + SQLite/Postgres | Manage users, documents, and extracted event data.                  |
| **Future Add-ons**    | PyTorch / HuggingFace | Fine-tune LayoutLMv3 for domain-specific SOF extraction.                |

---

## 📂 Project Structure
```
SoF-event-extractor/
├── pipeline/ # App for document upload & processing
│ ├── models.py # SOFDocument, SOFData models
│ ├── forms.py # File upload form
│ ├── views.py # Upload & processing views
│ ├── urls.py # Upload routes
│ └── templates/
│ └── pipeline/
│ ├── upload.html
│ └── upload_success.html
├── user_auth/
│ ├── models.py # User model
│ ├── forms.py # Signup/Login forms
│ ├── views.py # Authentication views
│ └── urls.py
├── base/ # Home app
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Getting Started

### 1. Clone the Repository

```git clone https://github.com/ArpitRohila045/SoF-event-extractor.git```
```cd SoF-event-extractor```

### 2. Create Virtual Environment & Install Dependencies
```python3 -m venv venv```
```source venv/bin/activate```
```pip install -r requirements.txt```

### 3. Run Migrations
```python manage.py makemigrations```
```python manage.py migrate```

### 4. Create a Superuser
```python manage.py createsuperuser```

### 5. Run the Development Server
```python manage.py runserver```

