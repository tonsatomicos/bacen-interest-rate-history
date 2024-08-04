# <p align="center">Projeto de Web Mining & Crawler Scraping<br>Bacen - Histórico das Taxas de Juros</p>

<p align="center">
<img src="http://img.shields.io/static/v1?label=LICENCA&message=...&color=GREEN&style=for-the-badge"/>
<img src="http://img.shields.io/static/v1?label=STATUS&message=N/A&color=GREEN&style=for-the-badge"/>
</p>

Este projeto foi concebido como parte de um desafio durante a disciplina de Web Mining & Crawler Scraping, no curso de pós-graduação em Engenharia de Dados, na Universidade de Fortaleza (Unifor).

O desafio consistia em desenvolver um scraper no site de nossa escolha, extrair e retornar os dados. Optei por raspar o histórico de taxas de juros básicas do BACEN.

Para realizar esse processo, utilizei <code>Selenium</code> para a raspagem de dados, <code>Pandas</code> para transformação, <code>Pandera</code> para qualidade de dados e <code>SQLAlchemy ORM</code> para persistência, realizando insert e update conforme necessário.

## Etapas

![Descrição da Imagem](https://github.com/tonsatomicos/bacen-interest-rate-history/blob/main/assets/estrutura.png?raw=true)

## Estrutura

Utilizando <code>Poetry</code> para gerenciamento de ambientes virtuais e dependências, e <code>Pyenv</code> para o controle de versão.

### Versão do Python
```bash
3.11.9
```

### Dependências | Produção

- selenium
- pandas
- lxml
- html5lib
- pandera
- sqlalchemy
- psycopg2-binary
- pyodbc
- loguru

### Dependências | Desenvolvimento

- flake8
- black
- isort
- ipykernel
- matplotlib
- pre-commit

### Instalação das Dependências

Você pode instalar as dependências manualmente, ou, utilizando o Poetry ou o Pip com os seguintes comandos:

#### Utilizando Poetry

```bash
poetry install
```

#### Utilizando Pip

```bash
pip install -r requirements.txt

```

## Configurações do Projeto - Parte 1 - Banco de Dados

O arquivo <code>./bacen-interest-rate-history/core/domain/models/rate_history.py</code> contém a definição da classe que representa a tabela do banco de dados, ou seja, a classe que mapeia a tabela onde os dados serão persistidos, com os campos necessários para cada registro.

Neste caso, a classe está mapeada para a tabela <code>historico_juros_taxas</code>. Caso seja necessário, você pode alterar para outra tabela conforme a necessidade do projeto.

Os scripts SQL disponibilizados em <code>./sql/</code> inclui o esquema da tabela, com detalhes sobre os tipos de dados, chaves primárias e quaisquer restrições adicionais necessárias.

### Como usar?

Nas linhas 10 e 11 do script <code>./bacen-interest-rate-history/bacen-interest-rate-history/core/main.py</code> existe a criação do objeto engine para os bancos <code>PostgreSQL</code> e <code>SQL Server</code>, basta configurar na ordem:

- Banco para persistência
    - Consulte o arquivo <code>./bacen-interest-rate-history/bacen-interest-rate-history/core/utils/db_engine.py</code> para verificar os bancos suportados.
- IP do banco
- Usuário
- Senha
- Database

### Qual banco usar?

Como visto anteriormente, a engine está adaptada para persistir os dados ou no Postgres ou no SQL Server, caso precise persistir em outros bancos, como MySQL, basta consultar a documentação do SQL Alchemy e adicionar uma nova opção na função <code>create_engine</code> existente no arquivo <code>./bacen-interest-rate-history/bacen-interest-rate-history/core/utils/db_engine.py</code>.

### Utilizando Docker

Tenho preparado na pasta <code>./bacen-interest-rate-history/infra/docker/</code> um docker-compose, com um container Postgres e um container SQL Server, que cria automaticamente o banco e as tabelas, caso queira utilizar um deles, prossiga com o comando:
<pre><code>docker-compose up -d</code></pre>

Lembre-se de verificar o usuário e a senha dos bancos de dados no arquivo <code>docker-compose.yml</code>.

## Configurações do Projeto - Parte 2 - Qualidade dos Dados

Usando <code>Pandera</code> para garantir a qualidade dos dados após a transformação. O arquivo <code>./bacen-interest-rate-history/core/domain/models/rate_history.py</code> contém a definição da classe que representa o schema de saída da transformação dos dados usando <code>Pandas</code>, verificando a tipagem dos dados e garantido que estejam de acordo com o schema do banco de dados.

## Conclusão

Após realizar essa primeira configuração, o projeto está pronto para ser executado. Ele pode facilmente persistir em qualquer banco de dados relacional, desde que a <code>engine</code> esteja configurada corretamente. Isso oferece uma ampla flexibilidade para adaptar o projeto a diferentes ambientes e requisitos de armazenamento de dados.

Para executar o projeto, utilize o seguinte comando:

```bash
python ./bacen-interest-rate-history/bacen-interest-rate-history/core/main.py
```
</p>

## Considerações Finais

- A documentação pode não estar tão detalhada, talvez seja necessário um certo nível de conhecimento para adaptar o código.
- Se tudo estiver configurado corretamente, basta executar o script e verificar a tabela no banco de dados usando o DBeaver ou outra ferramenta de sua preferencia.
- Tentei aplicar os conceitos de SOLID nesse projeto, por isso a estrutura pode parecer uma pouco confusa.
- Disponibilizei na pasta <code>./notebooks/</code> um jupyter notebook chamado <code>data_analysis.ipynb</code>, onde recupero os dados inseridos no banco de dados e faço uma análise da evolução da meta Selic ao longo do tempo.
<hr>

![Image](https://i.imgur.com/p4vnGAN.gif)
