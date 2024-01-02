import { useEffect, useState } from "react";
import { useMeta } from "../../../lib/meta"
import { IDatabase, IMenu } from "../../../types/types";
import Logo from "../elements/Logo";
import Menu from "../elements/Menu";
import UserInfo from "../elements/UserInfo";
import Language from "../elements/Language";
import { useTranslation } from "react-i18next";

export default function NavigationPanel() {
    const { t } = useTranslation();
    const [menu, setMenu] = useState<IMenu[]>([]);
    const { database } = useMeta();
    const initMenu = (db: IDatabase | null) => {
        let mnu: IMenu[] = [];
        mnu.push({
            id: 1,
            title: t('database'),
            items: [],
        });
        mnu.push({
            id: 2,
            title: t('menu_info'),
            items: [],
        });
        mnu.push({
            id: 3,
            title: t('menu_search'),
            items: [],
        });
        db?.forms.forEach(form => {
            if (form.form_type === 'input_form' && form.access_type !== null) {
                mnu[1].items?.push({
                    id: form.id,
                    title: form.title,
                    link: `/item/${form.id}`
                })
            }
            if (form.form_type === 'search_form' && form.access_type !== null) {
                mnu[2].items?.push({
                    id: form.id,
                    title: form.title
                })
            }
        })
        mnu.push({
            id: 4,
            title: t('menu_help'),
            items: [],
        });

        setMenu(mnu);
    }

    useEffect(() => {
        initMenu(database);
        console.log(database);
        console.log(menu);
    }, [database]);

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