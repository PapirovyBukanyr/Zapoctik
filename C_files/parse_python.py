import sys
import ast

def parse_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            tree = ast.parse(content)
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as file:
            content = file.read()
            tree = ast.parse(content)

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            print(f"\\section*{{Class: {node.name}}}")
            if ast.get_docstring(node):
                print(f"\\textit{{{ast.get_docstring(node)}}}\n")
            
            for body_item in node.body:
                if isinstance(body_item, ast.FunctionDef):
                    print(f"\\subsection*{{Method: {body_item.name}}}")
                    if ast.get_docstring(body_item):
                        docstring = ast.get_docstring(body_item)
                        print(f"\\textit{{{docstring}}}\n")
                        
                        # Extract Args and Returns from docstring
                        args_section = extract_section(docstring, "Args")
                        returns_section = extract_section(docstring, "Returns")
                        
                        if args_section:
                            print("\\subsubsection*{Args}")
                            print(f"{args_section}\n")
                        
                        if returns_section:
                            print("\\subsubsection*{Returns}")
                            print(f"{returns_section}\n")
                elif isinstance(body_item, ast.Assign):
                    for target in body_item.targets:
                        if isinstance(target, ast.Name):
                            print(f"\\subsubsection*{{Attribute: {target.id}}}")

def extract_section(docstring, section_name):
    lines = docstring.split('\n')
    section_lines = []
    in_section = False
    for line in lines:
        if line.strip().startswith(section_name):
            in_section = True
        elif in_section and line.strip() and not line.startswith(' '):
            break
        elif in_section:
            section_lines.append(line)
    return '\n'.join(section_lines).strip()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_python.py <file_path>")
        sys.exit(1)

    filepath = sys.argv[1]
    parse_file(filepath)
