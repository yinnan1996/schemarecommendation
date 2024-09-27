import copy
import json
import xlrd

from flask import Flask, jsonify, request
from flask_cors import CORS

import tree_edit_distance, cosine_similarity

app = Flask(__name__)
CORS(app)

# the example data store in the Excel, Open and read data from it
wb = xlrd.open_workbook(r"schema_dataset.xlsx")
sheet = wb.sheet_by_index(0)
contents = sheet.col_values(3)
ids = sheet.col_values(0)

# Data structures to store the contents and their corresponding IDs
all_data = {}
index = {}
ord_map = {}

# Iterate through the rows of the Excel sheet
for i in range(1, len(contents)):
    content = contents[i]
    id = ids[i]
    try:
    # Parse the content as JSON and store it in a dictionary
        content_dict = json.loads(content)
        all_data[id] = content_dict
        ord = content_dict['_ord']
        ord_map[id] = set(ord)
    except Exception:
        print(id)

@app.route('/api/example', methods=['POST'])
def api_example():
    """
    Calculate similarity between input data and data from an Excel sheet.

    This endpoint receives JSON data, calculates the similarity with the data stored
    in an Excel sheet using cosine similarity and tree edit distance, and returns
    the top N similar items.
    """
    input_data = request.get_json()
    input_ord = input_data["_ord"]

    input_ord_set = set(input_ord)
    # Initialize a dictionary to store data that matches the input order
    index_find_data = {}
    for id, _ in ord_map.items():
        if len(input_ord_set.intersection(ord_map[id])) / len(input_ord_set) >= 0.6:
            index_find_data[id] = all_data[id]

    # Dictionary to store similarity scores
    sim_map = {}
    for k, ifd in index_find_data.items():
        # Calculate the cosine similarity and tree edit distance
        cosine_sim = cosine_similarity.similarity(input_data, ifd)
        tree_sim = tree_edit_distance.similarity(input_data, ifd)
        sim = 0.5 * cosine_sim + 0.5 * tree_sim
        sim_map[k] = sim

    # Sort the data by similarity score in descending order
    sorted_sim = sorted(sim_map.items(), key=lambda x: x[1], reverse=True)
    
    # Select the top N elements based on similarity
    n = 10
    top_n = [item[0] for item in sorted_sim[:n]]

    # Prepare the response data
    res = []
    for id in top_n:
        content = copy.deepcopy(index_find_data[id])
        content_ord = content["_ord"]
        for io in input_ord:
            if io in content_ord:
                content_ord.remove(io)
                content.pop(io)
        content["_ord"] = content_ord
        res.append(content)

    res_ord = []
    res2 = []
    for content in res:
        content_ord = content["_ord"]
        for co in content_ord:
            if co not in res_ord:
                res2.append({
                    "_ord": [co],
                    co: content[co]
                })
                res_ord.append(co)
    res2 = res2[:3]

    # Return the response as JSON
    return jsonify(res2)


if __name__ == '__main__':
    """
    Run the Flask application if this script is executed as the main program.
    """
    app.run(debug=True, host="127.0.0.1", port=5000)
    # python api.py
    # http://127.0.0.1:5000/api/example