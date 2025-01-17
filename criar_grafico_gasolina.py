import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

plt.figure(figsize=(10, 6))
plt.plot(df['dia'], df['venda'], label='Preço da gasolina')

plt.title('Preço médio de venda da gasolina na cidade de São Paulo nos 10 primeiros dias de Julho de 2021')
plt.xlabel('Dia')
plt.ylabel('Preço')
plt.grid(True)
plt.legend()
plt.savefig('gasolina_sp_10PrimeirosDiasJulho2021.png', format='png', dpi=72)
plt.show()