from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load CSV data into a DataFrame
df = pd.read_csv('IndianFoodDatasetCSV.csv')

# Function to extract unique cuisine and course values
def get_unique_cuisines():
    return df['Cuisine'].unique()

def get_unique_courses(selected_cuisine=None):
    if selected_cuisine:
        return df[df['Cuisine'] == selected_cuisine]['Course'].unique()
    else:
        return df['Course'].unique()  # Return all unique courses if no cuisine selected

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggestions', methods=['POST'])
def suggestions():
    selected_cuisine = request.form['cuisine']
    selected_course = request.form['course']

    if selected_cuisine and selected_course:
        filtered_df = df[df['Cuisine'] == selected_cuisine]
        filtered_df = filtered_df[filtered_df['Course'] == selected_course]
    elif selected_cuisine:
        filtered_df = df[df['Cuisine'] == selected_cuisine]
    else:
        filtered_df = df.copy()  # Show all recipes if no selection

    recipes = filtered_df[['RecipeName', 'Course', 'PrepTimeInMins', 'CookTimeInMins']].to_dict('records')  # Prepare data for template
    return render_template('suggestions.html', recipes=recipes)

@app.route('/recipe/<recipe_id>' , methods=['GET', 'POST'])  # New route for recipe details
def recipe_details(recipe_id):
    selected_recipe = df[df['RecipeName'] == recipe_id]  # Get recipe details by name

    if selected_recipe.empty:  # Handle case where recipe is not found
        return render_template('error.html', message="Recipe not found")

    recipe_details = selected_recipe.to_dict('records')[0]  # Convert to dictionary
    return render_template('recipe_details.html', recipe=recipe_details)


# Replace with your actual API credentials
API_ID = "7aa516a5"
API_KEY = "dc836a223fb788b11ae390504d9e97ce"

@app.route('/recipefinder')  # This route defines the `recipefinder` page
def recipefinder():
  # Your logic for handling the recipe finder page (e.g., retrieving recipe data)
  return render_template('ReciepeFinder.html')  # Updated filename

@app.route('/search_recipes', methods=['POST'])
def search_recipes():
  search_term = request.form['search']
  # Implement logic to use search_term with API credentials (API_ID, API_KEY) to retrieve recipes
  # You can use a library like requests for making API calls
  recipes = []  # Replace with actual recipe data retrieved from API
  return render_template('ReciepeFinder.html', recipes=recipes)

# New routes for the three modes
@app.route('/pantry-mode')
def pantry_mode():
    cuisines = get_unique_cuisines()
    courses = get_unique_courses()
    return render_template('pantry_mode.html', cuisines=cuisines, courses=courses)

@app.route('/cook-mode')
def cook_mode():
    cuisines = get_unique_cuisines()
    courses = get_unique_courses()
    return render_template('cook_mode.html', cuisines=cuisines, courses=courses)

@app.route('/cook-mode-suggestions', methods=['POST'])
def cook_mode_suggestions():
    selected_cuisine = request.form.get('cuisine', '')
    selected_course = request.form.get('course', '')
    max_time = request.form.get('time', '')
    mood = request.form.get('mood', '')
    
    # Start with all recipes
    filtered_df = df.copy()
    
    # Filter by cuisine
    if selected_cuisine:
        filtered_df = filtered_df[filtered_df['Cuisine'] == selected_cuisine]
    
    # Filter by course
    if selected_course:
        filtered_df = filtered_df[filtered_df['Course'] == selected_course]
    
    # Filter by time (TotalTimeInMins)
    if max_time:
        max_time_int = int(max_time)
        filtered_df = filtered_df[filtered_df['TotalTimeInMins'] <= max_time_int]
    
    # Filter by mood (map to Diet or Course)
    if mood:
        if mood == 'healthy':
            # Healthy mood: filter for vegetarian/vegan diets
            filtered_df = filtered_df[filtered_df['Diet'].isin(['Vegetarian', 'Vegan'])]
        elif mood == 'comfort':
            # Comfort food: typically main courses or desserts
            filtered_df = filtered_df[filtered_df['Course'].isin(['Main Course', 'Dessert'])]
        elif mood == 'quick':
            # Quick: filter for recipes with less than 30 minutes total time
            filtered_df = filtered_df[filtered_df['TotalTimeInMins'] <= 30]
        elif mood == 'indulgent':
            # Indulgent: desserts or snacks
            filtered_df = filtered_df[filtered_df['Course'].isin(['Dessert', 'Snack'])]
    
    # Select relevant columns for display
    recipes = filtered_df[['RecipeName', 'TranslatedRecipeName', 'Course', 'PrepTimeInMins', 
                           'CookTimeInMins', 'TotalTimeInMins', 'Servings', 'Diet', 'Cuisine']].to_dict('records')
    
    return render_template('cook_mode_results.html', recipes=recipes, 
                          cuisine=selected_cuisine, course=selected_course, 
                          time=max_time, mood=mood)

@app.route('/order-mode')
def order_mode():
    return render_template('order_mode.html')



if __name__ == "__main__":
    app.run(debug=True)