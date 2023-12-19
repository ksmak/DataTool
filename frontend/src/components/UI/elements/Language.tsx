import { useTranslation } from "react-i18next";

export default function Language() {
    const { i18n } = useTranslation();

    const langs = [
        {
            title: 'KAZ',
            label: 'kk'
        },
        {
            title: 'RUS',
            label: 'ru'
        },
    ]

    return (
        <div className='flex flex-row justify-center items-center gap-4 text-white font-bold'>
            {langs.map((item, index) => (
                <span
                    key={index}
                    className={`${i18n.language === item.label ? 'border-2 border-white' : ''} p-1 text-sm rounded-md hover:cursor-pointer`}
                    onClick={() => i18n.changeLanguage(item.label)}
                >
                    {item.title}
                </span>
            ))}
        </div>
    )
}