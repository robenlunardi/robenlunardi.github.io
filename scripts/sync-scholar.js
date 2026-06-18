import axios from 'axios';
import * as cheerio from 'cheerio';
import fs from 'fs';
import path from 'path';

const SCHOLAR_ID = 'PTMGNKIAAAAJ';
const SCHOLAR_URL = `https://scholar.google.com.br/citations?user=${SCHOLAR_ID}&hl=en&oi=ao&pagesize=100`;

function detectLanguage(title) {
  const portugueseWords = [' e ', ' para ', ' de ', ' o ', ' a ', ' os ', ' as ', ' com ', ' em ', ' do ', ' da ', ' no ', ' na ', ' Redes ', ' Computadores ', ' Segurança ', ' Avaliação ', ' Desenvolvimento '];
  const titleLower = title.toLowerCase();
  const isPortuguese = portugueseWords.some(word => titleLower.includes(word.toLowerCase()));
  return isPortuguese ? 'PT' : 'EN';
}

async function fetchPublications() {
  try {
    console.log('Fetching publications from Google Scholar...');
    const { data } = await axios.get(SCHOLAR_URL, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
      }
    });

    const $ = cheerio.load(data);
    const publications = [];

    $('.gsc_a_tr').each((i, el) => {
      const title = $(el).find('.gsc_a_at').text();
      const link = 'https://scholar.google.com' + $(el).find('.gsc_a_at').attr('href');
      const authors = $(el).find('.gs_gray').first().text();
      const venue = $(el).find('.gs_gray').last().text();
      const citations = parseInt($(el).find('.gsc_a_ac').text()) || 0;
      const year = $(el).find('.gsc_a_y').text();
      const lang = detectLanguage(title);

      publications.push({
        title,
        link,
        authors,
        venue,
        citations,
        year,
        lang
      });
    });

    console.log(`Found ${publications.length} publications.`);

    const dataPath = path.join(process.cwd(), 'src/data/publications.json');
    fs.writeFileSync(dataPath, JSON.stringify(publications, null, 2));
    console.log(`Successfully saved to ${dataPath}`);

  } catch (error) {
    console.warn('Warning: Could not fetch publications from Google Scholar (likely blocked).');
    console.warn('Reason:', error.message);
    
    // Check if the data file already exists
    const dataPath = path.join(process.cwd(), 'src/data/publications.json');
    if (fs.existsSync(dataPath)) {
      console.log('Using existing publications.json data.');
    } else {
      console.error('Error: No existing publications.json found and fetch failed.');
      process.exit(1);
    }
  }
}

fetchPublications();
