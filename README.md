# 🌊 Sistema de Monitoramento e Alerta de Nível do Rio (Recife)

Este projeto é um protótipo digital desenvolvido para **monitorar o nível de um rio**, com foco na **previsão e alerta de possíveis enchentes**. Ele integra dados meteorológicos, simulações do nível do rio, um modelo matemático preditivo e visualizações gráficas e tabulares para facilitar a interpretação.

---

## ✨ Funcionalidades Principais

* **Previsão do Tempo Atual:** Exibe a descrição do tempo e a temperatura em Celsius para a cidade de **Recife**, utilizando dados da API do OpenWeatherMap.
* **Simulação do Nível do Rio:** Simula a variação do nível do rio ao longo de **10 dias**, considerando aumentos aleatórios devido à "chuva" e respeitando limites de nível (mínimo de **0.5m** e máximo de **3.0m**).
* **Modelagem Polinomial:** Ajusta uma **função polinomial de grau 2** aos dados simulados. Essa função permite identificar a tendência do nível do rio e ajuda a prever seu comportamento futuro.
* **Alerta de Enchente:** O sistema visualiza um **limite de alerta de enchente (2.5m)** diretamente no gráfico, indicando quando o nível do rio atinge um ponto crítico.
* **Visualização Gráfica:** Apresenta um **gráfico claro** da variação do nível do rio, mostrando os dados simulados, a tendência polinomial e o limite de alerta para uma compreensão visual imediata.
* **Tabela Detalhada:** Exibe os **dados numéricos diários** em formato tabular, incluindo o dia, o nível simulado e o nível previsto pelo polinômio. A tabela é **scrollável** para fácil navegação.

---

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **`requests`:** Biblioteca para realizar requisições a APIs externas (como a do OpenWeatherMap).
* **`customtkinter`:** Framework para construção de interfaces gráficas (GUI) modernas e personalizáveis.
* **`matplotlib`:** Biblioteca fundamental para a criação e renderização de gráficos de alta qualidade.
* **`numpy`:** Biblioteca essencial para cálculos numéricos, especialmente na implementação da regressão polinomial.

---

## 🚀 Como Executar o Projeto

Siga estes passos simples para rodar a aplicação em seu ambiente local:

1.  **Salve o Código:** Copie e cole o código Python fornecido em um arquivo com a extensão `.py` (ex: `monitoramento_rio.py`).
2.  **Instale as Dependências:** Abra seu terminal ou prompt de comando e execute o comando abaixo para instalar as bibliotecas necessárias:

    ```bash
    pip install requests customtkinter matplotlib numpy
    ```
3.  **Obtenha sua API Key do OpenWeatherMap:**
    * Acesse [https://openweathermap.org/api](https://openweathermap.org/api) e crie uma conta gratuita.
    * Após o registro, você encontrará sua **API Key** na seção "API keys" do seu perfil.
    * No seu arquivo Python, localize a linha que define a `apiKey` e substitua `"SUA_API_KEY_AQUI"` pela sua chave real.

4.  **Execute a Aplicação:** No terminal, navegue até o diretório onde você salvou o arquivo `.py` e execute:

    ```bash
    python monitoramento_rio.py
    ```

---

## 📊 Análise e Interpretação dos Dados

### 1. Domínio e Imagem da Função

* **Domínio:** Para a função do nível do rio ($f(\text{dia})$), o domínio representa os **dias da simulação**. Neste protótipo, o domínio é um conjunto discreto de dias: $\{1, 2, 3, \dots, 10\}$. Isso significa que estamos observando e modelando o nível do rio dia a dia ao longo de um período de 10 dias.
* **Imagem:** A imagem da função corresponde aos **níveis do rio (em metros)** que são gerados na simulação ou previstos pelo modelo. Na nossa simulação, o nível do rio é restrito a um intervalo de **0.5m (mínimo) a 3.0m (máximo)**. Portanto, todos os valores de nível observados e previstos pela função estarão dentro desse intervalo de segurança.

### 2. Ponto de Nível Máximo Alcançado

Este ponto crucial indica o **maior nível que o rio atingiu** durante todo o período simulado. Para identificá-lo, basta verificar o **valor mais alto** registrado na coluna "**Nível Simulado (m)**" da tabela e o "Dia" correspondente.

* **Exemplo:** Se o maior valor na coluna "Nível Simulado" for **3.00m** e isso ocorrer no **Dia 7**, então 3.00m é o ponto de nível máximo.

### 3. Dias de Risco de Transbordamento

Definimos como **dias de risco de transbordamento** aqueles em que o nível do rio é **maior que 2 metros**. Esta é uma métrica vital para o sistema de alerta precoce. Você pode identificar esses dias simplesmente observando os valores na coluna "**Nível Simulado (m)**" na tabela.

* **Exemplo:** Se no **Dia 3** o "Nível Simulado" for **2.02m**, esse dia já indica um risco de transbordamento.

### 4. Modelo Matemático e Alerta de Enchentes

O cerne deste sistema reside na **função polinomial ($f(\text{dia}) = a_2 \cdot (\text{dia})^2 + a_1 \cdot (\text{dia}) + a_0$)**. Ela desempenha um papel fundamental em:

* **Captura de Tendências:** Ao se ajustar aos dados históricos, a função identifica e descreve se o nível do rio está em uma tendência de subida, descida ou atingindo um pico, fornecendo insights sobre o comportamento do rio.
* **Previsão:** Embora a simulação atual seja limitada a 10 dias, a função polinomial pode ser extrapolada (com cautela) para estimar níveis em dias futuros, caso dados adicionais fossem fornecidos.
* **Alerta Proativo:** A funcionalidade mais importante é o alerta. Se a curva da função polinomial indicar uma **tendência de subida acentuada** que se aproxima ou ultrapassa o **limite de alerta (a linha vermelha no gráfico)**, um aviso pode ser disparado proativamente. Isso oferece um tempo valioso para que as autoridades e a população se preparem antes que um transbordamento real ocorra.

---

## 📊 Visualização do Protótipo

Ao executar o programa, você verá uma interface gráfica que apresenta a previsão do tempo no topo e, abaixo dela, o gráfico da variação do nível do rio. Embora este `README.md` não mostre a interface completa em imagem, a visualização será semelhante à seguinte tabela de dados:

### Exemplo da Tabela de Variação do Rio

| Dia | Nível Simulado (m) | Nível Polinomial (m) |
| :-- | :----------------- | :------------------- |
| 1   | 1.35               | 1.30                 |
| 2   | 1.68               | 1.62                 |
| 3   | 2.02               | 1.95                 |
| 4   | 2.30               | 2.20                 |
| 5   | 2.65               | 2.45                 |
| 6   | 2.90               | 2.65                 |
| 7   | 3.00               | 2.78                 |
| 8   | 2.95               | 2.85                 |
| 9   | 2.80               | 2.80                 |
| 10  | 2.50               | 2.60                 |

*(Os valores apresentados na tabela acima são apenas **exemplos** e podem variar a cada execução do programa devido à natureza aleatória da simulação do nível do rio.)*
