/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        'accent': '#575A6C',
        // 'primary': '#73C536',
        'primary': '#006500',
        'secondary': '#3686C9',
        'background': '#E0E2D2',
        'rich-black': '#0A1D29',
        'dark-khaki': '#C3C786'
      },
    },
  },
  plugins: [],
}
