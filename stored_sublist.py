# Make a solution that takes a list of numbers or strings and returns a list with the items from the original list stored into sublists. 
# Items of the same value should be in the same sublist.
# Examples [2, 1, 2, 1] ➞ [[2, 2], [1, 1]], [5, 4, 5, 5, 4, 3] ➞ [[5, 5, 5], [4, 4], [3]], ["b", "a", "b", "a", "c"] ➞ [["b", "b"], ["a", "a"], ["c"]]
# Notes The sublists should be returned in the order of each element's first appearance in the given list.

liste = [2, 1, 2, 1, "a", "b", "c", "a", "b", "a"]
elements = {}

for i in liste :
    if i not in elements :
        elements[i] = [i]
    else :
        elements[i] += [i]
print(list(elements.values()))