import pandas as pd

# 1. Carica il dataset con fuel_consumption già normalizzato a numeric/NaN
df = pd.read_csv('car_prices_with_fuel_consumption.csv')

# 2. Assicura che 'fuel_consumption' sia numerico
df['fuel_consumption'] = pd.to_numeric(df['fuel_consumption'], errors='coerce')

# 3. Uniforma casing per make e body
df['make'] = df['make'].str.strip().str.upper()
df['body'] = df['body'].str.strip().str.upper()

# 4. Conta valori mancanti iniziali
initial_missing = df['fuel_consumption'].isna().sum()

# 5. Salva copia dei valori originali
df['fuel_orig'] = df['fuel_consumption']

# === PASSATA 1: imputazione make–body–year ===
group1 = (
    df.loc[df['fuel_orig'].notna()]
      .groupby(['make','body','year'])['fuel_orig']
      .mean()
      .reset_index(name='mean_mb_year')
)
df = df.merge(group1, on=['make','body','year'], how='left')
df['fuel_consumption'] = df['fuel_consumption'].fillna(df['mean_mb_year'])

# === PASSATA 2: imputazione body–year ===
group2 = (
    df.loc[df['fuel_orig'].notna()]
      .groupby(['body','year'])['fuel_orig']
      .mean()
      .reset_index(name='mean_b_year')
)
df = df.merge(group2, on=['body','year'], how='left')
df['fuel_consumption'] = df['fuel_consumption'].fillna(df['mean_b_year'])

# === PASSATA 3: imputazione body ===
group3 = (
    df.loc[df['fuel_orig'].notna()]
      .groupby('body')['fuel_orig']
      .mean()
      .reset_index(name='mean_b')
)
df = df.merge(group3, on='body', how='left')
df['fuel_consumption'] = df['fuel_consumption'].fillna(df['mean_b'])

# 6. Conta valori mancanti dopo le tre passate
final_missing = df['fuel_consumption'].isna().sum()
filled = initial_missing - final_missing

print(f"Valori mancanti iniziali: {initial_missing}")
print(f"Valori mancanti dopo 3 passate: {final_missing}")
print(f"Totale imputati: {filled}")

# 7. Pulisci colonne ausiliarie
df = df.drop(columns=['fuel_orig', 'mean_mb_year', 'mean_b_year', 'mean_b'])

# 8. Salva il dataset finale
output_path = 'car_prices_with_fuel_completed.csv'
df.to_csv(output_path, index=False)
print(f"Dataset definitivo salvato in: {output_path}")
