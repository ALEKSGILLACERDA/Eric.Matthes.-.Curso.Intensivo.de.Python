unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
current_design = unprinted_designs.pop()
completed_models.append(current_design)
print("Printing model: " + current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)