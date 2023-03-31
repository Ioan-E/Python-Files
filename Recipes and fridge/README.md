## Thermomix app mockup - recipies and fridge

### Description

The app provides a list of the needed ingredients based on a recipe and a fridge content. 

It uses two classes: one for all recipes, and another for the fridge content. Both provide the functionality to add or modify recipes/ingredients. The most important feature is to provide a shopping list with the ingredients that are not available.

This project brought a particularly hard challenge. That was to define two decorators for the prepare_shopping_list() function.

I had to make sure that the decorator that archives the shopping list was applied before the decorator that improves its appearance, as the archived version should maintain its original formatting. To solve this, I researched the proper syntax for applying multiple decorators and tested various arrangements until I found the correct order.

Another obstacle was applying a mixin to improve the appearance of the shopping list. This involved understanding how a Mixin Class is behaving and how inheritance is used to deploy such class. I overcame these challange through research, experimentation, and testing until I found the correct solution.

In summary, the obstacles I faced helped me develop an app that can take the information on a recipe, compare it with the content of a fridge, and deliver a list of needed ingredients. All this while keeping a pythonic approach to the code.

### How to run and use the project

1. Fork the repository.
2. Clone the forked repository
3. Go to playground, add recipies (several examples are provided).
4. Add the existing ingredients. Some are already available.
5. Check if all required ingredients are avaialble - fridge.check_recipe(recipe).
6. Prepare a shoppping list - prepare_shopping_list(fridge, recipe).
