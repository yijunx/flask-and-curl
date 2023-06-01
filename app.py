from flask import Flask, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os
import tempfile
import time
from flask_pydantic import validate
from pydantic import BaseModel


app = Flask(__name__)





def save_files(files_dict: dict[str, FileStorage], folder_path: str) -> dict:
    filepath_dict = {}  # key -> filepath
    for key, value in files_dict.items():
        filename = secure_filename(value.filename)  # sanitize filename
        filepath = os.path.join(folder_path, filename)
        value.save(filepath)
        filepath_dict[key] = filepath
    return filepath_dict


class GetQuery(BaseModel):
    name: str
    age: int


@app.route('/endpoint_to_get', methods=['GET'])
@validate()
def get_endpoint(query: GetQuery):
    # if there are 2 name in the path
    print(request.args)  # ImmutableMultiDict has 2 names
    print(request.args.get("name"))  # only gets first name!!!
    print(query)  # also only gets first name
    return {"the-args": request.args}


@app.route('/endpoint_to_post_json', methods=['POST'])
def post_endpoint_for_json():
    print(request.json)
    return {"the-json": request.json}

@app.route('/endpoint_to_post_data_and_files', methods=['POST'])
def post_endpoint_for_data_and_form():
    print(request.form)
    print(request.files)
    # print(request.files)
    tempdirpath = tempfile.TemporaryDirectory(
        suffix=str(time.time())
    )  # use timestamp to avoid conflicting file
    filepath_dict = save_files(request.files, tempdirpath.name)
    for key, value in filepath_dict.items():
        with open(value, "rb") as f:
            print(f"HERE WE ARE READING THE FILE {key}")
            print(f.read())

    return {"the-form": request.form, "the-files": filepath_dict}


if __name__ == '__main__':
    app.run(debug=True, port=5000)
    

