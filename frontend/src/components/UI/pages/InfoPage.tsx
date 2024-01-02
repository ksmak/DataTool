import { useEffect, useState } from "react";
import { useParams } from "react-router-dom"
import { useMeta } from "../../../lib/meta";
import { IForms } from "../../../types/types";

export default function InfoPage() {
    const params = useParams();
    const { database } = useMeta();
    const [form, setForm] = useState<IForm | null>();
    // const id = params.id;
    const form_id = params.form_id;

    useEffect(() => {
        setForm(getForm(Number(form_id)));
    }, [form_id]);

    function getForm(form_id: number): IForm | null {
        database?.forms.forEach(form => {
            if (form.form_type === 'input_form' && form.id === form_id) {
                return form;
            }
        })
        return null;
    }

    return (
        <div>
            {form?.title}
            <form action="">
                {form && form.groups?.map(gr => (
                    <div>{gr.title}</div>
                ))}
            </form>
        </div>
    )
}