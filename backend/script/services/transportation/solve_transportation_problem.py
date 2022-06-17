import numpy as np

from services.transportation.make_balance import make_balance
from services.transportation.calculate_row_and_col_penalty import calculate_row_and_col_penalty
from services.transportation.min_row_max_col import min_row_max_col
from services.transportation.reduce_matrix import reduce_matrix


def solve_transportation_problem( data: list[list[int]] ):
	IBFS = np.array([0])
	allocation_steps = []
	step_matrix = []

	original_np_data = np.array( data )

	# original_cost_np_data = np.delete(data,-1, 1)
	# original_cost_np_data = np.delete(original_cost_np_data, -1, 0)

	processing_np_matrix = original_np_data.copy()
	processing_np_matrix =  make_balance(processing_np_matrix)
	# print(processing_np_matrix)
	processing_np_matrix = np.vstack([processing_np_matrix, [None for _ in range(len(processing_np_matrix[0]))]])
	processing_np_matrix = np.hstack([processing_np_matrix, [[None] for _ in range(len(processing_np_matrix))]])

	reduced_processing_matrix = processing_np_matrix
	# print(reduced_processing_matrix)
	while (len(reduced_processing_matrix) > 2) or (len(reduced_processing_matrix[0]) > 2) :

		# print('Loop ######################################### Loop')
		reduced_processing_matrix = calculate_row_and_col_penalty(reduced_processing_matrix)

		# print(reduced_processing_matrix)
		allocation_indices = min_row_max_col(reduced_processing_matrix)
		# print(allocation_indices)
		step_matrix.append(reduced_processing_matrix.tolist())
		reduced_processing_matrix = reduce_matrix(IBFS,reduced_processing_matrix, allocation_indices)


	# print(reduced_processing_matrix)
	# print(IBFS.item())
	# step_matrix.append(reduced_processing_matrix.tolist())

	result = reduced_processing_matrix
	return { "step_matrix": step_matrix ,"result": IBFS.item(), "matrix": result.tolist() }