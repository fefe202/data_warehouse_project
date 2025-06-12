import pandas as pd

# Legge il dataset dal file CSV
df = pd.read_csv('car_prices_cleaned.csv')

# Sostituisce i valori '+' e '!' in "trim" con "Base"
df['trim'] = df['trim'].replace({'+': 'Base', '!': 'Base'})

# Salva il DataFrame modificato in un nuovo file CSV
df.to_csv('car_prices_adjusted_trim.csv', index=False)

# Visualizza le prime righe per verificare le modifiche
print(df.head())
