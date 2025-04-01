# Proj-VemVer
Optical Store Online System - Relatório de Atividades
1. Capa
    Título do Relatório: Optical Store Online System - Gestão de Estoque e Registro de Produtos

    Autores: Bruno Jorge (RA: 2302995), Gabriel de Sá (RA: 2303258), Lucas Cleiton (RA: 2302790), Matheus Marques (RA: 2302994)

    Data: 31/03
    Objetivo
    Desenvolver um sistema online para uma ótica, otimizando o registro de produtos, a gestão de estoque e o acompanhamento de vendas.

2. Introdução
    Objetivo Geral
    Criar um sistema web baseado em Flask para gerenciar eficientemente o estoque de uma ótica. O sistema possibilita o cadastro de produtos, a atualização de estoque e o registro de vendas.
    Contexto
    A gestão de estoque é um fator essencial para o sucesso de empresas de varejo, especialmente em setores que lidam com produtos de alto valor, como óculos e lentes. A digitalização desse processo permite um melhor controle do inventário, aprimorando o atendimento ao cliente e reduzindo perdas.

3. Descrição e Análise do Caso
    Descrição do Caso
    O sistema desenvolvido contempla as seguintes funcionalidades:
    Gestão de Produtos: Cadastro, exclusão e listagem de produtos.
    Gestão de Estoque: Monitoramento da disponibilidade dos itens.
    Gestão de Vendas: Registro e acompanhamento de transações comerciais.
    A implementação utiliza o framework Flask e um banco de dados relacional (SQLite) para armazenar informações sobre produtos e vendas.
    Análise do Problema
    Um controle de estoque eficiente garante a disponibilidade dos produtos e minimiza perdas. O sistema aproveita os relacionamentos do banco de dados para atualizar automaticamente o estoque conforme as vendas são registradas.

4. Implementação
    Etapas de Desenvolvimento
    Configuração do Projeto:
    Instalação do Flask e SQLAlchemy.
    Criação do esquema de banco de dados.
    Módulo de Produtos:
    Implementação de endpoints para CRUD de produtos.
    Integração de templates HTML para visualização.
    Módulo de Vendas:
    Criação do modelo de vendas.
    Desenvolvimento de visualização das transações.
    Desafios e Soluções
    Desafio: Garantir a consistência dos dados entre estoque e vendas.
    Solução: Implementação de restrições de chave estrangeira para assegurar integridade referencial.

5. Resultados
    Testes e Validação
    Testes unitários para verificação de inclusão e remoção de produtos.
    Simulação de transações para validar a atualização de estoque.
    Implementação de validação frontend para evitar cadastros inconsistentes.
    Interpretação dos Resultados
    O sistema demonstrou eficiência na gestão de estoque e vendas. Os usuários podem adicionar produtos, monitorar estoque e registrar vendas com facilidade.


6. Conclusão
    Aprendizados
    Experiência no desenvolvimento de operações CRUD com Flask e SQLAlchemy.
    Importância dos relacionamentos entre tabelas para controle de estoque.
    Aplicabilidades Futuras
    Implementação de autenticação para segurança do acesso.
    Adição de relatórios para análise de vendas.

7. Impacto no Mundo Real
    Aplicações Práticas
    Melhor acompanhamento da disponibilidade de produtos para varejistas.
    Registros de vendas otimizam a reposição de estoque.
    Oportunidades de Expansão
    Integração com plataformas de e-commerce.
    Uso de machine learning para prever demandas futuras.

8. Desafios Futuros e Melhorias
    Aperfeiçoar a interface do usuário para melhor experiência.
    Otimizar consultas ao banco de dados para alta escala.
    Implementar notificações automáticas para reposição de estoque.

9. Configuração Técnica
    Estrutura de Diretórios
    test.py → define classes (Pessoa, Funcionario, Produto, Pedido, Estoque) com atributos específicos e validações. Em seguida, utiliza testes unitários com unittest para verificar se as instâncias dessas classes são criadas corretamente e se os dados são atribuídos corretamente. Se algum erro ocorrer, o teste falha e exibe uma mensagem de erro.
    App.py → configura uma aplicação Flask, cria as tabelas no banco de dados e registra rotas modulares para diferentes funcionalidades (cliente, estoque, funcionário, pedido e produto). Em seguida, inicia o servidor Flask com as configurações especificadas.


    requirements → lista de dependências para uma aplicação Python que usa Flask para desenvolvimento web, SQLAlchemy e Alembic para gerenciamento de banco de dados, pandas e numpy para manipulação de dados, e ferramentas como Jupyter para desenvolvimento interativo.


    settings.py → Configurações gerais do projeto (Banco de Dados, Apps, Middleware, etc.).


    static/ e templates/ → Arquivos visuais e front-end.


    venv/ → Ambiente virtual do Python.





