from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from __init__ import create_app

"""
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
"""
app = create_app()


if __name__ == "__main__":
    app.run(port=5003)
