/** @type {import('tailwindcss').Config} */
module.exports = {
	darkMode: ["class"],
	content: ["./index.html", "./src/**/*.{ts,tsx,js,jsx}"],
	theme: {
		extend: {
			borderRadius: {
				lg: 'var(--radius)',
				md: 'calc(var(--radius) - 2px)',
				sm: 'calc(var(--radius) - 4px)'
			},
			colors: {
				salmon: {
					50: '#fff3f1',
					100: '#ffe1df',
					200: '#ffcec5',
					300: '#ffac9d',
					400: '#ff7c65',
					500: '#ff5334',
					600: '#ed3615',
					700: '#bf280d',
					800: '#a5260f',
					900: '#882614',
					950: '#4a0f05'
				}
			},
			fontFamily: {
				sans: 'Inter'
			}
		}
	},
	plugins: [require("tailwindcss-animate")],
}
