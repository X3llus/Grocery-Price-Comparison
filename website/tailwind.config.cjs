/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        'accent': '#3686C9',
        'primary': '#006500',
        'secondary': '#575A6C',
        'background': '#F0FFF0',
        'rich-black': '#0A1D29',
      },
    },
  },
  plugins: [],
}
