import sys

from pyfiglet import Figlet
from tabulate import tabulate
import json
import time


def main():
  figlet = Figlet(font="small")
  data: dict = load_quiz_questions("quiz.json")

  print(figlet.renderText("BIENVENUE SUR TOGO QUIZ"))

  category: int = get_category(data)
  match category:
    case 1: 
      ask_questions(data, "Histoire")
    case 2: 
      ask_questions(data, "Politique")
    case 3: 
      ask_questions(data, "Geographie")
    case 4: 
      ask_questions(data, "Culture et Traditions")
    case 5: 
      ask_questions(data, "Sport")



## load quiz question on Togo
def load_quiz_questions(filename: str):
  try:
    with open(file=filename, mode="r", encoding="utf-8") as file:
      return json.load(file)
  except FileNotFoundError:
    return


def get_only_available_categories(data: dict):
  available = []
  for k in data.keys():
    available.append(k)

  return available


## get user categorie choice
def get_category(data: dict):
  av_cat = get_only_available_categories(data)
  for i, c in enumerate(av_cat, start=1):
    print(f"{i}. {c}")
  try:
    category = int(input("\nChoisis ta categorie de jeux: "))
    if category < 1 or category > len(av_cat):
      raise ValueError
  except ValueError:
    print("\nChoisis un nombre valide")
    return get_category(data)
  else:
    return category


def ask_questions(data: dict, category: str):
  """Pose les questions d'une catégorie avec un système de score et de temps."""
  questions: list[dict] = data[category]
  score = 0

  for i, q in enumerate(questions, 1):
    print("\n" + "=" * 50)
    print(f"Question {i} / {len(questions)}")
    print(f"{q['question']}")
    print("-" * 50)

    table_data = [[opt] for opt in q["options"]]
    print(tabulate(table_data, headers="disable", tablefmt="rounded_grid"))

    start_time = time.time()
    
    reponse_utilisateur = input("\nVotre choix (entrez le numéro) : ").strip()
    
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 1)

    print(f"Temps pris : {elapsed_time} secondes.")

    if check_answer(reponse_utilisateur, q["reponse"]):
        print("Youuuupii Bonne réponse !")
        score += 1
    else:
        print(f"Ouuups Mauvaise réponse. La bonne réponse était : {q['reponse']}")

  print("\n" + "=" * 50)
  print(f"Quiz terminé ! Votre score final : {score} / {len(questions)}")
  return score


def check_answer(user_answer: str, correct_answer: str) -> bool:
  """Vérifie si la réponse de l'utilisateur correspond à la bonne réponse."""
  return user_answer.strip() == str(correct_answer).strip()

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    sys.exit()
