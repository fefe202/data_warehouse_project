import pandas as pd

# 1) Carica il CSV
df = pd.read_csv('car_prices_without_outliers.csv')

# 2) Pulisci la colonna 'body'
df['body'] = (
    df['body']
    # Trasforma i trattini in spazi
    .str.replace('-', ' ', regex=False)
    # Porta tutto in minuscolo e rimuovi spazi iniziali/finali
    .str.lower().str.strip()
    # Rimpiazza eventuali spazi doppi con uno singolo
    .str.replace(r'\s+', ' ', regex=True)
    # Trasforma in Title Case, cioè ogni parola con iniziale maiuscola
    .str.title()
)

# 3) (Facoltativo) Controlla le uniche categorie rimaste
print("Valori unici in 'body' dopo la pulizia:")
print(df['body'].unique())

# 4) Salva il CSV ripulito
df.to_csv('car_prices_adjusted_body.csv', index=False)

print("Pulizia completata: vedi 'car_prices_adjusted_body.csv'.")
