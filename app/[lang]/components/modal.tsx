'use client'

import { Dispatch, SetStateAction, useEffect, useRef } from "react";

type ModalProps = {
    title: string,
    open: boolean,
    setOpen: Dispatch<SetStateAction<boolean>>,
}

export default function Modal({ title, open, setOpen, children }: React.PropsWithChildren<ModalProps>) {
    const refModal = useRef(null);

    useEffect(() => {
        window.onclick = function (event) {
            if (event.target === refModal.current) {
                setOpen(false);
            }
        };
    }, []);

    return (
        <div
            className={`${open ? "flex overflow-hidden" : "hidden"} fixed inset-0 z-50 items-center justify-center overflow-auto bg-gray-800 bg-opacity-50`}
            ref={refModal}
        >
            <div className="bg-white p-8 rounded-lg shadow-lg">
                <h2 className="text-2xl font-bold mb-4 text-primary">{title}</h2>
                {children}
            </div>
        </div>

    )
}