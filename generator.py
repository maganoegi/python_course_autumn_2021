

from typing import List, TypeVar, Optional, Tuple
import textwrap as tw
import abc

INDENT = '    '

T = TypeVar('T', bound='IContent')

ROOT = "./course_contents/"

SECTION_OPEN = "\n<section>\n"
SECTION_CLOSE = "\n</section>\n"
HTML_OPEN = """<!doctype html>
<html>"""
HTML_CLOSE = "</html>"
HEAD = """\n<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

    <title>Python Course</title>

    <link rel="stylesheet" href="dist/reset.css">
    <link rel="stylesheet" href="dist/reveal.css">
    <link rel="stylesheet" href="dist/theme/black.css">

    <style>
        a {
            font-size: 15px;
            margin: auto 0 0 auto;
        }
        li {
            font-size: 20px;
            margin-bottom: 20px;
        }
        .container {
            display: flex;
        }
        .col {
            flex: 1;
        }

        .column-list {
            columns: 100px;
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
            parallaxBackgroundImage: 'https://background-tiles.com/overview/black/patterns/large/1035.png',
            parallaxBackgroundSize: '300px 300px',
            parallaxBackgroundHorizontal: 200,
            parallaxBackgroundVertical: 50,

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

    @property
    def path(self) -> str:
        return self._path

    def build(self, path: str):
        return "".join(map(lambda x : tw.indent(x, INDENT), [
            SECTION_OPEN,
            self.contents(path),
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

    def contents(self, ch_path) -> str:
        return self.format_html(read_file(ch_path + self.path))
    
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
    def rule(self) -> str:
        return self._rule if self._rule else ''

    @property
    def title(self) -> str:
        return self._title
    
    def contents(self, ch_path: str):
        return "\n".join([
            self.format_title(), 
            self.format_code(read_file(ch_path + self.path))
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
        ...     IContent-subclass,
        ...     chapter_path="./path_to_chapter/"
        ... )
        >>> output_string = tree.compile()
    """

    def __init__(self, *args: T, chapter_path: str = ""):
        super().__init__()
        self._children = args
        self._path = ROOT + chapter_path

    @property
    def children(self) -> Tuple[T, ...]:
        return self._children

    def contents(self, ch_path: str) -> str:
        return "\n".join([c.build(self.path) for c in self.children])

    def compile(self) -> str:
        return HTML_OPEN + "".join(map(lambda x : tw.indent(x, INDENT), [
            HEAD,
            BODY_OPEN,
            "\n".join([
                c.build(self.path) for c in self.children
            ]),
            BODY_CLOSE
        ])) + HTML_CLOSE

if __name__ == '__main__':
    root = "./course_contents/"
    index_path = './index.html'

    welcome_0 = ContainingSegment(
        HtmlSegment('landing.html'),
        HtmlSegment('me.html'),
        HtmlSegment('goals.html'),
        HtmlSegment('infos.html'),
        HtmlSegment('letsgo.html'),
        chapter_path='0_welcome/',
    )

    introduction_1 = ContainingSegment(
        HtmlSegment('landing.html'),
        HtmlSegment('functions.html'),
        HtmlSegment('interpreted.html'),
        HtmlSegment('interpreted2.html'),
        chapter_path='1_introduction/'
    )

    environments_2 = ContainingSegment(
        HtmlSegment('landing.html'),
        HtmlSegment('idevstext.html'),
        HtmlSegment('idetextexamples.html'),
        HtmlSegment('cecours.html'),
        HtmlSegment('condasetup1.html'),
        HtmlSegment('projectsetup1.html'),
        HtmlSegment('projectsetup2.html'),
        chapter_path='2_environments/'
    )

    semantics_3 = ContainingSegment(
        HtmlSegment('landing.html'),
        CodeSegment('indentation.py', "En Python, il n'y a pas d'accolades"),
        CodeSegment('toutobjet1.py', "En Python, tout est un objet"),
        CodeSegment('toutobjet2.py', "Ce qui rend Python tres flexible"),
        HtmlSegment('toutobjet3.html'),
        HtmlSegment('toutobjet4.html'),
        CodeSegment('comments1.py', "Il existe 2 types de commentaires..."),
        CodeSegment('comments2.py', "exemples", '1-14|16-29'),
        HtmlSegment('funcmeth1.html'),
        CodeSegment('funcmeth2.py', "exemples", "4-18|24-36|42-53|60-65|76-86|98-106"),
        HtmlSegment('variables.html'),
        HtmlSegment('dynamictyping.html'),
        HtmlSegment('mutable.html'),
        HtmlSegment('dynamictyping2.html'),
        HtmlSegment('ducktyping.html'),
        CodeSegment('ducktypingexample1.py', "exemple conceptuel", '1-14|15-18|20-34'),
        HtmlSegment('strictlazy.html'),
        CodeSegment('strictlazyexample.py', "strict vs lazy evaluation", '1-3|4-12'),
        chapter_path='3_semantics/'
    )

    lang_structure_4 = ContainingSegment(
        HtmlSegment('landing.html'),
        HtmlSegment('builtinnumerical.html'),
        CodeSegment('casting.py', "conversion de type - Casting", '1-16|31-38'),
        CodeSegment('string.py', "type string", '1-3|5-7|9-11|13-18|20-28|30-40'),
        CodeSegment('bool.py', "boolean et operateurs", '1-11|13-23'),
        HtmlSegment('lists.html'),
        CodeSegment('listexamples.py', 'Listes - base', '1-2|4-6|8-14|18-23|27-29|32-47'),
        CodeSegment('listadvanced.py', 'Listes - avance', '1-11|13-18|20-30|32-38|40-43|45-46|48-52|54-65'), # TODO
        CodeSegment('flux.py', "Flux d'execution", '1-13|15-22|26-30|34-47|51-65|67-70 '),
        CodeSegment('calculator.py', "exemple - calculatrice", '44|45-47|1-11'),
        CodeSegment('ternary.py', "Expression ternaire"),

        chapter_path="4_langstructure/"
    )

    advanced_structure_5 = ContainingSegment(
        HtmlSegment("landing.html"),
        CodeSegment("tuples.py", "Tuples", "1-8|10-21|23-35|37-43"),
        CodeSegment("dictionaries.py", "Dictionnaires", "1-11|13-18|20-30|32-38|40-51|53-61"),
        CodeSegment("iterators.py", "Iterateurs", "1-14|20-27|29-40|42-54"),
        CodeSegment("generators.py", "Generators", "1-12|9-22|26-36|38-50"),
        CodeSegment("sets.py", "Set & Set Theory"),

        chapter_path="5_advancedstruct/"
    )

    modules_6 = ContainingSegment(
        HtmlSegment("landing.html"),
        HtmlSegment("whatismodule.html"),
        CodeSegment("modulexample.py", "Modules", "1-5|7-19|22-30|32-38|40-42"),
        HtmlSegment("whatispackage.html"),
        HtmlSegment("howtomakepackage.html"),
        CodeSegment("importpackage.py", "Comment utiliser packages", "1-7|9-22|24-30"),

        chapter_path="6_modules/"
    )

    oop_7 = ContainingSegment(
        HtmlSegment("landing.html"),
        HtmlSegment("definitions.html"),
        CodeSegment("example1.py", "Exemple pour commencer", "1-11|13-20|22-25|26-37|39-52|54-56|58-71|73-80"),
        HtmlSegment("pillars.html"),
        HtmlSegment("inheritance.html"),
        CodeSegment("inheritance_examples.py", "Types de Generalisation", "1-8|10-22|24-29|31-34"),

        chapter_path="7_oop/"
    )

    template = ContainingSegment(
        welcome_0,
        introduction_1,
        environments_2,
        semantics_3,
        lang_structure_4,
        advanced_structure_5,
        modules_6,
        oop_7
    )

    write_file(index_path, template.compile())

    print(template.compile())