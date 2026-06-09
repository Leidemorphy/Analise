import pandas as pd
import matplotlib.pyplot as plt

# =========================
# 1. CARREGAMENTO DOS DADOS
# =========================
df = pd.read_excel("messy_files_clean.xlsx")


# =========================
# 2. VISÃO GERAL DO DATASET
# =========================
print("\n=== INFO DO DATASET ===")
print(df.info())

print("\n=== VALORES NULOS ===")
print(df.isnull().sum())

print("\n=== ESTATÍSTICAS DESCRITIVAS ===")
print(df.describe())


# =========================
# 3. CRIAR COLUNA DE MÊS
# =========================
df["Month"] = df["Date"].dt.month_name()


# =========================
# 4. RECEITA POR REGIÃO
# =========================
receita_regiao = df.groupby("Region")["Total Sales"].sum().sort_values(ascending=False)

print("\n=== RECEITA POR REGIÃO ===")
print(receita_regiao)

plt.figure()
receita_regiao.plot(kind="bar")
plt.title("Receita por Região")
plt.xlabel("Região")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()


# =========================
# 5. PRODUTOS MAIS VENDIDOS (VOLUME)
# =========================
produtos_volume = df.groupby("Product")["Units Sold"].sum().sort_values(ascending=False)

print("\n=== PRODUTOS MAIS VENDIDOS (UNIDADES) ===")
print(produtos_volume)

plt.figure()
produtos_volume.plot(kind="bar")
plt.title("Produtos mais vendidos (Unidades)")
plt.xlabel("Produto")
plt.ylabel("Units Sold")
plt.xticks(rotation=45)
plt.show()


# =========================
# 6. PRODUTOS POR RECEITA
# =========================
produtos_receita = df.groupby("Product")["Total Sales"].sum().sort_values(ascending=False)

print("\n=== PRODUTOS POR RECEITA ===")
print(produtos_receita)

plt.figure()
produtos_receita.plot(kind="bar")
plt.title("Receita por Produto")
plt.xlabel("Produto")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()


# =========================
# 7. TENDÊNCIA MENSAL
# =========================
tendencia = df.groupby("Month")["Total Sales"].sum()

print("\n=== RECEITA POR MÊS ===")
print(tendencia)

plt.figure()
tendencia.plot(kind="line", marker="o")
plt.title("Tendência de Receita Mensal")
plt.xlabel("Mês")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid()
plt.show()


# =========================
# 8. TICKET MÉDIO
# =========================
ticket_medio = df["Total Sales"].mean()

print("\n=== TICKET MÉDIO ===")
print(ticket_medio)


# =========================
# 9. INSIGHTS AUTOMÁTICOS
# =========================
print("\n=== INSIGHTS ===")

top_regiao = receita_regiao.index[0]
top_produto = produtos_receita.index[0]
top_volume = produtos_volume.index[0]

print(f"- A região com maior receita é {top_regiao}.")
print(f"- O produto com maior receita é {top_produto}.")
print(f"- O produto mais vendido em volume é {top_volume}.")
print(f"- O ticket médio de venda é {ticket_medio:.2f}.")


# =========================
# 10. VALIDAÇÃO FINAL
# =========================
validacao = (df["Units Sold"] * df["Unit Price"] == df["Total Sales"]).all()

print("\n=== VALIDAÇÃO DE CONSISTÊNCIA ===")
print("Receita consistente:", validacao)