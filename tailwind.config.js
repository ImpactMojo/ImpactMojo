// tailwind.config.js
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html"
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'Segoe UI', 'Roboto', 'sans-serif'],
        heading: ['Dancing Script', 'cursive'],
      },
      colors: {
        'chalkboard-dark': '#2c3e50',
        'chalk-white': '#f8f9fa',
        'accent-blue': '#3498db',
        'accent-green': '#2ecc71',
        'accent-yellow': '#f1c40f',
        'accent-purple': '#9b59b6',
      },
      backgroundImage: {
        'chalkboard': "url('/assets/chalkboard-texture.png')",
      },
    },
  },
  plugins: [],
}
