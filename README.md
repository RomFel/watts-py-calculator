# ⚡ watts-py-calculator

**Calculadora simples de consumo de aparelhos elétricos em Python.**

Este script ajuda você a calcular o consumo total (em kWh) e o custo mensal aproximado dos aparelhos elétricos da sua casa ou escritório com base nas informações fornecidas.

---

## 🛠️ Como funciona

1. Execute o arquivo `main.py`.
2. O terminal irá solicitar os seguintes dados para cada aparelho:
   - Nome do aparelho
   - Quantidade de unidades
   - Consumo em watts por hora (W/h)
   - Horas de uso por dia
   - Dias de uso no mês
3. Os dados são armazenados e exibidos para cada aparelho individualmente.
4. O programa calcula:
   - Consumo total em kWh
   - Valor estimado da conta, com base na tarifa informada (TE + TUSD).
5. Ao final, o valor total da energia consumida e o custo são exibidos no console.

---

## 💻 Exemplo de uso

```bash
$ python main.py
Aparelho: Geladeira
Unidades: 1
Watts/h: 150
Horas: 24
Dias: 30
Adicionar outro aparelho? [s/n]: s
Aparelho: TV
Unidades: 2
Watts/h: 100
Horas: 5
Dias: 25
Adicionar outro aparelho? [s/n]: n

Aparelho: Geladeira
Consumo: 150 watts/h
Horas: 24 | Dias: 30
Total: 108000 watts/h

Aparelho: TV
Consumo: 100 watts/h
Horas: 5 | Dias: 25
Total: 25000 watts/h

------------------------------
Total: 133.0 kW/h
Informe as tarifas da sua conta (TE+TUSD): 0.80
R$: 106.4
