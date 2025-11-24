from fastapi import FastAPI
import pandas as pd
# Adicionar prepare_data_and_vectorize na importação
from recommender import get_recommendations, evaluate_accuracy, calculate_overall_accuracy, prepare_data_and_vectorize

app = FastAPI()

# Carrega os dados
items_df = pd.read_csv("items.csv")

# Inicializa a "inteligência" do sistema (Gera a matriz TF-IDF) assim que o servidor liga
# Isso garante que o sistema já saiba ler os mangás antes do primeiro usuário chegar
prepare_data_and_vectorize(items_df)

@app.get("/")
def root():
    return {"message": "Manga Recommender API online (Content-Based)"}

@app.get("/recomendar/{user_id}")
def recomendar(user_id: int):
    # Recarrega o arquivo de avaliações a cada chamada (para pegar novas notas)
    ratings_df = pd.read_csv("ratings.csv")
    recs = get_recommendations(user_id, items_df, ratings_df)
    return {"user_id": user_id, "recommendations": recs}

@app.get("/avaliar_acuracia/{user_id}")
def avaliar_acuracia(user_id: int):
    ratings_df = pd.read_csv("ratings.csv")
    result = evaluate_accuracy(user_id, items_df, ratings_df)
    if "message" in result:
        return {"message": result["message"]}
    return result

@app.get("/avaliar_acuracia_geral")
def avaliar_acuracia_geral():
    ratings_df = pd.read_csv("ratings.csv")
    result = calculate_overall_accuracy(items_df, ratings_df)
    return result