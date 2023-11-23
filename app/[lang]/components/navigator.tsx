import { MenuType } from "../types/types";
import Language from "./language";
import Logo from "./logo";
import Menu from "./menu";
import UserInfo from "./userinfo";

type NavigatorProps = {
    lang: string
}

export default async function Navigator({ lang }: NavigatorProps) {
    const mainMenu: MenuType[] = [
        {
            id: 1,
            title: "Ввод информации",
            items: [],
        },
        {
            id: 2,
            title: "Поиск информdации",
            items: [],
        },
        {
            id: 3,
            title: "Отчеты",
            items: [],
        },
        {
            id: 4,
            title: "Сервис",
            items: [
                {
                    id: 1,
                    title: "Структура баз данных",
                    link: "/structure_db"
                },
                {
                    id: 1,
                    title: "Справочники"
                },
                {
                    id: 1,
                    title: "Генератор отчетов"
                },
                {
                    id: 1,
                    title: "Конвертор"
                },
                {
                    id: 1,
                    title: "Пользователи"
                },
            ]
        },
    ]
    return (
        <div className="flex flex-row justify-between items-center border-b-2 py-2 px-4 bg-primary mb-4">
            <div>
                <Logo />
            </div>
            <nav className="grow">
                <ul className="flex flex-row justify-center gap-4 text-white">
                    {mainMenu.map((item) => {
                        return (
                            <Menu key={item.id} item={item} />
                        )
                    })}
                </ul>
            </nav>
            <div className="flex flex-row justify-between items-center gap-10">
                <UserInfo />
                <Language lang={lang} />
            </div>
        </div>
    )
}