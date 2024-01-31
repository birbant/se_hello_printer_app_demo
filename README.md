# Simple Flask App

Teaching app displaying name and message in various formats.

- Technologies:
  - Flask
  - Git
  - pytest
  - mockup
  - Flake8
- In the project we use virtual environment to create hermetic environment for the application:

```bash
#we create a virtual environment for application libriaries in Windows OS:
#add Python interpreter

#activating hermetic environment 
venv\Scripts\activate

pip install -r requirements.txt
pip install -r test_requirements.txt
pip list
```
Check: [tutorial venv](https://docs.python.org/3/tutorial/venv.html) and [flask libraries](http://flask.pocoo.org).

- Run the application:
```bash
# as a program from Terminal
python main.py
```
```bash
# from browser or using curl
curl 127.0.0.1:5000/
```
- Run tests (see: http://doc.pytest.org/en/latest/capture.html):

```bash
pytest
pytest --verbose -s
```