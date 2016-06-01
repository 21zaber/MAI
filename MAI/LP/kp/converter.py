from gedcom import Gedcom

def readgedcom(path):
    root = Gedcom(path)
    people = {}
    families = []
    d = root.element_dict()
    for i in d:
        elem = d[i]
        id = i
        if elem.is_individual():
            name = ''
            for i in elem.children():
                if i.tag() == 'NAME':
                    name = i.value().replace('/', '')
            people[id] = name
        else:
            fam = [[], 0, 0]
            for i in elem.children():
                if i.tag() == 'CHIL':
                    fam[0].append(i.value())
                if i.tag() == 'HUSB':
                    fam[1] = i.value()
                if i.tag() == 'WIFE':
                    fam[2] = i.value()
            families.append(fam)
    return (people, families)

people, families = readgedcom('tree1.ged')
for i in families:       
    for child in i[0]:
        print('parents("{}", "{}", "{}").'.format(people[child], people[i[1]], people[i[2]]))

print()
print('shurin(X, Ans):-')
print('\tparents(_, X, Wife), % X has a Wife')
print('\tparents(Wife, A, B), % Wife has a parents')
print('\tparents(Ans, A, B),  % Wife\'s parents have a son or dauther - Ans')
print('\tparents(_, Ans, _).  % Ans is a man')

print()
print('shurin("Роман Опенько", Ans).')

