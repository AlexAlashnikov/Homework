def names_gen(the_path: str, search: str) -> str:
    """Открывает файл, по заданной букве выводит имена"""
    with open(the_path) as file:
        the_path1 = file.readlines()
        search = search.upper()
        for i in the_path1:
            if i[0] == search:
                yield i.strip()


name_lookup = names_gen('unsorted_names.txt', 'p')
for name in name_lookup:
    print(name)