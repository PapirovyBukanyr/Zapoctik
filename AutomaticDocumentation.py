import os
import ast
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def extract_classes(file_path):
    """Extract classes, methods, and attributes from a Python file."""
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)
    result = []

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_info = {
                "name": node.name,
                "doc": ast.get_docstring(node),
                "methods": [],
                "attributes": [],
            }
            for body_item in node.body:
                if isinstance(body_item, ast.FunctionDef):
                    method_info = {
                        "name": body_item.name,
                        "doc": ast.get_docstring(body_item),
                    }
                    class_info["methods"].append(method_info)
                elif isinstance(body_item, ast.Assign):
                    for target in body_item.targets:
                        if isinstance(target, ast.Name):
                            class_info["attributes"].append(target.id)
            result.append(class_info)
    return result

def find_python_files(directory):
    """Recursively find all Python files in a directory."""
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files

def generate_pdf(output_path, data):
    """Generate a formatted PDF from extracted class information."""
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    y_position = height - 50

    # Set up styles
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    subtitle_style = styles["Heading2"]
    body_style = styles["BodyText"]

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y_position, "Python Class Documentation")
    y_position -= 30

    for file_data in data:
        file_name = file_data["file"]
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(colors.blue)
        c.drawString(50, y_position, f"File: {file_name}")
        y_position -= 20

        for cls in file_data["classes"]:
            # Class name
            c.setFont("Helvetica-Bold", 12)
            c.setFillColor(colors.black)
            c.drawString(60, y_position, f"Class: {cls['name']}")
            y_position -= 20

            # Class docstring
            if cls["doc"]:
                c.setFont("Helvetica", 10)
                c.setFillColor(colors.gray)
                c.drawString(70, y_position, f"Description: {cls['doc']}")
                y_position -= 20

            # Attributes
            if cls["attributes"]:
                c.setFont("Helvetica", 10)
                c.setFillColor(colors.black)
                c.drawString(70, y_position, "Attributes:")
                y_position -= 15
                for attr in cls["attributes"]:
                    c.drawString(80, y_position, f"- {attr}")
                    y_position -= 15

            # Methods
            if cls["methods"]:
                c.setFont("Helvetica", 10)
                c.setFillColor(colors.black)
                c.drawString(70, y_position, "Methods:")
                y_position -= 15
                for method in cls["methods"]:
                    c.drawString(80, y_position, f"- {method['name']}")
                    if method["doc"]:
                        c.setFont("Helvetica", 9)
                        c.setFillColor(colors.gray)
                        c.drawString(90, y_position - 10, f"Description: {method['doc']}")
                        y_position -= 20
                    else:
                        y_position -= 15

            y_position -= 10  # Space between classes

        y_position -= 20  # Space between files
        if y_position < 100:  # Check for page overflow
            c.showPage()
            y_position = height - 50

    c.save()

def main(directory, output_path):
    """Main function to parse directory and generate PDF."""
    python_files = find_python_files(directory)
    all_data = []

    for file_path in python_files:
        classes = extract_classes(file_path)
        if classes:
            all_data.append({"file": os.path.basename(file_path), "classes": classes})

    if all_data:
        generate_pdf(output_path, all_data)
        print(f"PDF generated: {output_path}")
    else:
        print("No classes found in the specified directory.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate documentation from Python files.")
    parser.add_argument("directory", help="Directory containing Python files.")
    parser.add_argument(
        "output", help="Path to the output PDF file (e.g., output.pdf)."
    )
    args = parser.parse_args()

    main(args.directory, args.output)
