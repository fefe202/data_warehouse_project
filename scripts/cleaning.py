import pandas as pd

# Legge il dataset dal file CSV (assicurati di salvare il tuo dataset in 'dataset.csv')
df = pd.read_csv('car_prices_updated.csv')

# Conta il numero totale di record presenti nel dataset
total_records = len(df)

# Rimuove i record che contengono almeno un valore nullo
df_clean = df.dropna(how='any')

# Calcola quanti record sono stati rimossi
removed_records = total_records - len(df_clean)

# Calcola la percentuale di record rimossi
removed_percentage = (removed_records / total_records) * 100

# Stampa i risultati
print(f"Numero di record rimossi: {removed_records}")
print(f"Percentuale di record rimossi: {removed_percentage:.2f}%")

# Salva il dataset pulito in un nuovo file CSV
df_clean.to_csv('car_prices_cleaned.csv', index=False)
