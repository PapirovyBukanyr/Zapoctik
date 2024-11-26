KATEX_HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.1/katex.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.1/katex.min.css">
    <script>
        function renderMath() {{
            var equation = "{equation}";
            var container = document.getElementById('math-container');
            katex.render(equation, container, {{
                throwOnError: false
            }});
        }}
    </script>
</head>
<body onload="renderMath()">
    <div id="math-container" style="font-size: 24px; text-align: center; margin-top: 20px;"></div>
</body>
</html>
"""
"""
HTML šablona pro zobrazení matematického výrazu pomocí KaTeXu.
"""
