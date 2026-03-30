# Trello-powerup-Project-Management

## Status

Projeto em fase experimental, em testes para possível integração gradual ao fluxo operacional interno.

# PDI Project Power-Up for Trello

Power-Up para Trello desenvolvido para centralizar e automatizar o acompanhamento de projetos do setor PDI, integrando leitura de dados locais com atualização estruturada de informações operacionais.

## Objetivo

Criar uma solução que permita reunir informações básicas e técnicas dos projetos em uma única interface de acompanhamento, reduzindo dependência de atualização manual e facilitando a visualização em tempo real.

## Problema identificado

Atualmente os projetos possuem informações distribuídas em diferentes pastas e controles manuais, dificultando:

* rastreamento de andamento
* atualização contínua
* visualização rápida de status
* organização centralizada de atividades

## Solução proposta

O sistema utiliza Python para analisar automaticamente a estrutura das pastas dos projetos e enviar informações para o Trello por meio de API.

## Funcionalidades atuais

* leitura automática do nome do projeto
* captura do caminho da pasta
* leitura da data de criação
* estrutura pronta para geração automática de cartões

## Tecnologias utilizadas

* Python
* Flask
* API do Trello
* requests

## Estrutura do projeto

```text
api/
│── app.py
│── leitura_pasta.py
│── trello_envio.py
```

## Próximas implementações

* leitura de quantidade de blocos
* identificação de arquivos TIFF
* análise de erros de tratamento
* análise de erros DTM
* previsão de entrega
* controle de colaboradores

## Status

Projeto em desenvolvimento modular, iniciando pela camada base de leitura e integração.

## Visão futura

Transformar o Power-Up em uma ferramenta de apoio operacional para centralização de projetos e atualização contínua do setor.
