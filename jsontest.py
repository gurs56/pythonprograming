import requests
import json

response = requests.get("https://edamam-edamam-nutrition-analysis.p.rapidapi.com/api/nutrition-data?ingr=1+large+apple",
  headers={
    "X-RapidAPI-Host": "edamam-edamam-nutrition-analysis.p.rapidapi.com",
    "X-RapidAPI-Key": "1ddebe7807mshf5fefb0b64dfa07p175361jsn4f4289dba7e0"
  }
)


food_data = response.json()
with open('food.json', 'w') as json_file:
  json.dump(food_data, json_file)

