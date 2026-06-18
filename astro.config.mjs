// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://roben.lunardi.inf.br',
  base: '/',
  vite: {
    plugins: [tailwindcss()]
  }
});