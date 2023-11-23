'use client'

import { join } from "path";
import { useState } from "react"
import { BiChevronUp } from "react-icons/bi";

export default function Collapse({
    title,
    cls,
    setNode,
    children
}: {
    title: string,
    cls?: string,
    setNode: () => void,
    children?: React.ReactNode
}) {
    const [open, setOpen] = useState(false);

    return (
        <div className="relative">
            <div
                className={[cls, "text-primary hover:cursor-pointer flex flex-row items-center gap-1"].join(' ')}
                onClick={() => {
                    setOpen(!open);
                    setNode();
                }}
            >
                {title}
                {children ? open ? <BiChevronUp /> : <BiChevronUp className="transition-transform rotate-180" /> : null}
            </div>
            <div
                className={`${open ? "absolute top-6 left-3" : "hidden"}`}

            >
                {children}
            </div>
        </div>
    )
}