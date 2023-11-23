import { Locale } from '@/i18n-config';
import { getDictionary } from '../../get-dictionary';

export default async function Home({ params: { lang } }: { params: { lang: Locale } }) {
  const dictionary = await getDictionary(lang);

  return (
    <main>
      <h1>{dictionary.title}</h1>
    </main>
  )
}
