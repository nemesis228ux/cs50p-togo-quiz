from project import get_only_available_categories, check_answer, load_quiz_questions

def test_get_only_available_categories():
  mock_data = {
    "Histoire": [{"question": "Q1", "options": ["1. A"], "reponse": "1"}],
    "Sport": [{"question": "Q2", "options": ["1. B"], "reponse": "1"}]
  }
  
  resultat = get_only_available_categories(mock_data)
  assert resultat == ["Histoire", "Sport"]
  assert isinstance(resultat, list)

def test_check_answer():
  assert check_answer("2", "2") is True
  assert check_answer(" 1 ", "1") is True 
  assert check_answer("3", "2") is False

def test_load_quiz_questions_not_found():
  resultat = load_quiz_questions("not_existing_file.json")
  assert resultat is None

def test_load_quiz_questions_success():
  resultat = load_quiz_questions("quiz.json")
  assert isinstance(resultat, dict)
  assert len(resultat) > 0