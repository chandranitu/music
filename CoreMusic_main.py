# A Python program to print all
# permutations using library function

from itertools import permutations
from src.core.MusicApi import create_folder, create_file, char_to_string

# Get all permutations of [1, 2, 3]
# perm = permutations(["Sa", "re", "Re", "ga", "Ga", "ma", "Ma", "Pa", "dha", "Dha", "ni", "Ni"])


perm = permutations(["Sa", "re", "ga", "ma"])
# Print the obtained permutations

# create folder
pdir = "/home/hadoop/"
cdir = "musicTest"
pathtest = create_folder(pdir, cdir)

path123 = "/home/hadoop/musicTest"
lst = []  # This list will contain all P&C text and make file
for i in list(perm):
    str1 = char_to_string(i)
    lst.append(str1)
    create_file(lst, path123)

if __name__ == "__main__":
    print("")
