import pandas as pd
import random

# 1) Carica il CSV
df = pd.read_csv('car_prices_adjusted_state.csv')

# 2) Estrai i colori validi per ciascuna colonna
valid_exterior = df.loc[df['color'] != '—', 'color'].dropna().unique().tolist()
valid_interior = df.loc[df['interior'] != '—', 'interior'].dropna().unique().tolist()

# 3) Costruisci i dizionari e stampali per verifica
exterior_dict = {i: c for i, c in enumerate(valid_exterior)}
interior_dict = {i: c for i, c in enumerate(valid_interior)}
print("Dizionario colori esterni:", exterior_dict)
print("Dizionario colori interni:", interior_dict)

# 4) Sostituisci i placeholder "—" in ciascuna colonna
mask_ext = df['color'] == '—'
mask_int = df['interior'] == '—'

df.loc[mask_ext, 'color'] = df.loc[mask_ext, 'color'].apply(lambda _: random.choice(valid_exterior))
df.loc[mask_int, 'interior'] = df.loc[mask_int, 'interior'].apply(lambda _: random.choice(valid_interior))

# 5) (Facoltativo) Verifica che non ci siano più "—"
print("Esterni rimasti “—”:", df['color'].eq('—').sum())
print("Interni rimasti “—”:", df['interior'].eq('—').sum())

# 6) Salva il risultato
df.to_csv('car_prices_adjusted_color_and_interior.csv', index=False)
print("Fatto! Vedi 'car_prices_adjusted_color_and_interior.csv'.")
