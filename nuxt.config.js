export default {
	// Global page headers: https://go.nuxtjs.dev/config-head
	head: {
		title: 'pyts',
		htmlAttrs: {
			lang: 'en'
		},
		meta: [
			{ charset: 'utf-8' },
			{ name: 'viewport', content: 'width=device-width, initial-scale=1' },
			{ hid: 'description', name: 'description', content: '' }
		],
		link: [
			{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
		]
	},

	serverMiddleware: [
		'~/backend/server.ts'
	],

	// Global CSS: https://go.nuxtjs.dev/config-css
	css: [
	],

	// Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
	plugins: [
	],

	// Auto import components: https://go.nuxtjs.dev/config-components
	components: true,

	// Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
	buildModules: [
		// https://go.nuxtjs.dev/typescript
		'@nuxt/typescript-build',
		// https://go.nuxtjs.dev/tailwindcss
		'@nuxtjs/tailwindcss',
		'@nuxtjs/axios',
		'@nuxtjs/composition-api/module'
	],

	tailwindcss: {
		mode: 'jit',
	},

	// Modules: https://go.nuxtjs.dev/config-modules
	modules: [
		'nuxt-compress'
	],

	'nuxt-compress': {
		gzip: {
			threshold: 8192,
		},
		brotli: {
			threshold: 8192,
		},
	},

	// Build Configuration: https://go.nuxtjs.dev/config-build
	build: {
	}
}
