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
    cuisines = get_unique_cuisines()
    courses = get_unique_courses()  # Initially get all courses
    return render_template('index.html', cuisines=cuisines, courses=courses)

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

if __name__ == '__main__':
    app.run(debug=True)
