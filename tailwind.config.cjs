// Feuille compilée des pages principales. Après toute modification de classes :
// npx -y tailwindcss@3.4.17 -c tailwind.config.cjs -i tw-entree.css -o assets/v2/site-tw.css --minify
module.exports = Object.assign({
  theme: {
    extend: {
      colors: {
        navy: { 50: '#F4F4F1', 100: '#E6E6E1', 200: '#CCCCC5', 300: '#A6A69E', 400: '#7F8078', 500: '#5D5E57', 600: '#45463F', 700: '#30322C', 800: '#1E201C', 900: '#141613' },
        glacier: { 50: '#eef8f9', 100: '#d5eff2', 200: '#abdfe5', 300: '#81cfd8', 400: '#5bbfcb', 500: '#4DA8B5', 600: '#3d8691', 700: '#2e656d', 800: '#1f4349', 900: '#0f2224' },
        rouge: { DEFAULT: '#EE6A2C', fonce: '#D85A1F' },
        cream: { 50: '#F7F7F4', 100: '#EFEFEA', 200: '#E3E3DC', 300: '#CFCFC7', 400: '#A6A69E' },
        gold: { 300: '#DCCBA8', 400: '#C4A97D', 500: '#A88C5C' },
      },
      fontFamily: {
        serif: ['Satoshi', 'system-ui', 'sans-serif'],
        sans: ['Satoshi', 'system-ui', 'sans-serif'],
      },
    },
  },
}, {
  content: ['./index.html','./boutique.html','./produit.html','./le-test.html','./partenaire.html','./merci.html','./contact.html','./mentions-legales.html','./confidentialite.html','./404.html','./design-system.html','./components.js','./catalogue.js','./site-config.js','./assets/v2/mecanismes.js'],
});
