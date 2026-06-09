# 📊 Data Cleaning & Transformation Project (Python + Pandas)

## 📌 Descrição

Este projeto tem como objetivo realizar a limpeza, transformação e padronização de um dataset de vendas "sujo", contendo inconsistências em datas, valores numéricos, categorias e formatos de texto.

O foco principal foi transformar os dados brutos em um dataset confiável para análise.

---

## 🧹 Etapas do processo

### 1. Carregamento dos dados
Importação do ficheiro Excel original com dados inconsistentes.

### 2. Limpeza de colunas
Remoção de colunas desnecessárias para análise.

### 3. Tratamento de datas
Conversão de strings para formato datetime.

### 4. Limpeza de valores numéricos
- Correção de valores escritos por extenso (ex: "thirty")
- Remoção de texto em preços ("USD 500")
- Conversão para tipos numéricos corretos

### 5. Tratamento de valores nulos
Remoção de linhas sem dados críticos como:
- Data
- Produto
- Preço
- Unidades vendidas

### 6. Engenharia de dados
Criação da métrica:
- Total Sales = Units Sold × Unit Price

### 7. Padronização de texto
Normalização de:
- Produtos
- Regiões
- Categorias

### 8. Reclassificação de categorias
Criação de uma regra de negócio para padronizar categorias com base no produto.

---

## 📊 Tecnologias utilizadas

- Python
- Pandas
- Excel (input/output)

---

## 📁 Output

Dataset final limpo e pronto para análise:
