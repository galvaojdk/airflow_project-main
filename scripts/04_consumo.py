import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Conectar ao banco
conn = sqlite3.connect('data/insidentes.db')

# Consulta
query = """
SELECT pais, COUNT(*) AS quantidade_ataques
FROM insidentes
GROUP BY pais
ORDER BY quantidade_ataques DESC
"""

# Obter os dados
df = pd.read_sql_query(query, conn)
conn.close()

# Plotar gráfico de barras horizontal com todos os países
plt.figure(figsize=(12, len(df) * 0.4))
plt.barh(df['pais'], df['quantidade_ataques'], color='steelblue')
plt.xlabel('Quantidade de Ataques')
plt.title('Quantidade de Ataques por País')
plt.gca().invert_yaxis()  # País com mais ataques no topo
plt.tight_layout()
plt.show()
