// Feuille compilée de tout le site (système de patch.io sur fond nuit : Albert Sans Light, IBM Plex Mono, action en orange).
// Après toute modification de classes :
// npx -y tailwindcss@3.4.17 -c tailwind.config.cjs -i tw-entree.css -o assets/v2/site-tw.css --minify
module.exports = {
  theme: {
    extend: {
      colors: {
        nuit: { DEFAULT: '#0A1622', 2: '#0F2030', 3: '#16293B' },
        navy: { 50: '#f0f3f6', 100: '#d9e0e8', 200: '#b3c1d1', 300: '#8da2ba', 400: '#6783a3', 500: '#41648c', 600: '#335075', 700: '#253c5e', 800: '#0F2030', 900: '#0A1622' },
        glacier: { 50: '#eef8f9', 100: '#d5eff2', 200: '#abdfe5', 300: '#81cfd8', 400: '#5bbfcb', 500: '#4DA8B5', 600: '#3d8691', 700: '#2e656d', 800: '#1f4349', 900: '#0f2224' },
        cream: { 50: '#FAFAF8', 100: '#F5F4F0', 200: '#ECEAE4', 300: '#DFDBCF', 400: '#C8C3B5' },
        rouge: { DEFAULT: '#EA642B', fonce: '#D2541F' },
        sable: '#F4F3EF',
      },
      fontFamily: {
        sans: ['Albert Sans', 'system-ui', 'sans-serif'],
        serif: ['Albert Sans', 'system-ui', 'sans-serif'],
        mono: ['IBM Plex Mono', 'ui-monospace', 'monospace'],
      },
    },
  },
  content: ['./*.html', './components.js', './catalogue.js', './site-config.js', './assets/v2/*.js'],
};
