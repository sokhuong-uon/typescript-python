import { spawn } from 'child_process'
import type { Response } from 'express'

type Config =  {
	mode: 'json' | 'text',
	scriptPath: string
}

type JSON_OBJECT = {
	[key: string]: any
}
type JSON_RESULT_DATA = {

	stepData: JSON_OBJECT[],
	finalData: JSON_OBJECT,
	result: number
}

export class PythonService {

	private config: Config

	constructor() {

		this.config = {
			mode: 'json',
			scriptPath: './backend/script'
		}

	}

	processData = ( jsonData: JSON_OBJECT, res: Response ) => {

		const jsonString = JSON.stringify( jsonData )

		let processedData: JSON_RESULT_DATA = {
			stepData: [],
			finalData: {},
			result: 0
		}

		const childProcess = spawn( 'python', [ 'main.py', jsonString ], {
			// stdio: "inherit",
			// shell: true,
			cwd: this.config.scriptPath,
			// env: {}
		})

		childProcess.stdout.on( "data", data => {

			console.log( "\x1b[32m", '✅ Output From Python')
			console.log( JSON.parse( data ) )

			try{

				const outputData: {
					result: number,
					step_matrix: number[][][],
					matrix: number[][],
				} = JSON.parse( data )

				processedData.finalData = outputData.matrix
				processedData.stepData = outputData.step_matrix
				processedData.result = outputData.result

				/** Set response */
				res.status( 200 ).json( processedData )

			} catch( err ) {

				console.error(
					"\x1b[31m",
					`Problem processing provided data: \n ${err}`
				)
				res.status( 204 ).json( `problem processing provided data!` )
			}
		})

		childProcess.stderr.on( "data", data => {

			console.error(
				"\x1b[31m",
				`Child process error! \n${data}`
			)

			res.status( 500 ).end()
		})

		childProcess.on( "exit", ( code, signal ) => {

			if ( code === 0 ) {

				console.log(
					"\x1b[32m",
					"🎉 Child process exited with " + `code ${code} and signal ${signal}`
				)
			} else {

				console.error(
					"\x1b[31m",
					"Child process exited with " + `code ${code} and signal ${signal}`
				)
			}

		})

	}

}