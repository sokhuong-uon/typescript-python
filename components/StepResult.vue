<template>
	<div class="w-screen h-screen flex flex-col bg-gray-900">
		<div class="w-full flex pl-32 items-center justify-start relative">

			<table v-if="stepData.length" class="table-fix w-auto ml-24 mt-8 p-3 rounded-lg bg-black text-gray-400 select-none">
				<thead class="p-2 text-gray-600">
					<tr>
						<th class="table-cel">S\D</th>
						<th v-for="(destination, i) of stepData[0]" :key="i" class="table-cel">
							<span v-if="i===stepData[0].length-1">Supply</span>
							<span v-else>D<sub>{{i+1}}</sub></span>
						</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="(source, i) of stepData[0][0]" :key="i">
						<td class="table-cel text-gray-600 font-bold">
							<span v-if="i===stepData[0][0].length-1">Demand</span>
							<span v-else>S<sub>{{i+1}}</sub></span>
						</td>
						<td v-for="(cost, j) of stepData[0]" :key="j" class="table-cel">

							<div v-if="(i===stepData[0].length-1)&&(j===stepData[0][0].length-1)" class="w-11/12 h-5/6 flex items-center justify-center rounded-md text-center text-3xl bg-gray-900">
								😊
							</div>

							<!-- <div v-else class="w-11/12 h-5/6 rounded-md text-center bg-gray-900 focus:outline-none" type="number" :name="`element-${i}${j}`" :id="`cell-${i}${j}`"></div>
							{{stepData}} -->

						</td>
					</tr>

				</tbody>
			</table>
			<pre class="text-white">
				{{stepData[0]}}
			</pre>
		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent, onMounted, PropType, ref, useContext, watch } from '@nuxtjs/composition-api'

type stepData = number[][][]

export default defineComponent({

	props:{
		stepData: {
			required: true,
			type: Array as PropType<stepData>
		}
	},

	setup( props ) {

		watch( props.stepData, (oldValue, newValue)=>{
			console.log(props.stepData);

		})

		onMounted( () => {

		})

		return {  }

	},
})
</script>
