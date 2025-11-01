🌾 Agriculture & Climate Q&A

📘 Overview
This is a Streamlit-based web application that allows users to explore and analyze agriculture and climate data of India.  
It combines district-level rainfall data with real-time crop data fetched from the [data.gov.in API](https://data.gov.in/).

Users can ask natural-language questions such as:
- Compare rainfall between Bhopal and Indore for 2013  
- Display rainfall data preview  

---

 🚀 Features
- 📊 Load local rainfall dataset (ODS/CSV/XLSX)
- 🌾 Fetch real-time crop production data using API
- 💬 Ask natural-language questions about rainfall or crops
- ⚙️ Uses `.env` file for secure API key storage
- 📈 Display tabular insights using Streamlit interface

---

🧰 Tech Stack
- Python 3
- Streamlit — for interactive web app
- Pandas — for data manipulation
- Requests — for API calls



⚙️ Installation & Setup

1️⃣ Clone the Repository
```bash
        git clone https://github.com/mohdfaizfaizii/project-samarth.git
        cd project-samarth
      - python-dotenv — for environment variables

2️⃣ (Optional) Create Virtual Environment and Activate
python -m venv venv  
venv\Scripts\activate         # Windows  
# or  
source venv/bin/activate      # Mac/Linux  
