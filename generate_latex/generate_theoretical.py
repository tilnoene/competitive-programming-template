# Code provided by Tiago de Souza Fernandes from University of Brasilia
# Repo: Tiagosf00/Competitive-Programming

import os
import subprocess
import shutil
from functools import cmp_to_key

def compare(x, y):
    if x == 'general.tex':
        return -1
    if y == 'general.tex':
        return 1
    
    if x < y:
        return 1
    else:
        return -1

def cpy_template():
    shutil.copyfile('generate_latex/template_theoretical.tex', 'generate_latex/theoretical.tex')

def get_blocked():
    blocked = set()
    with open("generate_latex/block_from_theoretical.txt") as f:
        for line in f:
            # Remove comments
            line = line.split('#')[0]
            # Normalize filename
            line = line.strip().lower().replace(" ", "_") + ".tex"
            blocked.add(line)
    return blocked


def remove_aux():
    items = [
        'theoretical.aux',
        'theoretical.log',
        'theoretical.toc',
        'theoretical.tex',
        'texput.log',
        'generate_latex/theoretical.tex',
        'theoretical.out',
    ]
    for item in items:
        if os.path.exists(item):
            os.remove(item)

def move_output():
  if os.path.exists('/theoretical.pdf'):
    os.remove('/theoretical.pdf')

  if os.path.exists('generate_latex/theoretical.pdf'):
    shutil.move('generate_latex/theoretical.pdf', '/')

def get_dir():
    path = 'theoretical'
    section_list = os.listdir(path)
    section = []
    
    if 'assets' in section_list:
        section_list.remove('assets')

    for section_name in section_list:
        subsection = []
        section_path = os.path.join(path, section_name)
        items = sorted(os.listdir(section_path), key=cmp_to_key(compare))
        
        for file_name in items:
            if file_name.endswith('.tex'):
                subsection.append(file_name)
            elif(os.path.isdir(os.path.join(section_path, file_name))):
                # Sub Directory
                sub_files = os.listdir(os.path.join(section_path, file_name))
                subsection.extend([
                    os.path.join(file_name, name) \
                    for name in sub_files if name.endswith('.tex')
                ])

        section.append((section_name, subsection))
    return section


def create_theoretical(section, blocked):
    cpy_template()
    path = 'theoretical'
    aux = ''
    with open('generate_latex/theoretical.tex', 'a') as texfile:

        for (item, subsection) in section:
            aux += '\\section{%s}\n' % item
            for file in subsection:
                if(file in blocked):
                    continue

                name, ext = os.path.splitext(file)
                # name = os.path.split(name)[1]  # Remove Segtree/ prefix
                file_name = " ".join([x.capitalize() for x in name.split("_")])
                file_path = os.path.join(path, item, file).replace('\\','/')

                aux += '\\input{%s}\n' % \
                    (file_path)

        aux += '\n\\end{document}\n'
        texfile.write(aux)

def main():
    section = get_dir()
    blocked = get_blocked()
    create_theoretical(section, blocked)

    cmd = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', ''
           'generate_latex/theoretical.tex']
    with open(os.devnull, 'w') as DEVNULL:
        try:
            subprocess.check_call(cmd, stdout=DEVNULL)
            subprocess.check_call(cmd, stdout=DEVNULL)
        except Exception:
            print("Erro na transformação de LaTex para pdf.")
            print("Execute manualmente para entender o erro:")
            print('pdflatex -interaction=nonstopmode -halt-on-error generate_latex/theoretical.tex')
            remove_aux()
            exit(1)

    remove_aux()
    move_output()

    print("O PDF foi gerado com sucesso!")

if __name__ == '__main__':
    main()