'use client'

import { ChangeEvent } from "react"

type FieldProps = {
    label: string,
    value: string | number | undefined,
    handleChange: (e: ChangeEvent<HTMLInputElement>) => void
    length?: number
}

export default function Field({ label, value, handleChange, length }: FieldProps) {
    return (
        <div className="flex flex-col gap-1 text-sm">
            <label htmlFor="new-dictionary">{label}</label>
            <input
                id="new-dictionary"
                className="border-2 p-1 text-sm text-gray-800 tracking-normal font-mono"
                type="text"
                value={value}
                onChange={handleChange}
                maxLength={length ? length : 30}
                size={length ? length : 30}
            />
        </div>
    )
}