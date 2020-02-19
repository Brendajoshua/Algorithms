#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_batches = float('inf')
  #for each ingredient in the recipe
  for i in recipe:
      # if it doesn't exist in the ingredients, return 0
      if ingredients.get(i) is None:
        return 0
      # if it's more than the amount in tje ingredients, return 0
      if recipe[i] > ingredients[i]:
        return 0
      # if current batches is less than max batches, reassign max batches
      current_batches = ingredients[i] // recipe[i]
      if current_batches < max_batches:
        max_batches = current_batches

  return max_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))