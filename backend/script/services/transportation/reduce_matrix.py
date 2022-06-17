import numpy as np


# Take a reduced matrix
def correct_new_supply_demand(matrix):
	matrix[-2, -2] = np.sum(matrix[:-2, -2])
	return matrix

def reduce_matrix(IBFS, matrix, allocation_indices ):

	supply = matrix[allocation_indices['row'], -2]
	demand = matrix[-2, allocation_indices['col']]

	allocation_value = min( supply, demand)


	if supply == demand :
		new_matrix = np.delete(matrix, allocation_indices['row'], 0)
		new_matrix = np.delete(new_matrix, allocation_indices['col'], 1)
	else:

		# If Supply < Demand
		if supply < demand:
			# print('delete row')
			matrix[ -2, allocation_indices['col']] -= allocation_value
			new_matrix = np.delete(matrix, allocation_indices['row'], 0)
			new_matrix = correct_new_supply_demand(new_matrix)

		# If Supply > Demand
		if supply > demand:
			# print('delete column')
			matrix[allocation_indices['row'], -2] -= allocation_value
			new_matrix = np.delete(matrix, allocation_indices['col'], 1)
			new_matrix = correct_new_supply_demand(new_matrix)

	# print(new_matrix)
	# print(allocation_steps_matrix)
	IBFS[0] += matrix[allocation_indices['row'], allocation_indices['col']] * allocation_value
	# print(IBFS[0])

	return new_matrix