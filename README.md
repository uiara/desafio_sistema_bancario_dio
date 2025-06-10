# desafio_sistema_bancario_dio

---

# 💰 Sistema Bancário em Python

Este projeto foi desenvolvido como parte de um **desafio da DIO Innovation** e simula um sistema bancário simples utilizando a linguagem Python. A aplicação é executada no terminal e permite realizar depósitos, saques e consultar um extrato detalhado.

## 🧠 Funcionalidades

* **Depósito**

  * Permite adicionar valores positivos ao saldo.
* **Saque**

  * Limite de 3 saques por dia.
  * Valor máximo por saque: R\$500,00.
  * Verificação de saldo suficiente.
* **Extrato**

  * Lista todas as transações realizadas com data e tipo.
  * Mostra o saldo final de forma formatada.

## 💻 Tecnologias utilizadas

* Python 3.12
* Módulo `datetime` (para registrar a data das transações)

## 📁 Estrutura do projeto

```
banco.py  # Script principal contendo as funções de depósito, saque e extrato
```

## ▶️ Como executar

1. Clone o repositório:

   ```bash
   git clone [https://github.com/uiara/desafio_sistema_bancario_dio.git](https://github.com/uiara/desafio_sistema_bancario_dio.git)
   cd desafio_sistema_bancario_dio
   ```

2. Execute o arquivo no terminal:

   ```bash
   python banco.py
   ```

3. Siga as instruções exibidas para realizar transações.

## 📋 Regras de Negócio

* O usuário pode sacar até **3 vezes por sessão**.
* Cada saque pode ter um valor **máximo de R\$500,00**.
* Apenas valores **positivos** podem ser depositados ou sacados.
* O extrato mostra transações formatadas com **data e valor**, incluindo o **saldo final**.

## ✨ Exemplo de saída formatada

```
===================================
|        EXTRATO BANCÁRIO        |
===================================
|   Data     |     Transação     |
-----------------------------------
| 10/06/2025 |   +       R$100.00 |
| 10/06/2025 |   -       R$50.00  |
-----------------------------------
| Saldo Atual:           R$50.00 |
===================================
```

## 👤 Autor

* [uiara](https://github.com/uiara)

---
