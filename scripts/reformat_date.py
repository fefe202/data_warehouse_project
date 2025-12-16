import pandas as pd

# 1. Leggi il CSV originale
df = pd.read_csv('car_prices_random_date.csv')

# 2. Rimuovi la parte tra parentesi tonde (es. " (PST)")
df['saledate_clean'] = df['saledate'].str.replace(r' \([^)]+\)$', '', regex=True)

# 3. Parsifica la data con il timezone offset GMT
df['saledate_dt'] = pd.to_datetime(
    df['saledate_clean'],
    format='%a %b %d %Y %H:%M:%S GMT%z'
)

# 4. Estrai solo la data e formattala ISO (YYYY-MM-DD)
df['saledate'] = df['saledate_dt'].dt.date.astype(str)

# 5. Elimina le colonne intermedie
df = df.drop(columns=['saledate_clean', 'saledate_dt'])

# 6. Salva il nuovo CSV pronto per Tableau
df.to_csv('car_prices_reformatted_date.csv', index=False)