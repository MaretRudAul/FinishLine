/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['League Gothic', 'sans-serif'],
      },
      colors: {
        darkred: '#8B0000'
      }
    },
  },
  plugins: [],
}

