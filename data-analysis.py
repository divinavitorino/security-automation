#This is the .py file is a basic analysis of data correlation
#With this analysis it was possible to determine the correlation 
#between the data, eliminating the possibility that this correlation 
#occurred by chance.

#Data cleanup - it's important before starting the analysis to clean the data
#that is going to be used. That includes: removing blank, N/A and columns 
# that are not going to be used.

#vars - don't forget to change the names to the vars that are currently on your project
#colors - feel free to change the color of the graphics. Consult the package documentation
#on how to address it

#Library imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

#Create a dataframe with the imported data
df = pd.read_csv('answers.csv')

#Basic info of the dataset
print(df.shape)
print(df.info())
print(df.describe())

#Histogram
plt.hist(df["skill_jenkins"], bins=30, edgecolor="black")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()

#Boxplot
column = "diretorio_out_ad"

plt.figure(figsize=(6,4))
plt.boxplot(df[column], vert=False, patch_artist=True, boxprops=dict(facecolor="lightblue"))
plt.title(f"Boxplot de {column}")
plt.xlabel(column)
plt.show()

#Dispersion Graph
plt.scatter(df["skill_ansible"], df["atuacao_iam"])
plt.xlabel("Ansible")
plt.ylabel("iam")
plt.title("Gráfico de Dispersão")
plt.show()

#Heatmap Correlation Matrix

df_number = df.select_dtypes(include=["number"])
df_number = df_number.drop(columns=['skill_read_ingles'])
correlacao = df_number.corr().values
col = df_number.columns
fig, ax = plt.subplots(figsize=(8, 6))
cax = ax.matshow(correlacao, cmap="gray")  # Criar o heatmap
plt.colorbar(cax)  # Barra de cores
ax.set_xticks(np.arange(len(col)))
ax.set_yticks(np.arange(len(col)))
ax.set_xticklabels(col, rotation=90)
ax.set_yticklabels(col)
plt.title("Correlation Heatmap")
plt.show()


#Standard deviation
dev_std = df_number.std()
print(dev_std)

#Correlation matrix and p-value
df_number = df.select_dtypes(include=["number"])
matrix_final = []
for i, col1 in enumerate(df_number.columns):
    for j, col2 in enumerate(df_number.columns):
        if i < j:  # avoid autocorrelation
            correlation, p_value = pearsonr(df_number[col1], df_number[col2])
            df_result = pd.DataFrame({
                "Column1": [col1],
                "Column2": [col2],
                "Correlation": [round(correlation, 2)],
                "p-value": [round(p_value, 2)]
            })
            matrix_final.append(df_result)
results_df = pd.concat(matrix_final, ignore_index=True)
results_df.dropna(inplace=True)
print(results_df)
