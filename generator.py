

from typing import List, TypeVar, Optional, Tuple
import textwrap as tw
import abc

INDENT = '    '

T = TypeVar('T', bound='IContent')

SECTION_OPEN = "\n<section>\n"
SECTION_CLOSE = "\n</section>\n"
HTML_OPEN = """<!doctype html>
<html>"""
HTML_CLOSE = "</html>"
HEAD = """\n<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

    <title>reveal.js</title>

    <link rel="stylesheet" href="dist/reset.css">
    <link rel="stylesheet" href="dist/reveal.css">
    <link rel="stylesheet" href="dist/theme/black.css">

    <style>
        a {
            font-size: 15px;
            margin: auto 0 0 auto;
        }
        li {
            font-size: 30px;
            margin-bottom: 25px;
        }
        .container {
            display: flex;
        }
        .col {
            flex: 1;
        }
    </style>

    <!-- Theme used for syntax highlighted code -->
    <link rel="stylesheet" href="plugin/highlight/monokai.css">
</head>\n"""
BODY_OPEN = """\n<body>
    <div class="reveal">
        <div class="slides">\n"""
BODY_CLOSE = """\n</div>
	</div>
    <script src="dist/reveal.js"></script>
    <script src="plugin/notes/notes.js"></script>
    <script src="plugin/markdown/markdown.js"></script>
    <script src="plugin/highlight/highlight.js"></script>
    <script>
        // More info about initialization & config:
        // - https://revealjs.com/initialization/
        // - https://revealjs.com/config/
        Reveal.initialize({
            hash: true,

            // Learn about plugins: https://revealjs.com/plugins/
            plugins: [ RevealMarkdown, RevealHighlight, RevealNotes ]
        });
    </script>
</body>\n"""

def read_file(path: str) -> str:
    f = open(path, "r")
    c = f.read()
    f.close()
    return c

def write_file(path: str, content: str) -> None:
    f = open(path, "w")
    f.write(content)
    f.close()

class IContent( metaclass=abc.ABCMeta ):
    @abc.abstractproperty
    @property
    def contents(self) -> str:
        pass

    def build(self):
        return "".join(map(lambda x : tw.indent(x, INDENT), [
            SECTION_OPEN,
            self.contents,
            SECTION_CLOSE
        ]))

class HtmlSegment( IContent ):
    """Represents HTML snippet. Part of composite design pattern for revealJS.

    Finds the .html file in question and inserts it into the final target 
    document with the help of the composite design pattern.

    USE:
        >>> HtmlSegment(rel_path + 'filename.html')

    IMPORTANT:
        Do not include the <section> tags in the .html file - they will be 
        wrapped around this element at compile-time.
    """
    
    def __init__(self, path: str):
        super().__init__()
        self._path = path

    @property
    def path(self) -> str:
        return self._path

    @property
    def contents(self) -> str:
        return self.format_html(read_file(self.path))
    
    def format_html(self, content: str) -> str:
        return tw.indent(content, INDENT)

class CodeSegment( IContent ):
    """Represents Python code snippet. Part of composite design pattern.

    Finds the .py file in the contents containing the target Python code to be
    displayed in the course. Title is provided to be put on top of the code, 
    for information. The rule corresponds to the optional value that can be 
    provided - it is used by the revealJS interpreter. 

    USE:
        >>> CodeSegment(rel_path + 'listc.py', "List Comprehension", '1,2|3-4')

    IMPORTANT:
        In the .py snippet file, please LEAVE THE FIRST LINE EMPTY.
    """

    def __init__(self, path: str, title: str, rule: Optional[str] = None):
        super().__init__()
        self._path = path
        self._rule = rule
        self._title = title

    @property
    def path(self) -> str:
        return self._path

    @property
    def rule(self) -> str:
        return self._rule if self._rule else ''

    @property
    def title(self) -> str:
        return self._title
    
    @property
    def contents(self):
        return "\n".join([
            self.format_title(), 
            self.format_code(read_file(self.path))
        ]) 

    def format_title(self) -> str:
        return f"<h3>{self.title}</h3>"

    def format_code(self, code: str) -> str:
        return f"""<pre><code class='language-python' data-trim data-noescape \
                    data-line-numbers='{self.rule}'>
        {tw.indent(code, INDENT)}
        </code></pre>"""

class ContainingSegment( IContent ):
    """Node element in the composite design pattern.

    Basic element of the composite design pattern used for this project. The 
    classes implementing the IContent interface can be held using this class.

    USE:
        >>> tree = ContainingSegment(
        ...     IContent-subclass,
        ...     IContent-subclass,
        ...     IContent-subclass
        ... )
        >>> output_string = tree.compile()
    """

    def __init__(self, *args: T):
        super().__init__()
        self._children = args

    @property
    def children(self) -> Tuple[T, ...]:
        return self._children

    @property
    def contents(self) -> str:
        return "\n".join([c.build() for c in self.children])

    def compile(self) -> str:
        return (
            HTML_OPEN +
            tw.indent(HEAD, INDENT) + 
            tw.indent(BODY_OPEN, INDENT) + 
            tw.indent("\n".join([c.build() for c in self.children]), INDENT) + 
            tw.indent(BODY_CLOSE, INDENT) +  
            HTML_CLOSE
        )

if __name__ == '__main__':
    root = "./course_contents/"
    index_path = './index.html'

    rel_path = root + '0_welcome/'
    welcome_0 = ContainingSegment(
        HtmlSegment(rel_path + 'landing.html'),
        HtmlSegment(rel_path + 'me.html'),
        HtmlSegment(rel_path + 'goals.html'),
        HtmlSegment(rel_path + 'infos.html'),
        HtmlSegment(rel_path + 'letsgo.html'),
    )

    rel_path = root + '1_introduction/'
    introduction_1 = ContainingSegment(
        HtmlSegment(rel_path + 'landing.html'),
        HtmlSegment(rel_path + 'functions.html'),
        HtmlSegment(rel_path + 'interpreted.html'),
        HtmlSegment(rel_path + 'interpreted2.html'),
    )

    interpreter_2 = ContainingSegment(

    )

    rel_path = root + '3_semantics/'
    semantics_3 = ContainingSegment(
        HtmlSegment(rel_path + 'landing.html'),
        CodeSegment(rel_path + 'indentation.py', "En Python, il n'y a pas d'accolades"),
        CodeSegment(rel_path + 'toutobjet1.py', "En Python, tout est un objet"),
        CodeSegment(rel_path + 'toutobjet2.py', "Ce qui rend Python très flexible"),
        HtmlSegment(rel_path + 'toutobjet3.html'),
        CodeSegment(rel_path + 'comments1.py', "Il existe 2 types de commentaires..."),
        CodeSegment(rel_path + 'comments2.py', "exemples", '1-14|16-29'),
        HtmlSegment(rel_path + 'funcmeth1.html'),
        CodeSegment(rel_path + 'funcmeth2.py', "exemples", "1-14|15-27|28-39|40-45|46-57|58-66"),
        HtmlSegment(rel_path + 'variables.html'),
    
    )

    template = ContainingSegment(
        welcome_0,
        introduction_1,
        semantics_3,
    )

    write_file(index_path, template.compile())

    print(template.compile())