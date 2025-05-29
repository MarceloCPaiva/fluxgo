# FluxGo 🚀

FluxGo é um projeto Django desenvolvido com fins de estudo e prática, com foco em construir uma plataforma simples para solicitação de serviços com um blog integrado. Ele segue boas práticas de organização, componentização e estilização com TailwindCSS.

---

## 🌟 Funcionalidades

- ✅ Página inicial com identidade visual moderna
- ✅ Página de serviços
- ✅ Página de blog com listagem e detalhe de posts
- ✅ Formulário de solicitação de atendimento com persistência no banco de dados
- ✅ Página de agradecimento após envio do formulário
- ✅ Design responsivo com TailwindCSS

---

## 🧠 Tecnologias Utilizadas

- [Python 3.12+](https://www.python.org/)
- [Django 5.x](https://www.djangoproject.com/)
- [TailwindCSS](https://tailwindcss.com/)
- HTML5 + CSS3
- SQLite (como banco de dados padrão para desenvolvimento)

---

## 📁 Estrutura de Pastas

```
fluxgo/
│
├── core/                # App principal
│   ├── templates/       # Templates HTML
│   ├── static/          # Arquivos estáticos (logo, CSS)
│   ├── models.py        # Modelos do banco de dados
│   ├── views.py         # Lógica de renderização das páginas
│   ├── urls.py          # Rotas do app core
│   └── forms.py         # Formulários (Django Forms)
│
├── fluxgo/              # Configurações globais do projeto
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── db.sqlite3           # Banco de dados local
├── manage.py            # Utilitário de linha de comando Django
└── README.md
```

---

## 🧪 Como Rodar o Projeto Localmente

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/fluxgo.git
cd fluxgo
```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

> Se ainda não tiver o `requirements.txt`, rode:
> ```bash
> pip freeze > requirements.txt
> ```

4. **Aplique as migrações do banco de dados:**

```bash
python manage.py migrate
```

5. **Execute o servidor de desenvolvimento:**

```bash
python manage.py runserver
```

6. **Acesse no navegador:**

```
http://127.0.0.1:8000/
```

---

## 🛠 Próximos Passos (V2)

- Autenticação e login de usuários
- Dashboard para visualizar solicitações
- Área administrativa estilizada
- Integração com API ou envio de e-mail automático
- Deploy (Vercel, Heroku, etc.)

---

## 📚 Aprendizado

Esse projeto serviu como base prática para dominar:

- Estrutura de um projeto Django
- Organização de views, models e templates
- Manipulação de formulários com `ModelForm`
- Salvamento de dados no banco
- Uso de TailwindCSS com Django

---

## 📸 Capturas de Tela

> (Insira aqui imagens do layout para tornar o repositório mais atrativo)

---

## 📄 Licença

Projeto de uso educacional. Sinta-se livre para usar como base e evoluir por conta própria. 🚀

---

Desenvolvido por [Marcelo Eduardo das Chagas Paiva](https://www.linkedin.com/in/marcelocpaiva/).
