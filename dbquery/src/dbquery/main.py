#!/usr/bin/env python
import sys
from dbquery.crew import DbQueryCrew

def run():
    inputs = {'user_question': 'Find people with age greater than 30?'}
    result = DbQueryCrew().crew().kickoff(inputs=inputs)
    
if __name__ == "__main__":
    run()