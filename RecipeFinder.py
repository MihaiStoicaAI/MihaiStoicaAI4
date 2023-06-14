import requests

class RecipeFinder:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def find_recipes(self):
        try:
            url = "https://api.example.com/recipes"
            payload = {"ingredients": self.ingredients}
            response = requests.get(url, params=payload)
            recipe_data = response.json()

            # Process recipe data here
            # ...

            # Placeholder output
            print(f"Recipes found using ingredients: {', '.join(self.ingredients)}")
            print("1. Spaghetti Bolognese")
            print("2. Chicken Stir-Fry")
            print("3. Vegetable Curry")
        except requests.exceptions.RequestException:
            print("Error occurred while retrieving recipes.")
        except ValueError:
            print("Error occurred while parsing recipe data.")

def main():
    ingredients = ["chicken", "broccoli", "soy sauce"]

    finder = RecipeFinder(ingredients)
    finder.find_recipes()

if __name__ == "__main__":
    main()
