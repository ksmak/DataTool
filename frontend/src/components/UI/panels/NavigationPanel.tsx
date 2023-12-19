import { useEffect, useState } from "react";
import { useMeta } from "../../../lib/meta"
import { IDatabase, IMenu } from "../../../types/types";
import Logo from "../elements/Logo";
import Menu from "../elements/Menu";
import UserInfo from "../elements/UserInfo";
import Language from "../elements/Language";

export default function NavigationPanel() {
    const [menu, setMenu] = useState<IMenu[]>([]);
    const { db } = useMeta();
    const initMenu = (db: IDatabase | null) => {
        let mnu: IMenu[] = [];
        mnu.push({
            id: 1,
            title: "База данных",
            items: [],
        });
        mnu.push({
            id: 2,
            title: "Ввод информации",
            items: [],
        });
        mnu.push({
            id: 3,
            title: "Поиск информации",
            items: [],
        });
        db?.forms.forEach(form => {
            if (form.form_type === 'input_form') {
                mnu[1].items?.push({
                    id: form.id,
                    title: form.title
                })
            }
            if (form.form_type === 'search_form') {
                mnu[2].items?.push({
                    id: form.id,
                    title: form.title
                })
            }
        })
        mnu.push({
            id: 4,
            title: "Справка",
            items: [],
        });

        setMenu(mnu);
    }

    useEffect(() => {
        initMenu(db);
        console.log(db);
        console.log(menu);
    }, [db]);

    return (
        <div className="flex flex-row justify-between items-center border-b-2 py-2 px-4 bg-primary mb-4">
            <div>
                <Logo />
            </div>
            <nav className="grow">
                <ul className="flex flex-row justify-center gap-4 text-white">
                    {menu.map((item) => {
                        return (
                            <Menu key={item.id} item={item} />
                        )
                    })}
                </ul>
            </nav>
            <div className="flex flex-row justify-between items-center gap-10">
                <UserInfo />
                <Language />
            </div>
        </div>
    )
}