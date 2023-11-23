'use client'

import { useEffect, useState } from "react"
import Collapse from "./collapse"
import { DictionaryType, FormType, TreeType } from "../types/types";
import Modal from "./modal";
import Field from "./field";
import prisma from "@/app/db";

export default function EditPanel() {
    const [node, setNode] = useState<FormType>();
    const [openDictionary, setOpenDictionary] = useState(false);
    const [dictionary, setDictionary] = useState<DictionaryType>({ name: '' });
    const [error, setError] = useState('');
    const [success, setSuccess] = useState(false);

    const tree: TreeType[] = [
        {
            id: 1,
            title: 'Справочники',
            form: FormType.dictionary,
        },
        {
            id: 2,
            title: 'База данных',
            form: FormType.database,
            items: [
                {
                    id: 1,
                    title: 'Формы для ввода информации',
                    form: FormType.input_form
                },
                {
                    id: 2,
                    title: 'Формы для поиска информации',
                    form: FormType.search_form
                },
                {
                    id: 3,
                    title: 'Формы для печати',
                    form: FormType.print_form
                },
            ]
        },
    ];

    const getToolbar = (form: FormType) => {
        switch (form) {
            case FormType.dictionary: {
                return (
                    <>
                        <button className="bg-primary p-2 text-white rounded-md" onClick={handleOpenDictionary}>Добавить</button>
                    </>
                )
            }
        }
    }

    const getForm = (form: FormType) => {
        switch (form) {
            case FormType.dictionary: {
                return (
                    <form>dictionary</form>
                )
            }
            case FormType.database: {
                return (
                    <form>database</form>
                )
            }
            case FormType.input_form: {
                return (
                    <form>input_form</form>
                )
            }
            case FormType.search_form: {
                return (
                    <form>search_form</form>
                )
            }
            case FormType.print_form: {
                return (
                    <form>print_form</form>
                )
            }
        }
    }

    const handleOpenDictionary = () => {
        setDictionary({ name: '' })
        setOpenDictionary(true);
    }

    const handleCreateDictionary = async () => {
        try {
            await prisma.dictionary.create({
                data: {
                    name: dictionary.name
                }
            });
            setSuccess(true);
        } catch(e: Error) {
            setError(e)
        }
        
    }

    useEffect(() => {
        console.log(dictionary);
    }, [dictionary])

    return (
        <div className="p-4 w-full flex flex-col gap-2">
            {/* modal */}
            <Modal title="Новый справочник" open={openDictionary} setOpen={setOpenDictionary}>
                <div className="flex flex-col items-center gap-2">
                    <Field
                        label="Наименование"
                        value={dictionary?.name}
                        handleChange={(e) => setDictionary({ ...dictionary, name: e.target.value })}
                        length={50}
                    />
                    <div className="self-end flex flex-row flex-wrap items-center gap-4">
                        <button className="bg-primary p-2 text-sm text-white rounded-md" onClick={handleCreateDictionary}>Сохранить</button>
                        <button className="bg-primary p-2 text-sm text-white rounded-md" onClick={() => setOpenDictionary(false)}>Закрыть</button>
                    </div>
                </div>
            </Modal>
            {/* toolbar */}
            <div className="flex flex-row flex-wrap gap-4 self-end">
                {node ? getToolbar(node) : null}
            </div>
            <div className='flex flex-row flex-wrap gap-4'>
                {/* tree */}
                <div className='w-1/4 border-2'>
                    {tree
                        ? tree.map((item) => (
                            <Collapse
                                key={item.id}
                                title={item.title}
                                setNode={() => setNode(item.form)}
                            >
                                {item.items
                                    ? item.items.map((it1) => (
                                        <Collapse
                                            key={it1.id}
                                            title={it1.title}
                                            setNode={() => setNode(it1.form)}
                                        >
                                            {it1.items
                                                ? it1.items.map((it2) => (
                                                    <Collapse
                                                        key={it2.id}
                                                        title={it2.title}
                                                        setNode={() => setNode(it2.form)}
                                                        cls={item.form === node ? "text-white bg-primary" : ""}
                                                    >
                                                        {it2.children}
                                                    </Collapse>
                                                ))
                                                : null}
                                        </Collapse>
                                    ))
                                    : null}
                            </Collapse>
                        ))
                        : null}
                </div>
                {/* form */}
                < div className='grow border-2' >
                    {node ? getForm(node) : null}
                </div>
            </div>
        </div>
    )
}