
# 🍃 MongoDB com Python

Este projeto demonstra a construção de uma API em Python integrada a um banco de dados NoSQL, o MongoDB. A comunicação com o banco é realizada de forma simples e direta através do Pymongo, que serve como a ponte para a persistência e manipulação de documentos.

Um dos maiores desafios ao trabalhar com bancos NoSQL é manter um padrão consistente de dados, já que, por natureza, eles são flexíveis. Para resolver isso, trouxemos um guardião mitológico para o nosso projeto: o Cerberus. Assim como o cão de três cabeças que guardava os portões do submundo, esta biblioteca funciona como uma camada de validação robusta, garantindo que apenas as requisições que seguem um schema pré-definido possam ser salvas. Ele é o nosso "Guardião do Banco de Dados", assegurando a integridade e o padrão das informações.

### Cenário do Projeto:
Para exemplificar a integração do MongoDB com Python, foi desenvolvido um projeto voltado ao registro de pedidos, no qual as informações provenientes das requisições HTTP são armazenadas como documentos no banco de dados NoSQL.



🍃 **Comunicação Eficiente com o Banco:** Utilizado como o driver oficial para estabelecer a comunicação entre a aplicação Python e o banco de dados MongoDB, o Pymongo, gerencia as conexões e abstrai as operações de CRUD (Create, Read, Update, Delete) de forma simples e eficiente.

🛡️ **Validação e Integridade dos Dados:** A biblioteca Cerberus atua como uma camada de validação para os dados da API. Em um banco schemaless como o MongoDB, ela garante a consistência ao persistir apenas documentos que sigam um padrão. Além disso, a biblioteca retorna respostas de erro detalhadas, indicando exatamente quais campos da requisição são inválidos, com base nas regras definidas na pasta validators.

✅ **Qualidade de Código Assegurada:** O código é constantemente analisado pela ferramenta de linting Pylint, que garante a conformidade com as melhores práticas do Python (PEP 8) e ajuda a prevenir bugs.

🧪 **Confiabilidade e Testes Automatizados:** A robustez da aplicação é garantida por uma suíte de testes implementada com Pytest, validando cada endpoint e regra de negócio para assegurar o seu correto funcionamento.


## ⚙️ Rodando localmente

#### 1. Clone o projeto


```bash
git clone https://github.com/LucasVizoto/mongoDB_python.git
```
#### 2. Crie e ative um ambiente virtual


```bash
python -m venv venv

source venv/bin/activate   # Linux/MacOS
venv\Scripts\activate      # Windows

```

#### 3. Instale as dependências

```bash
pip install -r requirements.txt
```


#### 4. Inicie o Servidor

```
python app.py
```

## 📖 Documentação da API

- Criar um novo pedido

```
  POST /delivery/order
```

#### Body da Requisição:
```
{
    "data": {
        "name": str,
        "address": str,
        "cupom": bool,
        "items": [
            {"item": str, "quantity": int}
        ]
    }
}
```


#### Resposta esperada: 
```
HTTP/1.1 201 Created
Content-Type: application/json

{
    "data": {
        "count": 1,
        "registry": true,
        "type": "Order"
    }
}

```
---
####

- Busca de Pedido por ID

```
  GET /delivery/order/:order_id
```
#### Params:
| Campo   | Tipo | Descrição|Exemplo|
| :---------- | :--------- | :---------- |:---------------------------------- |
| `order_id` | `string` | **Obrigatório**. "__id" do documento gerado no MongoDB.| 688e72a6d8002015f90814fe |

#### Exemplo de Resposta esperada: 
```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "data": {
        "attributes": {
            "_id": "688e72a6d8002015f90814fe",
            "address": "Endereço, 1805,
            "created_at": "Sat, 02 Aug 2025 17:18:46 GMT",
            "cupom": false,
            "items": [
                {
                    "item": "Pizza",
                    "quantity": 2
                }
            ],
            "name": "Order Name"
        },
        "count": 1,
        "type": "Order"
    }
}
```
O campo `created_at` é gerado automaticamente pela aplicação no momento da requisição de criação de um Pedido. A biblioteca datetime é utilizada para capturar o timestamp exato, que é então inserido no banco de dados.



---
#### 
- Atualização de Pedido

```
  PATCH /delivery/order/:order_id
```
#### Params:
| Campo   | Tipo | Descrição|Exemplo|
| :---------- | :--------- | :---------- |:---------------------------------- |
| `order_id` | `string` | **Obrigatório**. "__id" do documento gerado no MongoDB.| 688e72a6d8002015f90814fe |


#### Body da Requisição:
Para atualizar um pedido, envie no corpo da requisição apenas os campos que deseja alterar com seus respectivos novos valores. A estrutura dos campos é a mesma retornada pela consulta de um pedido via GET.

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "data":{
        "address": "Rua Atualizada"
    }
}
```

#### Resposta esperada: 
```
{
    "data": {
        "count": 1,
        "order_id": "688e72a6d8002015f90814fe",
        "type": "Order"
    }
}
```

## Rodando os testes

Caso deseja rodar um arquivo específico de teste, basta digitar o seguinte comando apontando o caminho do arquivo
```bash
  pytest -s -v src/*
```

Caso apenas deseja rodar todos os teste:
```
  pytest
```
## 🔗Links

 - [Link para o curso](https://app.rocketseat.com.br/classroom/mongo-db-em-python)
 - [Certificado](https://app.rocketseat.com.br/certificates/fba5e1c0-0725-4d2b-b966-199678d0e0a1)


## 🔎 Onde me encontrar

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/lucasvizoto/)

[![e-mail](https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white)](mailto:lucavizoto364@gmail.com)
