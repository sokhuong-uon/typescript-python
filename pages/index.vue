<template>
	<div class="w-screen h-screen flex flex-col bg-gray-900 overflow-hidden">
		<div class="w-full h-full flex flex-col overflow-y-auto">
			<form id="transportation-problem-form" action="" method="post" enctype="multipart/form-data" class="w-full h-full flex flex-col">
				<div class="w-full h-16 flex items-center justify-center text-gray-200 text-3xl">
					Transportation Problem Solver
				</div>

				<div class=" w-full flex flex-col items-center justify-center rounded-md">

					<div class="w-full h-16 flex items-center justify-start pl-56">
						<label for="number-of-destination" class="text-gray-500 text-2xl px-3">{{numberOfDestination}} </label>
						<input type="range" max="9" min="2" v-model="numberOfDestination" name="number-of-destination" id="number-of-destination" class="w-64 focus:outline-none">
					</div>

					<div class="w-full flex pl-32 items-center justify-start relative">

						<div class="flex flex-col items-center w-16 h-64 absolute top-6">
							<label for="number-of-source" class="w-full h-5 py-5 flex items-center justify-center text-gray-500 text-2xl">{{numberOfSource}}</label>
							<div class="w-full h-5/6 flex flex-col items-center justify-center relative">
								<input type="range" max="9" min="2" v-model="numberOfSource" name="number-of-source" id="number-of-source" class="vertical-range w-56 h-16 focus:outline-none">
							</div>
						</div>

						<table class="table-fix w-auto ml-24 mt-8 p-3 rounded-lg bg-black text-gray-400 select-none">
							<thead class="p-2 text-gray-600">
								<tr>
									<th class="table-cel">S\D</th>
									<th v-for="(destination, i) of transportationCost[0]" :key="i" class="table-cel">
										<span v-if="i===transportationCost[0].length-1">Supply</span>
										<span v-else>D<sub>{{i+1}}</sub></span>
									</th>
								</tr>
							</thead>
							<tbody>
								<tr v-for="(source, i) of transportationCost" :key="i">
									<td class="table-cel text-gray-600 font-bold">
										<span v-if="i===transportationCost.length-1">Demand</span>
										<span v-else>S<sub>{{i+1}}</sub></span>
									</td>
									<td v-for="(cost, j) of source" :key="j" class="table-cel">

										<div v-if="(i===transportationCost.length-1)&&(j===source.length-1)" class="w-11/12 h-5/6 flex items-center justify-center rounded-md text-center text-3xl bg-gray-900">
											{{isBalancedTransportationProblem? `😊` : `🤯`}}
										</div>

										<!-- <input v-if="(i===transportationCost.length-1)&&(j===source.length-1)" min="1" max="10000" disabled="true" class="w-11/12 h-5/6 rounded-md text-center bg-gray-900 focus:outline-none" type="number" :name="`input-${i}${j}`" :id="`cell-${i}${j}`"> -->
										<input v-else min="0" max="10000" v-model.number="transportationCost[i][j]" class="w-11/12 h-5/6 rounded-md text-center bg-gray-900 focus:outline-none" type="number" :name="`input-${i}${j}`" :id="`cell-${i}${j}`">

									</td>
								</tr>

							</tbody>
						</table>
					</div>

				</div>

				<div class="w-full h-16 pl-12 flex items-center justify-start">
					<button id="submit-button" type="submit" class="w-14 h-10 text-xl text-gray-300 rounded-md bg-green-700 focus:outline-none ring-pink-600 focus:ring-2">Solve</button>
					<div class="flex h-full ml-36 items-center justify-center text-gray-300 text-xl">
						Initial Basic Feasable Solution: <span class="text-2xl ml-1 text-green-500"> {{IBFS}}</span>
						</div>
				</div>
			</form>

			<!-- Result part -->
			<div class="w-full h-96 flex-shrink-0 relative">
				<!-- <div class="w-48 h-24 absolute top-0 left-0 z-50">
					<button @click="PreviousStep" :class="{'bg-red-700':stepIndex==0, 'bg-green-700':stepIndex!=0}" class="w-16 h-12 rounded-md focus:outline-none">Pre</button>
					<button @click="NextStep" :class="{'bg-red-700':stepIndex==stepData.length-1, 'bg-green-700':stepIndex!=stepData.length-1}" class="w-16 h-12 rounded-md focus:outline-none">Next</button>
				</div> -->
				<div v-if="stepData[stepIndex]" class="w-full flex flex-col pl-32 items-end justify-start relative">

					<table  v-for="(steps, index) of stepData" :key="index" class="table-fix w-auto mr-64 mt-8 p-3 rounded-lg bg-black text-gray-400 select-none">
						<thead class="p-2 text-gray-600">
							<tr>
								<th class="table-cel">S\D</th>
								<th v-for="(col, i) of stepData[index][0]" :key="i" class="table-cel">
									<span v-if="i===stepData[index][0].length-2">Supply</span>
									<span v-else-if="i===stepData[index][0].length-1">P<sub>row</sub></span>
									<!-- <span v-else>D<sub>{{i+1}}</sub></span> -->
								</th>
							</tr>
						</thead>
						<tbody>
							<tr v-for="(row, i) of stepData[index]" :key="i">

								<td class="table-cel text-gray-600 font-bold">
									<span v-if="i===stepData[index].length-2">Demand</span>
									<span v-else-if="i===stepData[index].length-1">P<sub>col</sub></span>
									<!-- <span v-else>S<sub>{{i+1}}</sub></span> -->
								</td>

								<td v-for="(cost, j) of row" :key="j" class="table-cel">

									<!-- <div v-if="(i>=fistStep.length-2)&&(j>=row.length-2)" class="w-11/12 h-5/6 flex items-center justify-center rounded-md text-center text-3xl bg-gray-900">
										😊
									</div> -->

									<div class="w-11/12 h-5/6 rounded-md text-center flex items-center justify-center bg-gray-900 focus:outline-none" type="number" :name="`element-${i}${j}`" :id="`cell-${i}${j}`"><span>{{cost}}</span></div>

								</td>

							</tr>

						</tbody>
					</table>

				</div>
			</div>

		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref, useContext, watch } from '@nuxtjs/composition-api'
import { eww_css } from '@/assets/constant'
export default defineComponent({

	setup() {

		const context = useContext()

		const numberOfSource = ref(2)
		const numberOfDestination = ref(3)
		const isBalancedTransportationProblem = ref(false)
		const transportationCost = ref<number[][]>([])
		const totalDemand = ref(0)
		const totalSupply = ref(0)

		const checkBalance = ref( ( costs: number[][]) => {

			totalSupply.value = 0

			costs.forEach( ( cost, i ) => {
				if( i=== costs.length-1) return
				totalSupply.value += cost[cost.length-1]
			})

			/**
			 * ! Fuck!
			 * * Fuck! why the fuck JS if so fuck!
			 * TODO: JAVA SCRIPT Syntax should has to be better 🤯
			 */
			totalDemand.value = costs[costs.length-1].reduce((x,y)=> x+y) - costs[costs.length-1][costs[costs.length-1].length-1]

			isBalancedTransportationProblem.value =  totalSupply.value == totalDemand.value ? true : false

		})

		const resampleCosts = ref(()=>{

			transportationCost.value = []

			for( let i = 0; i<= numberOfSource.value; i++ ) {

				let source:number[] = []

				for ( let j = 0; j <= numberOfDestination.value; j++ ) {

					source.push( Math.round(Math.random()*10 + 1))
				}

				transportationCost.value.push( source )
			}

			checkBalance.value(transportationCost.value)

		})
		resampleCosts.value()

		const stepData = ref<number[][][]>([])
		const fistStep = ref<number[][]>([])
		const stepIndex = ref(0)
		const IBFS = ref()

		const PreviousStep = ref( ()=>{
			if(stepIndex.value > 0) stepIndex.value -= 1
		})

		const NextStep = ref( ()=> {
			if(stepIndex.value < stepData.value.length -1) stepIndex.value += 1
		})

		watch( numberOfSource, (oldValue, newValue) => {

			resampleCosts.value()

		})

		watch( numberOfDestination, (oldValue, newValue) => {

			resampleCosts.value()

		})

		watch( transportationCost, (oldValue, newValue) => {

			checkBalance.value(transportationCost.value)
			// console.table(transportationCost.value)

		})

		onMounted( () => {

			const transportationProblemForm = document.getElementById('transportation-problem-form')! as HTMLFormElement
			transportationProblemForm.addEventListener('submit', ( event: Event) => {

				event.preventDefault()
				transportationCost.value[numberOfSource.value][numberOfDestination.value] = totalDemand.value
				// console.table(transportationCost.value)

				//#region prepare data
				const formData = new FormData()

				/**
				 * Append textual input(s) to the form
				 */
				const extraFormInputBlob = new Blob([JSON.stringify(transportationCost.value)], {type : 'application/json'})
				const extraFormInputFile = new File([extraFormInputBlob], 'matrix')
				formData.append( "matrix", extraFormInputFile )
				//#endregion prepare data

				/**
			 * Upload files to the server
			 */
				context.$axios.$post( '/solver/transportation', formData ).then( ( res ) =>{

					// console.table( res )

					console.log('%c Initial Basic Feasable Solution', eww_css )
					const processed = res
					stepData.value = res.stepData
					// console.log(stepData.value)
					fistStep.value = stepData.value[0]
					console.log(fistStep.value)
					stepIndex.value = 0

					IBFS.value = processed.result

					console.groupCollapsed('Step by step')
					stepData.value.forEach( (step: number[][], i: number)=>{
						console.log("🔰 %c Step ", "color:'#00ff00';background-color: '#aaaaaa'; height: 16px;")
						console.table( step )
					})
					console.groupEnd()

					// console.log('✅ Final')
					// console.table(processed.finalData)

					console.log(`%c💲 IBFS: %c${processed.result}`, `color: #00000000; font-size:16px;-webkit-text-stroke:1px white;`,'color:green; font-size:22px;font-wieght: bold')


				}).catch( ( err)  =>{

					console.log(`Uploading problem:\n${err.message}`)

				})

			})

		})

		return { numberOfSource, numberOfDestination, transportationCost, isBalancedTransportationProblem, stepData, fistStep, stepIndex, PreviousStep, NextStep, IBFS }

	},
})
</script>

<style>
	.vertical-range {
		-webkit-transform: rotate(90deg);
		-moz-transform: rotate(90deg);
		-o-transform: rotate(90deg);
		transform: rotate(90deg);
	}
</style>