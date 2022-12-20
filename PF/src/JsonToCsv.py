import pandas as pd
df = pd.read_json (r'D:\tudo\Mestrado\IAA\Final\AprendizagemAutomatica\PF\src\data.json')
df.to_csv (r'D:\tudo\Mestrado\IAA\Final\AprendizagemAutomatica\PF\src\data1.csv', index = None)