from shopping_list import Recipe,PrettyRecipe, RecipesBox, Fridge,PrettyFridge, check_the_fridge, \
    prepare_shopping_list, shopping_list_archive

print('--------------------------')
print('Customer facing showcase')
print('--------------------------')
print('')

# create the ingredients dict for multiple recipes, containing name and quantity of an ingredient
mac_and_cheese_ingredients = {
    'macaroni': 1,
    'cheese': 0.5
}

mac_and_cheese = Recipe(
    "Famous Mac & Cheese",
    mac_and_cheese_ingredients
)

hot_chocolate_ingredients = {
    'chocolate': 0.15,
    'milk': 0.5
}

hot_chocolate = PrettyRecipe(
    "Hot Chocolate",
    hot_chocolate_ingredients
)

burger_ingredients = {
    'bun': 1,
    'ground_beef': 1,
    'ceedar_cheese': 0.5,
    'onion': 2,
    'salad': 1,
    'smoked_sauce': 2
}
hot_dog_ingredients = {
            'bun': 1,
            'sausage': 1,
            'mustard': 0.5,
            'ketchup': 0.5
}
ribs_and_potato_ingredients = {
    'ribs': 2,
    'potato': 1,
    'chilli_sauce': 0.5,
    'garlic_sauce': 0.5,
    'pickles': 1
}
english_breakfast_ingredients = {
    'ham': 1,
    'egg': 2,
    'beans': 0.5,
    'cheese': 1,
    'tomatos': 1,
    'salad': 0.5
}
pizza_ingredients = {
    'dough': 1,
    'tomato_sauce': 1,
    'mozzarela': 2,
    'prosciutto': 4,
    'rucola': 0.5
}
pasta_carbonara_ingredients = {
    'pasta': 2,
    'bacon': 1,
    'sour_cream': 0.5,
    'egg': 1,
    'parmegiano': 0.5,
    'olivee_oil': 0.5
}

# create instances for each recipe by its title and dict of ingredients
# print('\n\033[34m RECIPES \033[0m\n')

burger = PrettyRecipe("Beef Burger", burger_ingredients)
# print(burger)
# # print(burger.__repr__())

hot_dog = PrettyRecipe('Hot Dog', hot_dog_ingredients)
# print(hot_dog)
# # print(hot_dog.__repr__())

ribs_and_poato = PrettyRecipe('Ribs and Potato', ribs_and_potato_ingredients)
# print(ribs_and_poato)
# # print(ribs_and_poato.__repr__())

english_breakfast = PrettyRecipe('English Breakfast', english_breakfast_ingredients)
# print(english_breakfast)
# # print(english_breakfast.__repr__())

pizza = PrettyRecipe('Pizza Prociutto Crudo', pizza_ingredients)
# print(pizza)
# # print(pizza.__repr__())

pasta_carbonara = PrettyRecipe('Pasta carbonara', pasta_carbonara_ingredients) 
# print(pasta_carbonara)
# # print(pasta_carbonara.__repr__())

# create the recipes_box database as a RecipesBox instance , and add recipes in
# print('\n\033[34m RECIPES BOX \033[0m\n')

recipes_box = RecipesBox()
recipes_box.append(burger)
recipes_box.append(hot_dog)
recipes_box.append(ribs_and_poato)
recipes_box.append(english_breakfast)
recipes_box.append(pizza)
recipes_box.append(pasta_carbonara)
# print(recipes_box)

# recipes_box.pop()
# print(recipes_box)
# burger_recipe = recipes_box.pick(burger)
# print(burger_recipe)

# # create the fridge, as an instance of Frige, and add ingredients in
# print('\n\033[34m FRIDGE \033[0m\n')

fridge = PrettyFridge()
fridge['mustard'] = 10
fridge['ketchup'] = 0.1
fridge.update({'bun': 100})
fridge.update({'sausage': 100})
fridge.update({'onion': 100})
fridge.update({'salad': 100})
fridge.update({'potato': 50})
fridge.update({'garlic_sauce': 35})
fridge.update({'ribs': 1})
fridge.update({'pasta': 10})
fridge.update({'bacon': 15})
fridge.update({'egg': 30})
# print(fridge)
fridge.check_ingredient('ketchup')

# # test if an intredient is in the fridge
# print('\n\033[34m IS ... IN THE FRIDGE ? \033[0m\n')

# ingredient_test_list = ['mustard', 'onion', 'ground beef']
# for ingredient in ingredient_test_list:
#     print(f'Is {ingredient} in the fridge?')
#     fridge.check_ingredient(ingredient)

# # add and extract ingredients in/from the fridge , and test the case when the quantity is 0
# print('\n\033[34m UPDATE INGREDIENTS IN FRIGE \033[0m\n')

# print('Fridge intial: ', '\n', fridge, sep='')
# fridge.add_ingredient_in_fridge('bun', 15)
# fridge.add_ingredient_in_fridge('potato', 100)
# print('+ 15 buns and + 100 potato:', '\n', fridge, sep='')
# print('- 100 onion: ')
# fridge.remove_ingredient_from_fridge('onion', 100)
# print(fridge)

# # check if there are ingredients for a recipe in the fridge and
# # return list with presnt ingredients and with misiing ingredients
# print('\n\033[34m CHECK RECIPE \033[0m\n')

# for recipe in recipes_box:
#     print('\ncheck_recipe for ', recipe.recipe_name)
#     print('Recipe:', '\n', recipe, '\n')
#     print('Fridge content:', '\n', fridge, sep='')
#     shopping_list = fridge.check_recipe(recipe)
#     print('Ingredients missing: ', shopping_list)

# # check the fridge if has ingredients for recipes, return a list of recipes
# # for wich there are at lest half of ingredients im the fridge
# print('\n\033[34m CHECK THE FRIDGE \033[0m\n')

# viable_recipes_box = check_the_fridge(fridge, recipes_box)
# print(f'For next recipes there has at least half of ingredients in the fridge:\n')
# for recipe in viable_recipes_box:
#     print(f'- {recipe}')

# # test pick a recipe
# print('\n\033[34m PICK A RECIPE \033[0m\n')

# recipe = recipes_box.pick(english_breakfast)
# print(f'You pick {recipe.recipe_name} recipe =>\n{recipe}')

# # test pick a random recipe
# print('\n\033[34m PICK A RANDOM RECIPE 2 TIMES \033[0m\n')
# for x in range(2):
#     random_recipe = recipes_box.pick()
#     print(f'Pick a random recipe =>\n{random_recipe}\n')

# check the fridge if contains all the necessary ingredients for a recipe,
# if not print a fancy shopping list, and add this to a archive
print('\n\033[34m PREPARE SHOPPING LIST FOR ALL RECIPES \033[0m\n')

for recipe in recipes_box:
    print(f'\nShopping List for {recipe.recipe_name}:\n')
    prepare_shopping_list(fridge, recipe)
    # pass
# print(recipes_box)
# print(fridge)


# # print the shopping lists archive
# print('\n\033[34m SHOPPING LIST ARCHIVE \033[0m\n')

# for shopping_list in shopping_list_archive:
#     print(shopping_list)

# # print(shopping_list_archive)

# # Previous showcase

# print('')
# print('--------------------------')
# print('Simplified showcase')
# print('--------------------------')
# print('')
# print('Showcase Recipe Printing:')

# print(hot_chocolate)
# hot_chocolate.pretty_print()

# our_recipes_box = RecipesBox()
# our_recipes_box.append(hot_chocolate)
# our_recipes_box.append(mac_and_cheese)
# print (our_recipes_box)

# our_recipes_box.remove(mac_and_cheese)
# print(our_recipes_box)

# our_recipes_box.pick(hot_chocolate)
# print(our_recipes_box.pick(hot_chocolate))

# # Fridge tests
# in_the_fridge = {'macaroni' : 1, 'cheese': 0.5}
# our_fridge = PrettyFridge(ingredients=in_the_fridge)
# print(our_fridge)
# print ('cheese' in our_fridge)
# our_fridge.check_ingredient('cheese')
# for ingredient in our_fridge:
#     print (ingredient, our_fridge[ingredient])
# print (len(our_fridge))
# # print (our_fridge)
# # our_fridge.__setitem__('avocado', 3)
# # print (our_fridge)
# # our_fridge.__delitem__('cheese')
# # print (our_fridge)
# # our_fridge.add_ingredient_in_fridge('potatoes', 8)
# # print (our_fridge)
# # our_fridge.add_ingredient_in_fridge('potatoes', 4)
# # print (our_fridge)
# # our_fridge.remove_ingredient_from_fridge('potatoes', 6)
# # print (our_fridge)
# # our_fridge.remove_ingredient_from_fridge('potatoes', 6)
# # print (our_fridge)

# #in_the_fridge = {'milk' : 0.2, 'chocolate': 0.5,}
# #our_fridge = PrettyFridge(ingredients=in_the_fridge)
# # print (our_fridge)
# # print (our_fridge.inside_fridge) #verific ca primesc un dictionar
            

# our_fridge.check_recipe(hot_chocolate)
# our_fridge.pretty_print()