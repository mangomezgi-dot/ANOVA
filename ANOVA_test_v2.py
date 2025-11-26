import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
df = pd.read_csv("ANOVA_input.txt", sep="\t")

# Convertir a categóricas donde aplique
categorical_vars = [
    'cell_line', 'agent', 'treatment_time', 'medium_type',
    'resazurin_concentration', 'medium_replacement', 'antibiotics'
]

for col in categorical_vars:
    df[col] = df[col].astype('category')

# Definir fórmula, modelo lineal que pude entender gracias al codigo de R
formula = 'cell_viability ~ cell_line + agent + dose + treatment_time + medium_type + medium_volume + seeding_density + resazurin_concentration + resazurin_time + medium_replacement + antibiotics'

# Ajustar modelo lineal
model = ols(formula, data=df).fit()

# ANOVA tipo I (artículo)
anova_table = sm.stats.anova_lm(model, typ=1)

# Calcular -log10(p) para graficar
anova_table['-log10(p)'] = -np.log10(anova_table['PR(>F)'].replace(0, 1e-300))
anova_table = anova_table.sort_values('-log10(p)', ascending=False)
# anova_table.reset_index(inplace=True)

# Graficar estilo Figura 4
plt.figure(figsize=(10, 6))
sns.barplot(x=anova_table.index, y=anova_table['-log10(p)'], color='gray')

# Línea roja para significancia p=0.05
plt.axhline(-np.log10(0.05), color='red', linestyle='--', label='p = 0.05')

plt.xticks(rotation=45, ha='right')
plt.ylabel('-log10(p-valor)', fontsize=14)
plt.xlabel('Covariables', fontsize=14)
plt.title('Influencia de parámetros experimentales sobre viabilidad celular\n', fontsize=14)
plt.tight_layout()
sns.despine(top=True, right=True)

plt.savefig("ANOVA.png",
            dpi=300,
            bbox_inches='tight',
            transparent=True)

plt.show()

print(" RESULTADOS DE LA ANOVA MULTIVARIADA: \n")
print(anova_table[['sum_sq', 'df', 'F', 'PR(>F)']].round(4).rename_axis("Variable"))
