from apted import APTED, helpers

tree1 = helpers.Tree.from_text("{a{b}{c}}")
apted = APTED(tree1, tree1)
ted = apted.compute_edit_distance()
print(ted)
mapping = apted.compute_edit_mapping()
print(mapping)