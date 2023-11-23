import { Locale } from '@/i18n-config';
import { getDictionary } from '../../../get-dictionary';
import EditPanel from '../components/edit-panel';

export default async function Home({ params: { lang } }: { params: { lang: Locale } }) {
    const dictionary = await getDictionary(lang);

    return (
        <main className='container mx-auto min-h-screen flex flex-col'>
            <h1 className='self-center text-primary font-bold uppercase'>{dictionary.structureDB}</h1>
            <EditPanel />
        </main>
    )
}