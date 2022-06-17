
# from transportation.solve_transportation_problem import solve_transportation_problem
from services.transportation.solve_transportation_problem import solve_transportation_problem

if __name__ == '__main__':

	print('problem xxxx')
	solve_transportation_problem(
		[
			[ 3, 4, 6, 8, 9, 20 ],
			[ 2, 10, 1, 5, 8, 30 ],
			[ 7, 11, 20, 40, 3, 15 ],
			[ 2, 1, 9, 14, 16, 15 ],
			[ 40, 6, 8, 20, 6, 20 ],
		]
	)
	# print('problem 8. unbalanced')
	# solve_transportation_problem(
	# 	[
	# 		[ 4, 6, 8, 13, 50 ],
	# 		[ 13, 11, 10, 8,70 ],
	# 		[ 14, 4, 10, 13,30 ],
	# 		[ 9, 11, 13, 8, 50 ],
	# 		[ 25, 35, 105, 20, 50 ],
	# 	]
	# )

	# solve_transportation_problem([[12,2,3],[8,4,34]])
	# print('problem 1')
	# solve_transportation_problem(
	# 	[
	# 		[ 4, 1, 2, 4, 4, 60	],
	# 		[ 2, 3, 2, 2, 2, 35	],
	# 		[ 3, 5, 2, 4, 4, 40	],
	# 		[ 22, 45, 20, 18, 30, 135],
	# 	]
	# )
	# print('problem 1.1')
	# solve_transportation_problem(
	# 	[
	# 		[ 4, 1, 2, 4, 4, 30	],
	# 		[ 2, 3, 2, 2, 2, 35	],
	# 		[ 3, 5, 2, 4, 4, 30	],
	# 		[ 8, 9, 1, 4, 16, 20	],
	# 		[ 2, 12, 5, 4, 4, 20	],
	# 		[ 22, 45, 20, 18, 30, 135],
	# 	]
	# )
	# print('problem 2')
	# solve_transportation_problem(
	# 	[
	# 		[6,8,4,14],
	# 		[4,9,8,12],
	# 		[1,2,6,5],
	# 		[6,10,15,31],
	# 	]
	# )
	# print('problem 3')
	# solve_transportation_problem(
	# 	[
	# 		[ 7, 5, 9, 11, 30	],
	# 		[ 4, 3, 8, 6, 25	],
	# 		[ 3, 8, 10, 5, 20	],
	# 		[ 2, 6, 7, 3, 15	],
	# 		[ 30, 30, 20, 10, 90	],
	# 	]
	# )
	# print('problem 4')
	# solve_transportation_problem(
	# 	[
	# 		[ 3, 1, 7, 4, 300	],
	# 		[ 2, 6, 5, 9, 400	],
	# 		[ 8, 3, 3, 2, 500	],
	# 		[ 250, 350, 400, 200, 1200	],
	# 	]
	# )
	# print('problem 5')
	# solve_transportation_problem(
	# 	[
	# 		[ 6, 4, 1, 50 ],
	# 		[ 3, 8, 7, 40 ],
	# 		[ 4, 4, 2, 60 ],
	# 		[ 20, 95, 35, 150	],
	# 	]
	# )
	# print('problem 6. supply > demand')
	# solve_transportation_problem(
	# 	[
	# 		[ 6, 4, 1, 50 ],
	# 		[ 3, 8, 7, 60 ],
	# 		[ 4, 4, 2, 60 ],
	# 		[ 20, 95, 35, 150	],
	# 	]
	# )
	# print('problem 7. supply < demand')
	# solve_transportation_problem(
	# 	[
	# 		[ 8, 4, 1, 50 ],
	# 		[ 3, 2, 7, 20 ],
	# 		[ 4, 1, 2, 60 ],
	# 		[ 20, 95, 35, 150	],
	# 	]
	# )
