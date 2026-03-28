from itertools import combinations
def minimum_components(components):
  # Write code below 💖
  

  target = 42

  for k in range(1, len(components)+1):
    for combo in combinations(components, k):
      if sum(combo) == target:
        return k
    
  return -1