/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        'primary': '#575A6C',
        'secondary': '#73C536',
        'accent': '#3686C9',
        'background': '#E0E2D2',
        'rich-black': '#0A1D29',
        'dark-khaki': '#C3C786'
      },
    },
  },
  plugins: [],
}
