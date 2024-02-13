# Asset Manager

Asset Manager é uma aplicação web desenvolvida em Django para gerenciar ativos de TI, como equipamentos, localizações, setores, grupos, categorias e fabricantes.

## Capturas de tela


### Tela de Login
![Tela de Login](screenshots/asset_manager_login.jpg)

### Dashboard
![Dashboard](screenshots/asset_manager_home.jpg)

### Página de Ativos
![Página de Ativos](screenshots/asset_manager_assets_page.jpg)

### Página de Cadastros
![Página de Cadastros](screenshots/asset_manager_assets_add.jpg)

## Funcionalidades

- Autenticação de usuário: Login e Logout.
- Dashboard: Visualização de estatísticas e resumos dos ativos.
- Gerenciamento de Ativos: Cadastro, edição e exclusão de equipamentos.
- Filtros: Filtre os ativos por localização, setor, grupo, categoria, fabricante e status.

## Instalação

1. Clone o repositório:
    ```
    git clone https://github.com/alexfructo/asset-manager.git
    ```

2. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```

3. Execute as migrações:
    ```
    python manage.py migrate
    ```

4. Inicie o servidor:
    ```
    python manage.py runserver
    ```

## Tecnologias Utilizadas

- Django: Framework web em Python para desenvolvimento rápido.
- HTML/CSS: Frontend para a interface de usuário.
- JavaScript: Para interatividade dinâmica na aplicação.
- Bootstrap: Framework CSS para design responsivo e componentes front-end.
