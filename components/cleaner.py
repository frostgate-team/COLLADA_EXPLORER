uniquelines = set(open('./out/matlist.txt', 'r', encoding='utf-8').readlines())
setter = open('./out/matlist.txt', 'w', encoding='utf-8').writelines(set(uniquelines))