from os import listdir
from os.path import join, isdir

def get_files(root):
    l = []
    for file in listdir(root):
        path = join(root, file)
        if not isdir(path):
            l += [path,]
        else:
            l += get_files(path)

    return l

for i in range(1, 10):
    root_path = '{}/'.format(i)
    files = get_files(root_path)

    with open("listing{}.txt".format(i), 'w') as f:
        for file in files:
            f.write('\n{}:\n'.format(file.rsplit('/')[-1]))
            with open(file, 'r') as fl:
                for i in fl.readlines():
                    f.write(i)


