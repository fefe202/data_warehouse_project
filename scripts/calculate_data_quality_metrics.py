import pandas as pd
import numpy as np

def calculate_data_quality_metrics(csv_file):
    """Calcola le 5 metriche di qualità dati per report"""
    
    df = pd.read_csv(csv_file)
    total_records = len(df)
    total_cells = df.size
    
    # 1. VALIDITY - % conformi al dominio
    validity_checks = 0
    validity_passed = 0
    
    # Anno valido (1900-2025)
    if 'year' in df.columns:
        validity_checks += total_records
        validity_passed += ((df['year'] >= 1900) & (df['year'] <= 2025)).sum()
    
    # VIN valido (17 caratteri)
    if 'vin' in df.columns:
        validity_checks += total_records
        validity_passed += (df['vin'].astype(str).str.len() == 17).sum()
    
    # Odometro valido (0-500000)
    if 'odometer' in df.columns:
        validity_checks += total_records
        validity_passed += ((df['odometer'] >= 0) & (df['odometer'] <= 500000)).sum()
    
    # Condizione valida (1-50)
    if 'condition' in df.columns:
        validity_checks += total_records
        validity_passed += ((df['condition'] >= 1) & (df['condition'] <= 50)).sum()
    
    # Prezzi validi
    if 'sellingprice' in df.columns:
        validity_checks += total_records
        validity_passed += ((df['sellingprice'] >= 500) & (df['sellingprice'] <= 200000)).sum()
    
    validity = (validity_passed / validity_checks * 100) if validity_checks > 0 else 100
    
    # 2. COMPLETENESS - % non nulli
    completeness = (df.notna().sum().sum() / total_cells) * 100
    
    # 3. CONSISTENCY - % compatibili
    consistency_checks = 0
    consistency_passed = 0
    
    # MMR vs Selling Price (differenza < 30%)
    if 'mmr' in df.columns and 'sellingprice' in df.columns:
        mmr_vals = pd.to_numeric(df['mmr'], errors='coerce')
        price_vals = pd.to_numeric(df['sellingprice'], errors='coerce')
        valid_pairs = (mmr_vals.notna() & price_vals.notna())
        
        if valid_pairs.sum() > 0:
            consistency_checks += valid_pairs.sum()
            diff_pct = abs((mmr_vals - price_vals) / mmr_vals) * 100
            consistency_passed += (diff_pct <= 30).sum()
    
    # Year vs Sale Date
    if 'year' in df.columns and 'saledate' in df.columns:
        years = pd.to_numeric(df['year'], errors='coerce')
        # Corretto: specificato utc=True e controllato se la conversione è riuscita
        sale_dates = pd.to_datetime(df['saledate'], errors='coerce', utc=True, infer_datetime_format=False)
        valid_pairs = (years.notna() & sale_dates.notna())
        
        if valid_pairs.sum() > 0:
            consistency_checks += valid_pairs.sum()
            valid_sale_dates = sale_dates[valid_pairs]
            valid_years = years[valid_pairs]
            if len(valid_sale_dates) > 0:
                sale_years = valid_sale_dates.dt.year
                consistency_passed += (sale_years >= valid_years).sum()
    
    consistency = (consistency_passed / consistency_checks * 100) if consistency_checks > 0 else 85
    
    # 4. UNIQUENESS - % non duplicati
    total_rows = len(df)
    unique_rows = len(df.drop_duplicates())
    uniqueness = (unique_rows / total_rows) * 100
    
    return validity, completeness, consistency, uniqueness

# ESECUZIONE
if __name__ == "__main__":
    csv_file = "car_prices.csv"
    
    try:
        validity, completeness, consistency, uniqueness = calculate_data_quality_metrics(csv_file)
        
        print("METRICHE QUALITÀ DATI:")
        print(f"Validity: {validity:.2f}%")
        print(f"Completeness: {completeness:.2f}%") 
        print(f"Consistency: {consistency:.2f}%")
        print(f"Uniqueness: {uniqueness:.2f}%")
        
    except Exception as e:
        print(f"Errore: {e}")
