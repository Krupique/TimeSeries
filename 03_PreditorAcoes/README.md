# Preditor de Ações

Repositório contendo o projeto Preditor de Ações utilizando o Streamlit

> A aplicação pode ser executada direto no servidor do heroku: <a target="_blank" href="https://app-stock-exchange.herokuapp.com">app-stock-exchange</a>

## INTRODUÇÃO

Este projeto teve por objetivo, o desenvolvimento de um modelo capaz de prever o preço das ações em um futuro próximo e determinar se o ativo vai se valorizar ou desvalorizar.

Os dados são coletados via API fornecida pelo Yahoo. O usuário pode definir a data incial e a data final da coleta. É possível selecionar uma ou mais empresas por vez, dentre as centenas de opções fornececidas pelo desenvolvedor.

O usuário pode cadastrar seu próprio Ticker localmente, caso o mesmo não esteja disponível nas opções pré-definidas.

O projeto traz uma análise exploratória, descritiva, estatística e preditiva utilizando diversas ferramentas e técnicas empregadas no uso de análise de séries temporais. Eu procurei detalhar o máximo possível dos conceitos e técnicas utilizadas para que este projeto possa servir de fonte de estudos a quem interessar.

## ORGANIZAÇÃO DOS DIRETÓRIOS
Arquivos na raiz do diretório:
> **main.py**: Arquivo principal do programa Streamlit, esse á o arquivo que deve ser executado para rodar a aplicação<br/>
> **Procfile**: Arquivo de configuração do Heroku, contém o comando que o Heroku deve executar para rodar a aplicação no servidor.<br/>
> **requirements.txt**: Bibliotecas necessárias para executar o projeto e suas versões específicas.<br/>
> **runtime.txt**: Versão Python utilizada no projeto<br/>
> **setup.sh**: Arquivo de configuração para executar o framework Streamlit no servidor do Heroku<br/>

Diretórios na raiz:
> **assets/**: Imagens utilizadas<br/>
> **include/**: Contém as bibliotecas desenvolvidas para modularizar o projeto.<br/>
> **notebook/**: O projeto de análise detalhado, realizado utilizando o formato ipynb.<br/>
> **utils/**: Arquivo txt que contém os tickers disponíveis no projeto.<br/>

Arquivos dentro dos diretórios:
> **include/calculos.py**: Biblioteca com as funções que fazem os cálculos as análises estatísticas.<br/>
> **include/coleta.py**: Biblioteca com as funções próprias para realizar a coleta dos dados e realizar o tratamento das informações.<br/>
> **include/graphs.py**: Biblioteca para criação dos gráficos utilizados. (Barplot, Boxplot, Lineplot, Canddlestick e Histogram)<br/>
> **include/modelo.py**: Biblioteca com a classe do Modelo Estatístico/Machine Learning desenvolvido.<br/>
> **notebook/notebook.ipynb**: Notebook desenvolvido com todas as análises, conceitos e técnicas utilizadas.<br/>
> **utils/lista_siglas.txt**: Arquivo txt com a lista de tickers disponíveis. Insira seu próprio ticker nessa lista para ser carregado e disponibilizado no projeto<br/>


## COMO EXECUTAR O PROJETO
Para executar o projeto em sua máquina local, certifique-se de ter instalado todas as dependências descritas nos arquivos `requirements.txt` e `runtime.txt`, navegue via terminal até o diretório do arquivo `main.py`, então execute o comando:
> `>streamlit run main.py`

Para executar o projeto de análises, tenha alguma `IDE` ou `Editor de Texto` que seja capaz de ler e executar arquivos `ipynb`, então abra o arquivo `notebook/notebook.ipynb` e execute célula por célula.

Para utilizar a aplicação web, acesse o seguinte link: <a target="_blank" href="https://app-stock-exchange.herokuapp.com">`app-stock-exchange`</a>

## COMO VISUALIZAR AS ANÁLISES
O arquivo notebook deste projeto já está compilado e executado, portanto, não é necessário re-executar para visualizar os resultados obtidos. Dentro do diretório notebook/ o arquivo README contém toda a descrição da análise.

É possível navegar pelo sumário do projeto até a análise desejada.


### Sumário das análises no arquivo .ipynb

- 1.) INTRODUÇÃO
	* 1.1) Definição do problema
	* 1.2) Objetivos do projeto
	* 1.3) Conceitos
* 2.) COLETA DE DADOS
* 3.) ANÁLISE DOS DADOS
	* 3.1) Análise Exploratória
	* 3.2) Análise Descritiva
		* 3.2.1) Volume
		* 3.2.2) Rentabilidade
* 4.) ANÁLISE DE SÉRIES TEMPORAIS
	* 4.1) Séries Temporais Aditivas e Multiplicativas
	* 4.2) Descomposição da Série Temporal
	* 4.3) Estacionaridade
		* 4.3.1) Recapitulando
		* 4.3.2) Verificando a Estacionariedade
		* 4.3.3) O Que São Lags (Defasagens ou Atrasos)?
		* 4.3.4) Autocorrelação
		* 4.3.5) Exibição das Rolling Statistics (Estatísticas Móveis)
		* 4.3.6) Gráficos ACF e PACF
		* 4.3.7) Teste Dickey-Fuller Aumentado
		* 4.3.8) Tipos de Estacionariedade
		* 4.3.9) Transformando uma Série Não Estacionária em Série Estacionária
* 5.) PRÉ-PROCESSAMENTO DOS DADOS
	* 5.1) Transformação dos Dados
		* 5.1.1) Transformação de Log
		* 5.1.2) Diferenciação
		* 5.1.3) Transformação de Raiz Quadrada
		* 5.1.4) Transformação Box-Cox
	* 5.2) Suavização(Smoothing)
		* 5.2.1) Smoothing
		* 5.2.2) Média Móvel Simples
		* 5.2.3) Média Móvel Ponderada Exponencial
* 6.) MODELAGEM
	* 6.1) Conceitos
	* 6.2) Divisão em Treino e Teste
	* 6.3) Método Naive
	* 6.4) Trabalhando com Forecasting mais avançado	
	* 6.5) Exponential Smoothing
	* 6.6) Modelos ARIMA
		* 6.6.1) Primeiro Modelo ARIMA
		* 6.6.2) Melhorando os parâmetros P, Q e D
		* 6.6.3) Determinando o valor do Parâmetro d para o modelo ARIMA
		* 6.6.4) Determinando o Valor do Parâmetro p para o Modelo ARIMA
		* 6.6.5) Determinando o Valor do Parâmetro q para o Modelo ARIMA
	* 6.7) Modelo SARIMA
		* 6.7.1) Seasonal Autoregressive Integrated Moving-Average (SARIMA)
		* 6.7.2) Elementos de Tendência
		* 6.7.3) Elementos de Sazonalidade
		* 6.7.4) Notação SARIMA
		* 6.7.5) Parâmetros SARIMA(3,1,0)(1,1,0)15
		* 6.7.6) Grid Search Método 1 - Stepwise Search
* 7.) FORECASTING
	* 7.1) Utilizando o modelo SARIMA para prever os próximos 6 meses
* 8.) CONSIDERAÇÕES SOBRE O PROJETO
	* 8.1) Considerações
	* 8.2) Streamlit
	* 8.3) Referências
	* 8.4) Agradecimentos


## CONTATO
Você pode me encontrar nas redes sociais:

* <a target="_blank" href="https://www.linkedin.com/in/henrique-krupck/">Linkedin: Henrique-Krupck</a> <br/>
* <a target="_blank" href="mailto:krupck@outlook.com">Email: krupck@outlook.com</a> <br/>
* <a target="_blank" href="https://wa.me/5518996755455">WhatsApp: (18) 99675-5455</a> <br/>
* <a target="_blank" href="https://www.instagram.com/h_krupck/">Instagram: @h_krupck</a> <br/>

Qualquer dúvida, sugestão, apotamento ou crítica é bem vinda

Atenciosamente,

**Henrique Krupck**
