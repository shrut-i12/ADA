
from itertools import combinations
weight=[7,3,4,5,2]
values=[10,20,35,15,34]
capacity=12
n=len(weight)
best_value=0
best_subset=None

print("subset\t\tTotal weight|TotalValue")
print("-"*45)
for r in range(n+1):
    for subset in combinations(range(n),r):
        total_weight=sum(weight[i]for i in subset)
        total_value=sum(values[i]for i in subset)
        subset_display="{"+",".join(str(i+1) for i in subset)+ "}"
        
        if total_weight<= capacity:
            print(f"{subset_display:<15}{total_weight:<15}${total_value}")
            if total_value > best_value:
                best_value=total_value
                best_subset=subset
        else:
            print(f"{subset_display:<15}{total_weight:<15}notfeasible")
print("\nOptimal solution:")
print("items selected:",{i + 1 for i in best_subset })   
print("Maximum values:$",best_value)             