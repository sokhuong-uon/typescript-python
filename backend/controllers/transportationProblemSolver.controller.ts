import type express from 'express'
import type { UploadedFile } from 'express-fileupload'
import { PythonService } from '../PythonService'

type JSON_OBJECT = {
	[key: string]: any
}

const transportationProblemSolver = ( req: express.Request, res: express.Response ) => {

	if ( !req.files ) return res.send( 'No file uploaded!' )

	const service = new PythonService

	const files = req.files
	const matrixDataFile = files.matrix as UploadedFile

	if ( !matrixDataFile ) return res.send( 'No data provided!' )

	let matrix: number[][]

	try {
		matrix = JSON.parse( matrixDataFile.data.toString() )
	} catch( err ) {
		return res.send( 'Error parsing form data!' )
	}

	const jsonData: JSON_OBJECT = {
		instruction: {
			id: 4,
			data: matrix
		}
	}

	service.processData( jsonData , res )
}

export default transportationProblemSolver