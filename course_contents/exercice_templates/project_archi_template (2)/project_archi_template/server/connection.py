

import server
import argparse

from server.models.sql_alchemy_model import db

def _parse_user_input():
    """ User input parser function """
    parser = argparse.ArgumentParser(
        description="TODO: Description of your application here"
    )

    parser.add_argument(
        '-d', 
        '--doc', 
        action='store_true', 
        help='generate documentation using pdoc'
    )

    parser.add_argument(
        '-m', 
        '--manual', 
        action='store_true', 
        help='run a script through terminal, use this for debugging purposes'
    )

    return parser.parse_args()


def _generate_doc() -> None:
    """ General purpose function for pdoc documentation generation (HTML) """
    print("Documentation Generated")
    import subprocess 

    process = subprocess.Popen(
        "pdoc --html . --force".split(),
        stdout=subprocess.PIPE
    )
    process.close()


def _run_server() -> None:
    """ Run the flask server instance """
    server.app.run(debug=True)


def _run_bypass_server() -> None:
    """ Custom testing interface without launching flask server instance. """
    raise NotImplementedError


def run() -> None:
    """ General command to launch the server of this project. """
    args = _parse_user_input()

    db.create_all()
    
    if args.doc:
        _generate_doc()
    if args.manual:
        _run_bypass_server()
    else:
       _run_server() 