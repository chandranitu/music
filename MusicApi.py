import os


def create_folder():
    return


# Parent Directory path
parent_dir = "/home/hadoop/"
# Directory
directory = "musicTest"
# mode
mode = 0o777
exist_ok = False
# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# '/home / hadoop / '

try:
    os.mkdir(path, mode)
except OSError as error:
    print(error)

print("Directory '% s' created" % directory)


def create_file(lst, folder):
    return 0
