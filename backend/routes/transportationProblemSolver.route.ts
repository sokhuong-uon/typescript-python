import { Router } from 'express'
import transportationProblemSolver from '../controllers/transportationProblemSolver.controller'


const transportationProblemSolverRouter = Router()

transportationProblemSolverRouter.post('/transportation', transportationProblemSolver)

export default transportationProblemSolverRouter