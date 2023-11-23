'use client'

import { useState } from "react";
import { MenuType } from "../types/types";
import { BiChevronUp } from "react-icons/bi";
import Link from "next/link";

type MenuProps = {
    item: MenuType,
}

export default function Menu({ item }: MenuProps) {
    const [open, setOpen] = useState(false);

    return (
        <li
            className="h-full relative flex flex-row items-center gap-1 hover:cursor-pointer"
            onMouseOver={() => setOpen(true)}
            onMouseOut={() => setOpen(false)}
            onClick={() => setOpen(!open)}
        >
            {item.title}
            {open ? <BiChevronUp /> : <BiChevronUp className="transition-transform rotate-180" />}
            {open
                ? <div
                    className="flex flex-col"
                    onMouseOver={() => setOpen(true)}
                    onMouseOut={() => setOpen(false)}
                >
                    <div className="absolute top-6 -left-5 z-50 bg-white border-2">
                        {item.items
                            ? item.items.map((it) => (
                                <div key={it.id} className="p-2 text-primary w-96 hover:bg-secondary">
                                    <Link href={it.link ? it.link : "/"}>
                                        {it.title}
                                    </Link>
                                </div>
                            ))
                            : null}
                    </div>
                </div>
                : null}
        </li>
    )
}