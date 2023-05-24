# TEST STORI

In these files are the test cases using Selenium for test automation.

## Install

To run the tests it is important to have Selenium installed, in the requirements.txt file are the necessary commands.

```
pip install selenium
```
or 
```
pip3 install selenium
```

To generate Reports in HTML format will be necesary also to install pytest, in the requirements.txt file are the necessary commands.

```
pip install pytest
```
or 
```
pip3 install pytest
```

## Run 

To run all the tests you must run the following command:
```
python3 main.py --browser Chrome
```
or
```
python main.py --browser Chrome

Note: You can choose which browser you want to run on, the options are as follows:
- Chrome
- Firefox
- Edge
- Safari

## Running pytest

Go to the "Tests" folder and run 

python -m pytest

If the html report is required run this command instead

python -m pytest --html=report.html

