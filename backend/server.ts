import express, { Router } from 'express'
import { Options, PythonShell } from 'python-shell'

const app = express()

app.get('/', ( req, res ) => {

	const message: any[] = []

	// PythonShell.runString('x=1+1;print(x)', undefined, ( err ) => {

	// 	if (err) throw err
	// 	console.log('finished')
	// })

	let options: Options = {
		mode: 'text',
		// pythonPath: 'path/to/python',
		pythonOptions: ['-u'], // get print results in real-time
		scriptPath: `${__dirname}/../assets/python/`,
		args: ['1', '2', '3']
	}
	PythonShell.run( 'echo.py', options, ( err , results ) => {
		if (err) throw err
		/* The results is an array consisting of message during execution */
		console.log('%j', results )

		if ( results ) {

			for ( const value of results ) {
				// console.log( typeof Number( value ) )
				message.push( Number( value ))

			}

			// console.log( typeof results)


			res.json( { results: message} )
		}

	})


})


/* Export the server middleware */
module.exports = {

	path: '/api',
	handler: app

}
