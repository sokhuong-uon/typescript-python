
from ortools.linear_solver import pywraplp


def solve_linear( data: list[int] ):

	# Create the linear solver with the GLOP backend.
	solver = pywraplp.Solver.CreateSolver('GLOP')

	# Create the variables x and y.
	x1 = solver.NumVar(0, float('inf'), 'x1')
	x2 = solver.NumVar(0, float('inf'), 'x2')
	# x2 = solver.NumVar(0, 2, 'x2')

	# print('Number of variables =', solver.NumVariables())

	# Create a linear constraint, 0 <= x + y <= 2.
	#...
	ct1 = solver.Constraint(0, 12, 'ct1')
	ct1.SetCoefficient(x1, 1)
	ct1.SetCoefficient(x2, 3)

	ct2 = solver.Constraint(13, float('inf'), 'ct2')
	ct2.SetCoefficient(x1, 3)
	ct2.SetCoefficient(x2, 1)

	ct3 = solver.Constraint(0, 3, 'ct3')
	ct3.SetCoefficient(x1, 1)
	ct3.SetCoefficient(x2, -1)

	# print('Number of constraints =', solver.NumConstraints())

	# Create the objective function, 3 * x + y.
	# 4X1 + 10X2
	objective = solver.Objective()
	objective.SetCoefficient(x1, 2)
	objective.SetCoefficient(x2, 2)
	# objective.SetMaximization()
	objective.SetMinimization()

	solver.Solve()

	# print('Solution:')
	# print('Objective value =', objective.Value())
	# print('x =', x.solution_value())
	# print('y =', y.solution_value())

	return { 'x': x1.solution_value(), 'x2': x2.solution_value(), 'z': objective.Value() }