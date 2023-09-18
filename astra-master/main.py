import json
import markdown
import os

from flask import Flask

from src.parser import Parser

app = Flask(__name__)
parser = Parser("raw_data/export_full.xml")


@app.route("/")
def index():
    """ route to index page for doc display. """
    with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as md:
        content = md.read()
        return markdown.markdown(content)


@app.route('/all')
def all_items():
    """ route to show all items."""
    response_data = json.dumps(list(parser.all_items), ensure_ascii=False)
    return response_data


@app.route('/spare')
def items_with_spare_parts():
    """ route to show spare parts items."""
    response_data = json.dumps(list(parser.items_with_spare_parts), ensure_ascii=False)
    return response_data


@app.route('/count')
def count():
    """ route to show count."""
    return str(parser.count)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
