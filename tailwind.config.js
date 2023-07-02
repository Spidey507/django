/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './suntory/templates/**/*.html',  // Add the path to your HTML templates
    './suntory/static/**/*.js',       // Add the path to your JavaScript files
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/aspect-ratio'),
    require('flowbite/plugin'),
  ],
}

///for whatever reason I need to run npx tailwindcss build suntory/static/suntory/styles.css -o suntory/static/suntory/output.css --watch everytime 
///I change something in the styles