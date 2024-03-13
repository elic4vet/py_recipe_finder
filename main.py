'''Required Tasks
These are the required tasks for this project. You should aim to complete these tasks before
adding your own ideas to the project.
1. Read the Edamam API documentation ★
https://developer.edamam.com/edamam-docs-recipe-api
2. Ask the user to enter an ingredient that they want to search for
3. Create a function that makes a request to the Edamam API with the required ingredient as
part of the search query (also included your Application ID and Application Key
4. Get the returned recipes from the API response
5. Display the recipes for each search result

Ideas for Extending the Project
Here are a few ideas for extending the project beyond the required tasks. These ideas are just
suggestions, feel free to come up with your own ideas and extend the program however you want.
● Save the results to a file
● Order the results by weight or another piece of data
● Ask the user additional questions to decide which recipe they should choose
● Cross-reference the ingredient against the Edamam nutrition analysis API
● Use a different searchable API (suggestions in useful resources)

'''

import requests
import json

def recipe_search(ingredient):
    app_id = '71b823dc'
    app_key = '47f63a9d595964e03745d3fb261eba0a'

    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    return data['hits']

def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)
    
    recipe_data_list = []
    for result in results:
        recipe = result['recipe']
        recipe_data = {
            'label': recipe['label'],
            'uri': recipe['url']
        }
        print(recipe['label'])
        print(recipe['url'])
        recipe_data_list.append(recipe_data)
    
    filename = '{}_research_results.json'.format(ingredient.replace(' ', '_')) 
    with open(filename, 'w') as f: 
        json.dump(recipe_data_list, f, indent=4) 

run()
