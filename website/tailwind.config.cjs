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
        'primary-hover': '#008B00',
      },
      keyframes: {
        wiggle: {
          '0%, 100%': { transform: 'rotate(-3deg)' },
          '50%': { transform: 'rotate(3deg)' },
        },
      },
      animation: {
        'short-bounce': 'bounce 1s ease-in-out 2',
        wiggle: 'wiggle 1s ease-in-out 1',
      },
    },
  },
  plugins: [],
}
