Project Title: AlpenGo - A Data Driven Guide

Team Number: 2
Team Name: AKA
Product Name: AlpenGo
Team Members: Alex Jocius, Katie Sobczak, Andrew Hogan

Weekly Team Meeting: Thursdays at 6pm MDT, 7pm CDT, 8pm EDT

Vision Statement: Encourage hiking through data driven metrics and recommendations.

Motivation: This website will offer a beginner and continued learning experience of frontend, backend, and database design while exploring the alpine wilderness of Colorado.

Risks to Project Completion: 
1.       First time working with development team
2.       First time working in certain languages (HTML / CSS / JavaScript)
3.       Scope of work – 58 14ers in CO
4.       Creative direction uncertainty – we don’t know what we want just yet, overall vision is not complete
Mitigation Strategy for Risks: 
1.       Continuous weekly meetings will provide the opportunity to better understand the teams’ strengths to alleviate inefficiencies.
2.       Continue learning through labs, completing them thoroughly and on time.
3.       Perhaps limit scope to only 10 or so peaks?
4.       Working as we go, ideas will come during the workflow. 

Development Method: Scrum – Leverage agile and scrum methodologies to quickly add product value through weekly and biweekly sprints while balancing desired customer goals.

### Setup
0. (Optional) Recommended to create a virtual environment:

`python -m venv dir_name`
Ex: `python -m venv alpengo`
* Clone the repo into this venv directory, and remember to activate the newly made venv before installing dependencies (next step).

1. Install Dependencies from the included requirements.txt using a CLI:

`pip install -r requirements.txt`
* Caution: You can optionally upgrade the modules within the requirements.txt. But be warned that this may cause errors in dependencies throughout the project.
** `pip install -U -r requirements.txt`
* If error occurs, rollback to initial requirements:
** `pip uninstall -r requirements.txt`
** `pip install -r requirements.txt`
* To capture the current list of packages installed for this project:
** `pip freeze > requirements.txt`

2. Run the included `alpengo_db.py` to initialize a SQLite DB with dummy data

`python alpengo_db.py`
* This will create an `alpengo_db` file within the same directory as the `alpengo_db.py`, ideally within the same directory as the `alpengo_app.py`.

3. To Be Continued...


Project Tracking Software Link: Trello - https://trello.com/w/akaworkspace5
