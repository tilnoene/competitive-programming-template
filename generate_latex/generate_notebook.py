import os
import subprocess
import shutil

def get_item_name(item):
  if item == 'dp':
    return 'DP'
  elif item == 'ds':
    return 'DS'
  
  return item.capitalize()

def cpy_template():
    shutil.copyfile('generate_latex/template_notebook.tex', 'generate_latex/notebook.tex')


def get_blocked():
    blocked = set()
    with open("generate_latex/block_from_notebook.txt") as f:
        for line in f:
            # Remove comments
            line = line.split('#')[0]
            # Normalize filename
            line = line.strip().lower().replace(" ", "_") + ".cpp"
            blocked.add(line)
    return blocked


def remove_aux():
    items = [
        'notebook.aux',
        'notebook.log',
        'notebook.toc',
        'notebook.tex',
        'texput.log',
        'generate_latex/notebook.tex',
    ]
    
    for item in items:
        if os.path.exists(item):
            os.remove(item)

def move_output():
  if os.path.exists('/notebook.pdf'):
    os.remove('/notebook.pdf')

  if os.path.exists('generate_latex/notebook.pdf'):
    shutil.move('generate_latex/notebook.pdf', '/')

def get_dir():
    path = 'code'
    section_list = os.listdir(path)
    section = []
    for section_name in section_list:
        subsection = []
        section_path = os.path.join(path, section_name)
        items = os.listdir(section_path)
        for file_name in items:
            if file_name.endswith('.cpp'):
                subsection.append(file_name)
            elif(os.path.isdir(os.path.join(section_path, file_name))):
                # Sub Directory
                sub_files = os.listdir(os.path.join(section_path, file_name))
                subsection.extend([
                    os.path.join(file_name, name) \
                    for name in sub_files if name.endswith('.cpp')
                ])
        
        section.append((section_name, subsection))
    return section


def create_notebook(section, blocked):
    path = 'code'
    aux = ''
    with open('generate_latex/notebook.tex', 'a') as texfile:

        for (item, subsection) in section:
            aux += '\\section{%s}\n' % get_item_name(item)

            for file in subsection:
                if(file in blocked):
                    continue

                name, ext = os.path.splitext(file)
                name = os.path.split(name)[1]  # Remove Segtree/ prefix
                file_name = " ".join([x.capitalize() for x in name.split("_")])
                file_path = os.path.join(path, item, file).replace("\\","/")
                
                aux += '\\includes{%s}{%s}\n' % \
                    (file_name, file_path)

        aux += '\n\\end{multicols}\n\\end{document}\n'
        texfile.write(aux)

def main():
    cpy_template()
    section = get_dir()
    blocked = get_blocked()
    create_notebook(section, blocked)

    cmd = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
           'generate_latex/notebook.tex']
    with open(os.devnull, 'w') as DEVNULL:
        try:
            subprocess.check_call(cmd, stdout=DEVNULL)
            subprocess.check_call(cmd, stdout=DEVNULL)
        except Exception:
            print("Erro na transformação de LaTex para pdf.")
            print("Execute manualmente para entender o erro:")
            print('pdflatex -interaction=nonstopmode -halt-on-error generate_latex/notebook.tex')
            exit(1)

    remove_aux()
    move_output()

    print("O PDF foi gerado com sucesso!")

if __name__ == '__main__':
    main()
