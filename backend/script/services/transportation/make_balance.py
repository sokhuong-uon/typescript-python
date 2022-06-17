import numpy as np

# Take a processing_np_matrix
def make_balance( matrix ):

	supply = matrix[:-1,-1]
	demand = matrix[-1,:-1]
	# print(demand, supply)

	total_supply = sum(supply)
	total_demand = sum(demand)
	if total_supply > total_demand:
		dummpy_col = [[0] for _ in range(len(matrix)-1)]
		dummpy_col.append([total_supply - total_demand])

		new_matrix = matrix[:,:-1]
		last_col = matrix[:,-1]
		last_col = last_col[:, np.newaxis]

		matrix = np.hstack([new_matrix, dummpy_col, last_col])


	if total_supply < total_demand:
		dummpy_row = [0 for _ in range(len(matrix[0])-1)]
		dummpy_row.append(total_demand - total_supply)

		new_matrix = matrix[:-1]
		last_row = matrix[-1]
		# print(dummpy_row)
		matrix = np.vstack([new_matrix, dummpy_row, last_row])
		# print(matrix)

	matrix[-1, -1] = max( total_demand, total_supply )
	# print(matrix)
	return matrix