# Mini API de Tarefas

Este repositório contém uma pequena API criada com **Django** e **Django REST Framework**. Ela segue o plano de estudos da Semana 1 e implementa um CRUD simples para tarefas.

## Como executar

1. Instale as dependências (necessário acesso à Internet):
   ```bash
   pip install -r requirements.txt
   ```
2. Acesse a pasta `triup` e aplique as migrações:
   ```bash
   cd triup
   python manage.py migrate
   ```
3. Ainda dentro da pasta `triup`, rode a aplicação:
   ```bash
   python manage.py runserver
   ```

Os endpoints da API ficam disponíveis em `/api/tasks/`.

## Relato de Aprendizado

- Criação de projetos e apps no Django
- Configuração do Django REST Framework
- Uso de `ModelSerializer` e `ViewSet`
- Roteamento com `DefaultRouter`
- Escrita de testes com `APITestCase`

## Checklist de Conceitos

- [x] Projeto Django iniciado
- [x] App dedicado para tarefas
- [x] Endpoints REST com DRF
- [x] Serialização e ViewSets
- [x] Testes básicos de API
