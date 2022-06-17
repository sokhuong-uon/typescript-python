import numpy as np

# Take the entire reduced_processing_matrix
def min_row_max_col( matrix: np.array ):

	row_penelty = matrix[:-2, -1]
	col_penelty = matrix[-1, :-2]

	min_row = np.where(row_penelty == np.amin(row_penelty))
	max_col = np.where(col_penelty == np.amax(col_penelty))

	# print( min_row[0], max_col[0])

	min_cost_for_allocation = float(np.inf)
	index_of_min_cost_for_allocation: dict = None

	for i in min_row[0]:

		for j in max_col[0]:

			if matrix[i,j] < min_cost_for_allocation:

				min_cost_for_allocation = matrix[i,j]
				index_of_min_cost_for_allocation = {'row':i,'col':j}

	return index_of_min_cost_for_allocation