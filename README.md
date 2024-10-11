# Análise de Dados de Gorjetas: Identificando Fatores e Construindo Modelos Preditivos

<p align="center">
  <img src="https://www12.senado.leg.br/radio/1/conexao-senado/2024/02/08/tribuna-do-consumidor-gorjetas/@@images/41e8f83f-99b2-43eb-a840-065299318f1b.jpeg" />
</p>

## Desenvolvedor

 - Paulo Carlos Filho (https://github.com/paulocarlosfilho/)
   
---

Este estudo tem como objetivo principal identificar os fatores que influenciam o valor das gorjetas em restaurantes e, com base nessa compreensão, desenvolver modelos preditivos capazes de estimar o valor da gorjeta em novas situações.

## Justificativa:

O setor de restaurantes busca constantemente maneiras de melhorar a experiência do cliente e aumentar a receita. As gorjetas representam uma parte significativa da renda dos garçons e podem ser influenciadas por diversos fatores. Compreender os elementos que levam a um valor de gorjeta maior permite que os estabelecimentos otimizem suas operações, melhorem o atendimento e, consequentemente, aumentem a satisfação dos clientes e a receita.

Nesse projeto abordaremos questões como:

1. Quais características de uma transação (valor da conta, tamanho do grupo, dia da semana, etc.) têm maior impacto no valor da gorjeta?
2. É possível construir um modelo preciso para prever o valor da gorjeta em novas situações?
3. Existem tendências ao longo do tempo no valor das gorjetas, como variações sazonais ou relacionadas a eventos específicos?

Ao responder a essas perguntas, este estudo contribui para o setor de restaurantes ao:

1. **Otimizar o atendimento:** Permitir que os restaurantes adaptem o atendimento de acordo com o perfil do cliente para incentivar maiores gorjetas.
2. **Desenvolvendo programas de fidelidade:** Criar programas que recompensem clientes que deixam gorjetas maiores.
3. **Analisando o impacto de promoções:** Avaliar como diferentes promoções influenciam o valor da gorjeta.
4. **Tomando decisões estratégicas:** Utilizar os insights obtidos para tomar decisões mais estratégicas sobre preços, menu e atendimento.

Em resumo, este estudo visa oferecer insights valiosos para a indústria de restaurantes, permitindo que os estabelecimentos otimizem suas operações, melhorem a satisfação dos clientes e aumentem a receita.


<!-- T
> **Nota**: todo o texto abaixo é somente para entendimento do usuário do template. Por favor remova-o quando for atualizar este `README.md`.

## Funcionalidades

Esse template foi inicialmente baseado no [template de ciência de dados do cookiecutter](https://drivendata.github.io/cookiecutter-data-science/), mas ao longo do tempo várias modificações foram sendo realizadas. Atualmente o template tem as seguintes características:
 - Utilização do arquivo `pyproject.toml` como centralizador de dependências;
 - Configuração para criação de aplicação `streamlit`;
 - Utilização de [jupyter notebooks](https://jupyter.org/) para arquivos de análise;
 - Documentação com o [mkdocs](https://www.mkdocs.org/) ([material design](https://squidfunk.github.io/mkdocs-material/) theme)

## Instruções

### Requisitos

Para utilizar este template, você precisará de um ambiente com os seguintes softwares:
 - git
 - Python 3.8
 - Poetry `1.1.13` ou superior

É aconselhável o uso do `pyenv` para o gerenciamento de versões do Python.

### Iniciando um novo projeto

Para iniciar um novo projeto você precisa ter instalado na sua máquina as aplicações citadas na seção anterior, depois disso basta:

1. clicar no botão **Use this template** (ou "Usar este modelo").
2. Digitar um nome para seu repositório e uma descrição opcional.
3. Escolher a visibilidade do projeto (Publica ou privada).
4. Clicar em **Create repository from template** (Criar repositório a partir do modelo).

Pronto, acaba de criar um repositório a partir deste modelo. Para mais informações sobre o uso de templates, acesse a [documentação oficial](https://docs.github.com/pt/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).


### Contribuindo com um repositório já criado

Depois de criar o repositório, para começar a modificá-lo e/ou contribuir com repositórios já criados,  você precisa cloná-lo. Para isso, siga os seguintes passos:

1. Acima da lista de arquivos, clique no botão **Code** (em verde).
2. Copie a URL para o repositório.
    - Tente clonar utilizando uma chave **SSH**. Para isso, clique na aba **SSH** e em seguida clique no ícone de cópia.
3. Abra o terminal.
4. Altere o diretório de trabalho atual para o local que deseja ter o diretório clonado.
5. Digite `git clone` e cole a URL que você copiou anteriormente:

```
git clone git@github.com:NOME-DE-USUARIO/REPOSITORIO.git
```
6. Pressione **Enter** para criar seu clone local.

Proto, com isso você acaba de clonar um repositório. Para mais informações sobre a clonagem de arquivos, acesse a [documentação oficial](https://docs.github.com/pt/repositories/creating-and-managing-repositories/cloning-a-repository).

Com o repositório clonado, você precisa navegar até a pasta local, usando o comando :

```
cd REPOSITORIO
```

Estando na pasta do repositório, basta instalar as dependências do projeto utilizando o comando:

```
poetry install
```

Ele irá instalar todas as dependências contidas no arquivo `pyproject.toml`. Depois disso basta ativar o ambiente virtual criado pelo Poetry utilizando o comando:

```
poetry shell
```

Para mais informações sobre os comandos do Poetry, visite a [documentação oficial](https://python-poetry.org/docs/).

Para contribuir com um projeto, tente utilizar uma metodologia adequada. Utilize [este artigo](https://omadson.github.io/site/blog/2022/software-development-workflow/) para obter mais informações.


### Organização de diretórios


```
.
├── data/              # Diretório contendo todos os arquivos de dados
│   ├── external/      # Arquivos de dados de fontes externas
│   ├── interim/       # Arquivos de dados intermediários
│   ├── processed/     # Arquivos de dados processados
│   └── raw/           # Arquivos de dados originais, imutáveis
├── docs/              # Documentação gerada através da biblioteca mkdocs
├── models/            # Modelos treinados e serializados, predições ou resumos de modelos
├── notebooks/         # Diretório contendo todos os notebooks utilizados nos passos
├── references/        # Dicionários de dados, manuais e todo o material exploratório
├── src/               # Código fonte utilizado nesse projeto
│   ├── data/          # Classes e funções utilizadas para download e processamento de dados
│   ├── deployment/    # Classes e funções utilizadas para implantação do modelo
│   └── model/         # Classes e funções utilizadas para modelagem
├── app.py             # Arquivo com o código da aplicação do streamlit
├── Procfile           # Arquivo de configuração do heroku
├── pyproject.toml     # Arquivo de dependências para reprodução do projeto
├── poetry.lock        # Arquivo com sub-dependências do projeto principal
├── README.md          # Informações gerais do projeto
└── tasks.py           # Arquivo com funções para criação de tarefas utilizadas pelo invoke

```
-->
