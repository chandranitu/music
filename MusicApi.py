import os


# this method will create a folder if doesn't exist
def create_folder(pdir, cdir):
    # Parent Directory path
    global error
    # mode
    mode = 0o777
    exist_ok = False
    # Path
    path = os.path.join(pdir, cdir)
    try:
        os.mkdir(path, mode)
    except OSError as error:
        print(error)
    print("Directory '% s' created" % path)


# this method will generate complete file according to generated in for loop
def create_file(lst, path1):
    for i in list(lst):
        filename = os.path.join(path1, i + ".txt")
        file1 = open(filename, "w")
        toFile = i
        file1.write(toFile)
        file1.close()


# this method will combine char to string for file name
# Example  ('Sa', 're', 'ga', 'ma')  -> Saregama.txt
def char_to_string(s):
    # initialization of string to ""
    new = ""

    # traverse in the string
    for x in s:
        new += x

        # return string
    return new
