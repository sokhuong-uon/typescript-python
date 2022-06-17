import express from 'express'
import expressFileUpload from 'express-fileupload'
import transportationProblemSolverRouter from './routes/transportationProblemSolver.route'

const app = express()
/**
 * Middlewares
 */
// @ts-ignore
app.use( expressFileUpload() )

/**
 * Routers
 */
app.use( transportationProblemSolverRouter )


/* Export the server middleware */
module.exports = {

	path: '/solver',
	handler: app

}
