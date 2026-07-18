import os
import pandas as pd
import numpy as np

def clean_count_series(series):
    # Convert series to numeric, replacing NaNs and redacted '***' or '.' with 0
    s = series.astype(str).str.replace(',', '').str.strip()
    s = pd.to_numeric(s, errors='coerce').fillna(0)
    return s.astype(int)

def read_raw_csv(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Required file not found: {path}")
    
    # Detect encoding
    encoding = 'utf-8'
    with open(path, 'rb') as f:
        first_bytes = f.read(4)
        if first_bytes.startswith(b'\xff\xfe') or first_bytes.startswith(b'\xfe\xff'):
            encoding = 'utf-16'

    # Detect delimiter
    try:
        with open(path, 'r', encoding=encoding) as f:
            first_line = f.readline()
            sep = '\t' if '\t' in first_line else ','
        df = pd.read_csv(path, encoding=encoding, sep=sep)
    except Exception:
        df = pd.read_csv(path)
    
    # Standardize column names (strip whitespace)
    df.columns = [col.strip() for col in df.columns]
    return df

def prepare_all_data(data_dir="data"):
    print("--- Preparing Data (Clean & Cast) ---")
    data_files = {
        "plan_academicLevel": "plan_academicLevel.csv",
        "plan_legalSex": "plan_legalSex.csv",
        "plan_residency": "plan_residency.csv",
        "plan_citizenship": "plan_citizenship.csv",
        "plan_race": "plan_race.csv",
        "plan_termAdmitType": "plan_termAdmitType.csv",
        "plan_fullTimePartTime": "plan_fullTimePartTime.csv",
        
        "school_legalSex": "school_legalSex.csv",
        "school_residency": "school_residency.csv",
        "school_citizenship": "school_citizenship.csv",
        "school_race": "school_race.csv",
        "school_termAdmitType": "school_termAdmitType.csv",
        "school_age": "school_age.csv",
        
        "level_legalSex": "level_legalSex.csv",
        "level_residency": "level_residency.csv",
        "level_citizenship": "level_citizenship.csv",
        "level_race": "level_race.csv",
        "level_termAdmitType": "level_termAdmitType.csv",
        "level_age": "level_age.csv",
        
        "credits_academicLevel": "credits_academicLevel.csv",
        "wisconsinCounty_academicLevel": "wisconsinCounty_academicLevel.csv",
        "usState_academicLevel": "usState_academicLevel.csv",
        "country_academicLevel": "country_academicLevel.csv",
        
        "wisconsinCounty_residency": "wisconsinCounty_residency.csv",
        "usState_residency": "usState_residency.csv",
        "country_residency": "country_residency.csv",
        "wisconsinCounty_termAdmitType": "wisconsinCounty_termAdmitType.csv",
        "usState_termAdmitType": "usState_termAdmitType.csv",
        "country_admitType": "country_admitType.csv",
        "internationalCountry_academicLevel": "internationalCountry_academicLevel.csv",
        
        "wisconsinCounty_map": "wisconsinCounty_map.csv",
        "usMap": "usMap.csv",
        "worldMap": "worldMap.csv",
        
        "highSchoolName_legalSex": "highSchoolName_legalSex.csv",
        "transfer_legalSex": "transfer_legalSex.csv",
        
        "grade_distribution": "grade_distribution_parsed.csv",
        "gpa_parsed": "gpa_parsed.csv",
    }
    
    dfs = {}
    for key, filename in data_files.items():
        path = os.path.join(data_dir, filename)
        df = read_raw_csv(path)
        
        # 1. Strip all string cells in the DataFrame
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].astype(str).str.strip()
            
        # 2. Clean count columns to actual integers
        for col in df.columns:
            col_lower = col.lower()
            if "count" in col_lower or "student" in col_lower:
                # Gating to prevent cleaning country, county, school, or level text columns
                if "level" not in col_lower and "school" not in col_lower and "country" not in col_lower and "county" not in col_lower:
                    df[col] = clean_count_series(df[col])
                    
        # 3. Specific table formatting
        if key == "credits_academicLevel":
            df["Credits Enrolled"] = pd.to_numeric(df["Credits Enrolled"], errors='coerce').fillna(15).astype(int)
            
        elif key in ["wisconsinCounty_map", "usMap", "worldMap"]:
            df["Latitude (generated)"] = pd.to_numeric(df["Latitude (generated)"], errors='coerce').fillna(43.0731)
            df["Longitude (generated)"] = pd.to_numeric(df["Longitude (generated)"], errors='coerce').fillna(-89.4012)
            
        elif key == "grade_distribution":
            # Only keep sections (exclude totals)
            df = df[df["is_course_total"] == False].copy()
            df["grades_count"] = clean_count_series(df["grades_count"])
            df = df[df["grades_count"] > 0]
            df["section_id"] = range(1, len(df) + 1)
            
            # Cast grade percentage columns to clean floats
            grade_cols = ['A_pct', 'AB_pct', 'B_pct', 'BC_pct', 'C_pct', 'D_pct', 'F_pct', 
                          'S_pct', 'U_pct', 'CR_pct', 'N_pct', 'P_pct', 'I_pct', 'NW_pct', 'NR_pct', 'other_pct']
            for gcol in grade_cols:
                df[gcol] = df[gcol].replace('.', '0').replace('nan', '0').replace('', '0')
                df[gcol] = pd.to_numeric(df[gcol], errors='coerce').fillna(0.0)
                
        dfs[key] = df
        
    return dfs

if __name__ == "__main__":
    prepare_all_data()
