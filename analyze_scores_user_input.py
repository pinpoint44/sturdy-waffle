scores = []

for i in range(4):
    item = int(input(f"Enter 4 scores: "))
    scores.append(item)
#Sample scores : 25, 35, 40, 28
print("\nYour list of scores:")
print(scores)

def analyze_scores(scores):
    if not scores:
        return "No scores to analyze."

    average_score = sum(scores) / len(scores)
    
    print(f"Average score: {average_score:.1f}")
 
analyze_scores(scores)
