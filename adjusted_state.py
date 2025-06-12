import pandas as pd

# Dizionario di mapping da abbreviazione a nome completo
state_map = {
    'AL': 'Alabama',        'AK': 'Alaska',         'AZ': 'Arizona',
    'AR': 'Arkansas',       'CA': 'California',     'CO': 'Colorado',
    'CT': 'Connecticut',    'DE': 'Delaware',       'FL': 'Florida',
    'GA': 'Georgia',        'HI': 'Hawaii',         'ID': 'Idaho',
    'IL': 'Illinois',       'IN': 'Indiana',        'IA': 'Iowa',
    'KS': 'Kansas',         'KY': 'Kentucky',       'LA': 'Louisiana',
    'ME': 'Maine',          'MD': 'Maryland',       'MA': 'Massachusetts',
    'MI': 'Michigan',       'MN': 'Minnesota',      'MS': 'Mississippi',
    'MO': 'Missouri',       'MT': 'Montana',        'NE': 'Nebraska',
    'NV': 'Nevada',         'NH': 'New Hampshire',  'NJ': 'New Jersey',
    'NM': 'New Mexico',     'NY': 'New York',       'NC': 'North Carolina',
    'ND': 'North Dakota',   'OH': 'Ohio',           'OK': 'Oklahoma',
    'OR': 'Oregon',         'PA': 'Pennsylvania',   'RI': 'Rhode Island',
    'SC': 'South Carolina', 'SD': 'South Dakota',   'TN': 'Tennessee',
    'TX': 'Texas',          'UT': 'Utah',           'VT': 'Vermont',
    'VA': 'Virginia',       'WA': 'Washington',     'WV': 'West Virginia',
    'WI': 'Wisconsin',      'WY': 'Wyoming',
    'PR': 'Puerto Rico'
}

# 1) Carica il dataset (modifica il path/filename a piacere)
df = pd.read_csv('car_prices_adjusted_body.csv')

# 2) Sovrascrivi la colonna 'state' con i nomi completi
df['state'] = (
    df['state']
      .str.strip()      # rimuove spazi accidentali
      .str.upper()      # converte in maiuscolo per far combaciare le chiavi
      .map(state_map)   # mappa con il dizionario
      .fillna('Unknown')# sostituisce eventuali codici non riconosciuti
)

# 3) Salva il risultato
df.to_csv('car_prices_adjusted_state.csv', index=False)

print("Conversione completata, vedi 'car_prices_adjusted_state.csv'")
