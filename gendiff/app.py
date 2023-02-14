import json
import yaml
from flask import Flask, render_template, request, flash, jsonify
from gendiff.diff_tree import build_diff_tree
from gendiff.formaters.json import format_json
from gendiff.formaters.plain import format_plain
from gendiff.formaters.stylish import format_stylish

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'


def parse_web(data):
    if isinstance(data, dict):
        return data
    elif isinstance(data, str):
        if data.startswith('{'):
            return json.loads(data)
        elif data.startswith('---'):
            return yaml.safe_load(data)
        else:
            raise ValueError('Unknown file format')
    else:
        raise ValueError('Unsupported data type')


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/api/diff", methods=["POST"])
def api_diff():
    old_data = request.json.get("Structure1")
    new_data = request.json.get("Structure2")
    if not old_data or not new_data:
        return jsonify({"error": "Data fields cannot be empty"}), 400
    try:
        old_data_parsed = parse_web(old_data)
        new_data_parsed = parse_web(new_data)
        output_type = request.json.get("outputFormat")
        diff_tree = build_diff_tree(old_data_parsed, new_data_parsed)
        if output_type == 'plain':
            result = format_plain(diff_tree)
        elif output_type == 'json':
            result = format_json(diff_tree)
        else:
            result = format_stylish(diff_tree)
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
