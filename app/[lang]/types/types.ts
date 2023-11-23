export enum FormType {
    dictionary = 'dictionary',
    database = 'database',
    input_form = 'input_form',
    search_form = 'search_form',
    print_form = 'print_form'
}

export type MenuType = {
    id: number,
    title: string,
    link?: string,
    items?: MenuType[]
}

export type TreeType = {
    id: number,
    title: string,
    form: FormType,
    items?: TreeType[],
    children?: React.ReactNode
}

export type DictionaryType = {
    id?: string,
    name: string
}