import numpy as np

# Take only a specific row or column
def calculate_penalty( row_or_col: np.array ):

	sorted_unique = np.unique(row_or_col)
	if len(sorted_unique) > 1:
		return sorted_unique[1] - sorted_unique[0]
	else:
		count = row_or_col.tolist().count(sorted_unique[0])
		return sorted_unique[0] if count == 1 else 0


def calculate_row_and_col_penalty(reduced_processing_matrix):
	for i in range(len(reduced_processing_matrix)-2):
			reduced_processing_matrix[i][-1] = calculate_penalty(reduced_processing_matrix[i][:-2])

	for j in range(len(reduced_processing_matrix[-1])-2):
		reduced_processing_matrix[-1][j] = calculate_penalty(reduced_processing_matrix[:-2, j])

	return reduced_processing_matrix