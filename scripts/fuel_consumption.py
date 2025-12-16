import pandas as pd

# 1. Carica i dataset
df_prices = pd.read_csv('car_prices_with_land.csv')
df_fuel   = pd.read_csv('Fuel_Consumption_2000-2022.csv')

# 2. Normalizza i nomi dei modelli in maiuscolo per l'unione
df_prices['model_upper'] = df_prices['model'].str.upper()
df_fuel['MODEL_UPPER']   = df_fuel['MODEL'].str.upper()

# 3. Calcola il consumo medio per modello (colonna "FUEL CONSUMPTION")
df_fuel_mean = (
    df_fuel
    .groupby('MODEL_UPPER')['FUEL CONSUMPTION']
    .mean()
    .round(2)                       # arrotonda alla seconda cifra decimale
    .reset_index()
    .rename(columns={'FUEL CONSUMPTION': 'fuel_consumption'})
)

# 4. Unisci i due DataFrame sui modelli
df_enriched = df_prices.merge(
    df_fuel_mean,
    left_on='model_upper',
    right_on='MODEL_UPPER',
    how='left'
)

# Mostra quanti valori sono stati aggiunti
added = df_enriched['fuel_consumption'].notna().sum()
total = len(df_enriched)
print(f"Aggiunti valori di 'fuel_consumption' per {added} su {total} righe")

# 5. Riempi i mancanti con placeholder "N/A"
df_enriched['fuel_consumption'] = df_enriched['fuel_consumption'].fillna('N/A')

# 6. Pulisci colonne ausiliarie
df_enriched = df_enriched.drop(columns=['model_upper', 'MODEL_UPPER'])

# 7. Salva il risultato
output_path = 'car_prices_with_fuel_consumption.csv'
df_enriched.to_csv(output_path, index=False)

print(f"Dataset arricchito salvato in: {output_path}")
print(f"Valori mancanti di 'fuel_consumption' sostituiti con 'N/A'")
