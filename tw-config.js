// Réglages Tailwind communs (charte du site) — chargé juste après le CDN Tailwind
tailwind.config = {
  theme: {
    extend: {
      colors: {
        navy: { 50: '#f0f3f6', 100: '#d9e0e8', 200: '#b3c1d1', 300: '#8da2ba', 400: '#6783a3', 500: '#41648c', 600: '#335075', 700: '#253c5e', 800: '#172847', 900: '#0B1D2E' },
        glacier: { 50: '#eef8f9', 100: '#d5eff2', 200: '#abdfe5', 300: '#81cfd8', 400: '#5bbfcb', 500: '#4DA8B5', 600: '#3d8691', 700: '#2e656d', 800: '#1f4349', 900: '#0f2224' },
        cream: { 50: '#FAFAF8', 100: '#F5F4F0', 200: '#ECEAE4', 300: '#DFDBCF', 400: '#C8C3B5' },
        gold: { 300: '#DCCBA8', 400: '#C4A97D', 500: '#A88C5C' },
      },
      fontFamily: {
        serif: ['Satoshi', 'system-ui', 'sans-serif'],
        sans: ['Satoshi', 'system-ui', 'sans-serif'],
      },
    },
  },
};
