# A Python program to print all
# permutations using library function

from itertools import permutations
from src.core.MusicApi import create_folder

# Get all permutations of [1, 2, 3]
# perm = permutations(["Sa", "re", "Re", "ga", "Ga", "ma", "Ma", "Pa", "dha", "Dha", "ni", "Ni"])


perm = permutations(["Sa", "re", "ga", "ma"])
# Print the obtained permutations

create_folder
for i in list(perm):
    print(i)

if __name__ == "__main__":
    print("")
