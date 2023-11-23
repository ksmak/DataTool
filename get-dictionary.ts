import 'server-only'
import { Locale } from '@/i18n-config'

const dictionaries: { [key: string]: () => Promise<any> } = {
    ru: () => import('./dictionaries/ru.json').then((module) => module.default),
    kk: () => import('./dictionaries/kk.json').then((module) => module.default),
}

export const getDictionary = async (locale: Locale) =>
    dictionaries[locale]?.() ?? dictionaries.ru()