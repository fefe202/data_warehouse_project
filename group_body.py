import pandas as pd

# mapping da body originale → macro-categoria
body_map = {
    'Suv': 'SUV',
    'Hatchback': 'Hatchback',
    'Sedan': 'Sedan',
    'G Sedan': 'Sedan',
    'Coupe': 'Coupe',
    'G Coupe': 'Coupe',
    'Elantra Coupe': 'Coupe',
    'Genesis Coupe': 'Coupe',
    'Cts Coupe': 'Coupe',
    'Koup': 'Coupe',
    'Q60 Coupe': 'Coupe',
    'G37 Coupe': 'Coupe',
    'Cts V Coupe': 'Coupe',
    'Convertible': 'Convertible',
    'G Convertible': 'Convertible',
    'Beetle Convertible': 'Convertible',
    'G37 Convertible': 'Convertible',
    'Q60 Convertible': 'Convertible',
    'Wagon': 'Wagon',
    'Cts Wagon': 'Wagon',
    'Tsx Sport Wagon': 'Wagon',
    'Van': 'Van',
    'E Series Van': 'Van',
    'Promaster Cargo Van': 'Van',
    'Ram Van': 'Van',
    'Transit Van': 'Van',
    'Minivan': 'Minivan',
    'Regular Cab': 'Pickup Cab',
    'Access Cab': 'Pickup Cab',
    'King Cab': 'Pickup Cab',
    'Double Cab': 'Pickup Cab',
    'Quad Cab': 'Pickup Cab',
    'Crew Cab': 'Pickup Cab',
    'Cab Plus': 'Pickup Cab',
    'Cab Plus 4': 'Pickup Cab',
    'Club Cab': 'Pickup Cab',
    'Mega Cab': 'Pickup Cab',
    'Xtracab': 'Pickup Cab',
    'Supercab': 'Pickup Cab',
    'Supercrew': 'Pickup Cab',
    'Crewmax Cab': 'Pickup Cab',
    'Extended Cab': 'Pickup Cab',
}

# 1) Carica il CSV
df = pd.read_csv('car_prices_random_date.csv')

# 2) Sovrascrivi body con la macro-categoria (o lascia l’originale se non presente)
df['body'] = df['body'].map(body_map).fillna(df['body'])

# 3) (Opzionale) Verifica i valori unici
print(df['body'].unique())

# 4) Salva
df.to_csv('car_prices_grouped_body.csv', index=False)
print("Done: 'body' aggiornata in car_prices_grouped_body.csv")
