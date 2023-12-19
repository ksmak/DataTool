export interface IUser {
    id: number,
    username: string,
    fullName: string,
}

export interface IMenu {
    id: number,
    title: string,
    link?: string,
    items?: IMenu[],
}

export interface IField {
    id: number,
    pos: number,
    title: string,
    group: number,
    is_key: boolean,
    is_enable: boolean,
    precision: number,
    dictionary: number,
    field_name: string,
    field_type: string,
    is_require: boolean,
    is_visible: boolean,
    is_duplicate: boolean
}

export interface IGroup {
    id: number,
    pos: number,
    title: string,
    fields: IField[],
    is_multy: boolean,
    table_name: string,
}

export interface IForms {
    id: number,
    pos: number,
    title: string,
    groups: IGroup[],
    form_type: string
}

export interface IReports {
    id: number,
    pos: number,
    title: string,
}

export interface IConvertor {
    id: number,
    pos: number,
    title: string,
}

export interface IDatabase {
    id: number,
    pos: number,
    title: string,
    forms: IForms[],
    reports: IReports[],
    convertors: IConvertor[],
}

export interface IAuthContext {
    user: IUser | null,
    isAuthenticated: boolean,
    login: (user: IUser, accessToken: string, refreshToken: string) => void,
    logout: () => void,
}

export interface IMetaContext {
    db: IDatabase | null,
    setDb: React.Dispatch<React.SetStateAction<IDatabase | null>> | null
}