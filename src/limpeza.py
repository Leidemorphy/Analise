import pandas as pd

# =========================
# 1. CARREGAMENTO DOS DADOS
# =========================
df = pd.read_excel("messy_files.xlsx")


# =========================
# 2. REMOÇÃO DE COLUNAS DESNECESSÁRIAS
# =========================
df = df.drop(columns=["Profit Margin (%)"])


# =========================
# 3. CONVERSÃO DE DATA
# =========================
df["Date"] = pd.to_datetime(
    df["Date"],
    format="mixed",
    errors="coerce",
    dayfirst=True
)


# =========================
# 4. LIMPEZA DAS COLUNAS NUMÉRICAS
# =========================

# Conversão de valores escritos por extenso
mapa_unit_sold = {"thirty": 30, "twenty": 20}

df["Units Sold"] = (
    df["Units Sold"]
    .replace(mapa_unit_sold)
    .astype("Int64")
)

# Limpeza do preço unitário (remoção de texto)
df["Unit Price"] = (
    df["Unit Price"]
    .astype(str)
    .str.extract(r"(\d+\.?\d*)")
)

df["Unit Price"] = pd.to_numeric(df["Unit Price"])


# =========================
# 5. REMOÇÃO DE VALORES NULOS CRÍTICOS
# =========================
df = df.dropna(subset=["Date", "Unit Price", "Units Sold", "Product"])


# =========================
# 6. CRIAÇÃO DE MÉTRICAS DERIVADAS
# =========================
df["Total Sales"] = df["Units Sold"] * df["Unit Price"]


# =========================
# 7. PADRONIZAÇÃO DE TEXTO
# =========================
df["Product"] = df["Product"].str.strip().str.capitalize()
df["Region"] = df["Region"].str.strip().str.capitalize()
df["Category"] = df["Category"].str.strip().str.capitalize()


# =========================
# 8. RECLASSIFICAÇÃO DE CATEGORIA (REGRA DE NEGÓCIO)
# =========================
mapa = {
    "Laptop": "Electronics",
    "Phone": "Electronics",
    "Tablet": "Electronics",
    "Monitor": "Electronics",
    "Desktop": "Electronics"
}

df["Category"] = df["Product"].map(mapa)


# =========================
# 9. VALIDAÇÃO RÁPIDA
# =========================

# Verificar consistência da receita
# print((df["Units Sold"] * df["Unit Price"] == df["Total Sales"]).all())


# =========================
# 10. EXPORTAÇÃO DOS DADOS LIMPOS
# =========================
df.to_excel("messy_files_clean.xlsx", index=False)