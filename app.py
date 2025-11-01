import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from data_utils import load_rainfall_data, fetch_crop_data, top_k_states_by_crop

# Load environment variables
load_dotenv()

# Page setup
st.set_page_config(page_title="🌾 Build For Bharat", layout="centered")
st.title("🌾 Build For Bharat — Agriculture & Climate Q&A")

# API setup (now loaded from .env)
API_KEY = os.getenv("API_KEY")
RAIN_PATH = os.getenv("RAIN_PATH")

# Load rainfall data
rain_df = load_rainfall_data(RAIN_PATH)
if not rain_df.empty:
    st.success(f"✅ Local rainfall data loaded successfully ({len(rain_df)} rows).")
else:
    st.error("❌ Could not load rainfall data. Check file path or format.")

# Fetch crop data via API
crop_df = fetch_crop_data(API_KEY)
if not crop_df.empty:
    st.success(f"✅ Live crop data fetched successfully ({len(crop_df)} records).")
else:
    st.warning("⚠️ No crop data found or API returned empty response.")

# Helper function
def compare_rainfall(df, district1, district2, year):
    try:
        cols = [c.lower() for c in df.columns]
        dist_col = next((c for c in df.columns if "district" in c.lower()), None)
        year_col = f"{year} Actual Rainfall"
        if not dist_col or year_col not in df.columns:
            return "Columns not found in rainfall data."
        d1 = df[df[dist_col].str.contains(district1, case=False, na=False)]
        d2 = df[df[dist_col].str.contains(district2, case=False, na=False)]
        if d1.empty or d2.empty:
            return "District(s) not found."
        r1 = float(d1[year_col].mean())
        r2 = float(d2[year_col].mean())
        more = district1 if r1 > r2 else district2
        diff = abs(r1 - r2)
        return f"🌧️ {district1}: {r1:.1f} mm\n🌧️ {district2}: {r2:.1f} mm\n💧 {more.upper()} had {diff:.1f} mm higher rainfall."
    except Exception as e:
        return f"Error comparing rainfall: {e}"

# Input box
st.markdown("💬 **Ask a question about rainfall or crops**")
st.caption("Examples:\n• Compare rainfall between BHOPAL and INDORE for 2013\n• Top 5 states producing Wheat")

query = st.text_input("Type your question:")

if query:
    q_lower = query.lower()

    # Rainfall comparison
    if "compare" in q_lower and "rainfall" in q_lower:
        parts = query.split()
        districts = [p for p in parts if p.isalpha()]
        year = next((p for p in parts if p.isdigit()), None)
        if len(districts) >= 4 and year:
            d1, d2 = districts[-4], districts[-2]
            result = compare_rainfall(rain_df, d1, d2, year)
            st.markdown(result)
        else:
            st.warning("Please specify two districts and a year.")
    
    # Top crop-producing states
    elif "top" in q_lower and "state" in q_lower and "crop" in q_lower:
        words = query.split()
        k = next((int(w) for w in words if w.isdigit()), 5)
        crop_name = next((w for w in words if w.isalpha() and w.lower() not in ["top", "states", "producing", "in", "for", "crop"]), "Wheat")
        result = top_k_states_by_crop(crop_df, crop_name, k)
        if result.empty:
            st.warning("No matching crop data found.")
            st.json(list(crop_df.columns))
        else:
            st.dataframe(result)
    else:
        st.info("Try asking about rainfall comparison or top crops.")

# Data previews
st.divider()
if st.button("📊 Show Rainfall Data Preview"):
    st.dataframe(rain_df.head())

if st.button("🌾 Show Crop Data Preview"):
    st.dataframe(crop_df.head())
