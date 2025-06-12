import pandas as pd

# Parametri modificabili
csv_input = 'car_prices_reformatted_date.csv'
csv_output = 'car_prices_without_outliers.csv'
colonna_prezzo = 'sellingprice'
# Consiglio: moltiplicatore IQR tipico è 1.5; per rimozione più selettiva si può salire a 2 o 2.5
iqr_multiplier = 1.5  

# 1. Leggi il CSV
df = pd.read_csv(csv_input)

# 2. Calcola Q1, Q3 e IQR
Q1 = df[colonna_prezzo].quantile(0.25)
Q3 = df[colonna_prezzo].quantile(0.75)
IQR = Q3 - Q1

# 3. Definisci limiti
lower_bound = Q1 - iqr_multiplier * IQR
upper_bound = Q3 + iqr_multiplier * IQR

# 4. Filtra il DataFrame
df_filtered = df[(df[colonna_prezzo] >= lower_bound) & (df[colonna_prezzo] <= upper_bound)]

# 5. Salva risultato
df_filtered.to_csv(csv_output, index=False)

# Output informazioni a video
print(f"Record originali: {len(df)}, dopo filtro: {len(df_filtered)}")
print(f"Soglie usate: lower={lower_bound:.2f}, upper={upper_bound:.2f}")
