import pandas as pd

# Load the data
data = pd.read_csv('test.csv')

# Define a function to check if a given rule is an association rule
def is_association_rule(antecedent, consequent, support_threshold=4, confidence_threshold=0.5):
    support_antecedent = data[antecedent].sum()
    consequent_items = consequent.split(',')
    support_both = data[data[antecedent] == 1][consequent_items].all(axis=1).sum()
    confidence = support_both / support_antecedent
    support = support_both
    return support >= support_threshold and confidence >= confidence_threshold

# Define test cases
test_cases = [
    ("Brie", "Brie,Whipped cream"),
    ("Whipped cream", "Whipped cream,Tomato sauce"),
    ("Nutella", "Whipped cream,Nutella"),
    ("Tomato sauce", "Brie,Whipped cream"),
    ("Brie,Nutella", "Brie,Tomato sauce,Nutella")
]

# Evaluate test cases
for antecedent, consequent in test_cases:
    antecedent_list = antecedent.split(',')
    is_association = is_association_rule(antecedent_list[0], consequent)
    print(f"Rule: {{ {antecedent} }} -> {{ {consequent} }} is an association rule: {is_association}")
