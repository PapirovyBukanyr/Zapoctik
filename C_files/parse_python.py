import sys
import ast
import os

class CommentExtractor(ast.NodeVisitor):
    def __init__(self):
        self.comments = []

    def visit_FunctionDef(self, node):
        if ast.get_docstring(node):
            self.comments.append(ast.get_docstring(node))
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        if ast.get_docstring(node):
            self.comments.append(ast.get_docstring(node))
        self.generic_visit(node)

def extract_comments_from_source(tree):
    extractor = CommentExtractor()
    extractor.visit(tree)
    return extractor.comments

def sanitize_latex(text):
    """Nahradí problematické znaky pro LaTeX."""
    return text.replace('_', '\\_')

def parse_file(filepath, output):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            tree = ast.parse(content)
    except Exception as e:
        print(f"Chyba při čtení souboru {filepath}: {e}")
        return

    rel_path = os.path.relpath(filepath)
    output.write("\\begin{itemize}\n")
    #output.write(f"\\item\\subsection*{{Soubor: {sanitize_latex(rel_path)}}}\n")

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            output.write(f" \\subsection*{{Třída: {sanitize_latex(node.name)}}}\n")
            if ast.get_docstring(node):
                comments = extract_comments_from_source(tree)
                output.write("\\begin{itemize}\n")
                for comment in comments:
                    output.write(f"\\item{{{sanitize_latex(comment)}}}\n")
                output.write("\\end{itemize}\n")
            
            for body_item in node.body:
                if isinstance(body_item, ast.FunctionDef):
                    output.write(f"\\item \\textit{{Metoda: {sanitize_latex(body_item.name)}}}\n")
                    if ast.get_docstring(body_item):
                        output.write(f"\\textit{{{sanitize_latex(ast.get_docstring(body_item))}}}\n")
                elif isinstance(body_item, ast.Assign):
                    for target in body_item.targets:
                        if isinstance(target, ast.Name):
                            output.write(f"\\item \\textit{{Atribut: {sanitize_latex(target.id)}}}\n")

    output.write("\\end{itemize}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Použití: python parse_python.py <soubor> <výstup>")
        sys.exit(1)

    filepath = sys.argv[1]
    output_path = sys.argv[2]

    with open(output_path, 'a', encoding='utf-8') as output:
        parse_file(filepath, output)
