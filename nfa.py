def open_file(filename):
    file = open(filename, "r")
    content = file.readlines()
    file.close()
    return content

