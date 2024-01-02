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

export interface IForm {
    id: number,
    pos: number,
    title: string,
    groups: IGroup[],
    form_type: string,
    access_type: string | null,
}

export interface IReport {
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
    forms: IForm[],
    reports: IReport[],
    convertors: IConvertor[],
}

export interface IDb {
    id: number,
    title: string,
}

export interface IAuthContext {
    user: IUser | null,
    isAuthenticated: boolean,
    login: (user: IUser, accessToken: string, refreshToken: string) => void,
    logout: () => void,
    dbList: IDb[]
}

export interface IMetaContext {
    database: IDatabase | null,
    setDb: (db: IDatabase) => void,
}