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
- python-dotenv — for environment variables  

---

⚙️ Installation & Setup

1️⃣ Clone the Repository
```bash
git clone https://github.com/mohdfaizfaizii/project-samarth.git
cd project-samarth
````

---

2️⃣ (Optional) Create Virtual Environment and Activate

```bash
python -m venv venv
venv\Scripts\activate 
```

3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

4️⃣ Get Your API Key

👉 Go to [https://data.gov.in](https://data.gov.in)
👉 Login or create a free account
👉 Copy your API key from My Account → API Keys

---

5️⃣ Create `.env` File in the project root and add:

(You can create manually or use echo command below)

```bash
echo API_KEY=your_api_key_here > .env
echo RAIN_PATH=data/datafile.ods >> .env
```
---

6️⃣ Run the App

```bash
streamlit run app.py
```
---

📂 Project Structure

```
project-samarth/
│
├── app.py              # Main Streamlit app
├── data_utils.py       # Helper functions (API + data)
├── data/               # Local rainfall dataset
│   └── datafile.ods
├── .env                # API key file (not uploaded)
├── requirements.txt    # Dependencies list
└── README.md           # Documentation file
```
