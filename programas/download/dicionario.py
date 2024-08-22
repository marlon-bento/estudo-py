import os
from pathlib import Path
dir_path = os.path.dirname(os.path.realpath(__file__))
for meta_file in os.listdir(str(dir_path)+'/data/meta-data'):
    print(meta_file)

def extract_entity_name(filename):
    return filename.split('.')[0]

extract_entity_name('Licitacao.txt')

def read_meta_data(path):
    data = open(path, "rt")
    meta_data = []
    for line in data:
        line_data = line.split('\t')
        meta_data.append((line_data[0],line_data[1],line_data[2]))
    data.close()
    return meta_data
print(read_meta_data(str(dir_path)+'/data/meta-data/Instituicao.txt'))
print("teste")