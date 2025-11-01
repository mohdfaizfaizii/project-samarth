import pandas as pd
import requests

def load_rainfall_data(file_path="data/datafile.ods"):
    """Load rainfall dataset from local ODS/XLSX/CSV file."""
    try:
        if file_path.endswith(".ods"):
            df = pd.read_excel(file_path, engine="odf")
        elif file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path)
        elif file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        else:
            raise ValueError("Unsupported file format.")
        df.columns = [c.strip() for c in df.columns]
        return df
    except Exception as e:
        print("❌ Error loading rainfall data:", e)
        return pd.DataFrame()

def fetch_crop_data(api_key, resource_id="35be999b-0208-4354-b557-f6ca9a5355de", limit=5000):
    """Fetch crop data from data.gov.in API."""
    url = f"https://api.data.gov.in/resource/{resource_id}"
    params = {"api-key": api_key, "format": "json", "limit": limit}
    try:
        resp = requests.get(url, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json().get("records", [])
        if not data:
            return pd.DataFrame()
        df = pd.DataFrame(data)
        df.columns = [c.strip() for c in df.columns]
        return df
    except Exception as e:
        print("❌ Error fetching crop data:", e)
        return pd.DataFrame()

def get_rainfall_for_district_year(rain_df, district_name, year):
    """Get rainfall value for a specific district and year."""
    if rain_df is None or rain_df.empty:
        return None
    mask = rain_df[rain_df.columns[0]].astype(str).str.contains(district_name, case=False, na=False)
    matched = rain_df[mask]
    if matched.empty:
        return None
    year_col = f"{year} Actual Rainfall"
    if year_col not in rain_df.columns:
        return None
    try:
        val = matched.iloc[0][year_col]
        return float(val)
    except Exception:
        return None

def top_k_states_by_crop(crop_df, crop_name, k=5):
    """Find top K states producing a crop."""
    if crop_df is None or crop_df.empty:
        return pd.DataFrame()
    state_col, crop_col, prod_col = None, None, None
    for c in crop_df.columns:
        lc = c.lower()
        if "state" in lc and state_col is None:
            state_col = c
        if ("crop" in lc or "commodity" in lc) and crop_col is None:
            crop_col = c
        if ("production" in lc or "yield" in lc or "prod" in lc) and prod_col is None:
            prod_col = c
    if not (state_col and crop_col and prod_col):
        return pd.DataFrame()
    df = crop_df[[state_col, crop_col, prod_col]].copy()
    df[prod_col] = pd.to_numeric(df[prod_col], errors="coerce").fillna(0)
    filtered = df[df[crop_col].astype(str).str.contains(crop_name, case=False, na=False)]
    if filtered.empty:
        return pd.DataFrame()
    agg = filtered.groupby(state_col)[prod_col].sum().reset_index().sort_values(by=prod_col, ascending=False).head(k)
    return agg
