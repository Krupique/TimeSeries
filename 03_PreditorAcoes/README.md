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


### Sumário do projeto
