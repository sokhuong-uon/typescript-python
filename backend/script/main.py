import sys, json
from enum import Enum
from typing import Dict
from services import data_processing

class Instruction( Enum ):
	SUM_LIST = 1
	FIND_MAX = 2
	SOLVE_LINEAR = 3
	SOLVE_TRANSPORTATION_PROBLEM = 4


def process_task( instruction ):

	if instruction['id'] <= 0:
		return None

	if instruction['id'] == Instruction.SUM_LIST.value:
		return data_processing.sum_list( instruction['data'] )

	if instruction['id'] == Instruction.FIND_MAX.value:
		return data_processing.find_max( instruction['data'] )

	if instruction['id'] == Instruction.SOLVE_LINEAR.value:
		return data_processing.solve_linear( instruction['data'] )

	if instruction['id'] == Instruction.SOLVE_TRANSPORTATION_PROBLEM.value:
		return data_processing.solve_transportation_problem( instruction['data'] )


def main():

	# the final data that will be sent to nodejs.
	final_data: dict = {}

	# Take input
	json_string = sys.argv[1:][0]
	# print( json_string)

	json_data: dict = json.loads( json_string )

	if json_data["instruction"]:
		processed = process_task( json_data["instruction"])
	else:
		processed = None

	# Setup final data dictionary
	final_data["result"] = processed["result"]
	final_data["matrix"] = processed["matrix"]
	final_data["step_matrix"] = processed["step_matrix"]
	final_data["final"] = True
	# final_data["email"] = "sokhuong.usk@gmail.com"

	# send final data to nodejs through stdout
	print( json.dumps(final_data) )


if __name__ == '__main__':
	main()