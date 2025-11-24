# *Trabalho ODS1 - AP2: Sistema de Recomendação de Mangás (Content-Based)* #

Segundo Trabalho Prático (AP2) da disciplina Oficina de Desenvolvimento de Sistemas 1.

---

## Objetivo do Sistema ##

Este projeto implementa uma plataforma de recomendação de mangás baseada em Filtragem por Conteúdo (Content-Based Filtering).

Este sistema analisa as características dos próprios mangás (como gênero, autor, tags e sinopse) para entender o perfil de gosto do utilizador. Se o utilizador avalia bem mangás de "Ação" e "Ninjas", o sistema recomendará outras obras que contenham essas mesmas palavras-chave e descrições similares, independentemente do que outros usuários pensam.

## Tecnologias Utilizadas ##

- Linguagem: Python 3.11+

- Backend: FastAPI

- Frontend: Streamlit

- Machine Learning / Processamento de Dados:

- Scikit-learn: Para vetorização de texto (TF-IDF) e cálculo de similaridade (Cosseno).

- Pandas & NumPy: Manipulação de dados e operações vetoriais.

## Instalação e Execução ##

### 1. Configurar o Ambiente Virtual

*Certifique-se de ter o Python 3.11+ instalado.*

Verificar Versão

```bash
python --version
```

Criar Ambiente Virtual

```bash
python -m venv venv
```

Ativat Ambiente Virtual

```bash
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate
```

### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 3. Rodar a Aplicação

*O sistema é dividido em duas partes que devem rodar simultaneamente em terminais diferentes (ambos com o venv ativado).*

**Terminal 1: Backend (API)**

```bash
cd backend
uvicorn app:app --reload
```

*O backend iniciará em http://127.0.0.1:8000 e carregará a matriz de inteligência TF-IDF automaticamente.*

**Terminal 2: Frontend (Interface)**

```bash
cd frontend
streamlit run app_streamlit.py
```

*O navegador abrirá automaticamente com a aplicação.*

## Lógica de Recomendação (Como Funciona)

*A lógica central está no arquivo backend/recommender.py e segue três etapas principais:*

### 1. Vetorização dos Itens (TF-IDF)

O sistema cria uma "sopa de metadados" para cada mangá, concatenando as seguintes informações:

- Categoria (Gênero)

- Autor

- Ano

- Título

- Tags (Ex: "Ninja", "Espadas", "Vampiros")

- Sinopse

Em seguida, utiliza o TF-IDF (Term Frequency-Inverse Document Frequency) para converter esse texto em vetores numéricos. Isso permite que o sistema entenda matematicamente a importância de cada palavra (por exemplo, a palavra "Ninja" será muito relevante para diferenciar Naruto de um romance escolar).

### 2. Construção do Perfil do Utilizador

O sistema analisa o histórico de avaliações do utilizador:

Seleciona todos os mangás que o utilizador avaliou com nota igual ou superior a 3 (considerados como "Gostei").

Calcula um vetor médio desses mangás. Esse vetor resultante representa o "gosto médio" do utilizador no espaço vetorial.

### 3. Geração de Recomendações (Similaridade de Cosseno)

Para recomendar:

O sistema calcula a Similaridade de Cosseno entre o Vetor do Perfil do Utilizador e os vetores de todos os mangás do catálogo.

Os mangás com maior similaridade (ângulos mais próximos) são retornados como recomendação, excluindo aqueles que o utilizador já viu.

## Métricas e Avaliação de Acurácia

O sistema possui uma rota dedicada (/avaliar_acuracia) para medir a performance das recomendações.

**Metodologia de Teste:**

As avaliações de um utilizador são divididas em Treino (50%) e Teste (50%).

O sistema gera recomendações usando apenas os dados de Treino.

Verifica-se se os itens recomendados aparecem na lista de Teste com avaliações positivas (Nota >= 3).

**Métricas Calculadas:**

Precision: Qual a porcentagem das recomendações geradas que o utilizador realmente gostou?

Recall: Dos itens que o utilizador gosta, quantos o sistema conseguiu encontrar?

F1-Score: Média harmônica entre Precision e Recall, oferecendo um balanço geral da performance.

### Estrutura de Arquivos
```bash
/
├── backend/
│   ├── app.py           # API FastAPI e rotas
│   ├── recommender.py   # Lógica do Content-Based Filtering
│   ├── items.csv        # Catálogo de mangás com metadados
│   └── ratings.csv      # Histórico de avaliações
├── frontend/
│   └── app_streamlit.py # Interface gráfica Streamlit
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação
```
