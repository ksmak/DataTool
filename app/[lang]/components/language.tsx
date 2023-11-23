'use client'

import { usePathname } from 'next/navigation';
import Link from 'next/link';

type LanguageProps = {
    lang: string
}

export default function Language({ lang }: LanguageProps) {
    const pathName = usePathname()
    const redirectedPathName = (locale: string) => {
        if (!pathName) return '/';
        const segments = pathName.split('/');
        segments[1] = locale;
        return segments.join('/');
    }

    return (
        <div className='flex flex-row justify-center items-center gap-4 text-white font-bold'>
            <Link href={redirectedPathName('kk')} className={`p-1 text-sm rounded-md ${lang === 'kk' ? 'border-2 border-white' : ''}`}>KAZ</Link>
            <Link href={redirectedPathName('ru')} className={`p-1 text-sm rounded-md ${lang === 'ru' ? 'border-2 border-white' : ''}`}>RUS</Link>
        </div>
    )
}