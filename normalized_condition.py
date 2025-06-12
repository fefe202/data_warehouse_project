import pandas as pd

# Legge il dataset dal file CSV
df = pd.read_csv('car_prices_adjusted_trim.csv')

# Definisce gli intervalli e le etichette per le categorie
bins = [0, 9, 19, 29, 39, 49]  
labels = ['Extremely Used', 'Heavily Used', 'Moderately Used', 'Lightly Used', 'Like New']

# Sostituisce direttamente nella colonna "condition" i valori numerici con le categorie
df['condition'] = pd.cut(df['condition'], bins=bins, labels=labels, include_lowest=True)

# Visualizza le prime righe per verificare la normalizzazione
print(df[['condition']].head())

# Salva il DataFrame modificato in un nuovo file CSV
df.to_csv('car_prices_normalized_condition.csv', index=False)
