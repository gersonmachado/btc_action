# Bitcoin - GitHub Actions

Este projeto rastreia o valor do Bitcoin (BTC) em reais (BRL) periodicamente e armazena os resultados em um arquivo CSV. A cada ~~5 minutos~~ sexta, uma consulta é realizada automaticamente através de **GitHub Actions**, que obtém o valor do BTC e o salva em um arquivo de dados (`data.csv`) usando **Python**, **pandas** e **yfinance**.

## Funcionalidades

- Consulta automática do valor do **Bitcoin (BTC/USD)**.
- Consulta a cotação do dólar atual para conversão do **Bitcoin em reais (BTC/BRL)**.
- Salvamento dos valores em um arquivo **CSV** com registros de data e hora.
- Utiliza **GitHub Actions** para automatizar a consulta periódica sem a necessidade de execução manual.
- Ferramentas principais: `yfinance`, `pandas`, `python`, `Power BI`.


## Preview
![Print do funcionamento](https://github.com/gersonmachado/btc_action/blob/main/pbi/pbi_view_btc.jpg)

