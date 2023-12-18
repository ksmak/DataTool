export interface IUser {
    id: number,
    name: string,
    firstName: string,
    lastName: string,
    middleName: string | null
}

export interface IAuthContext {
    user?: IUser,
    accessToken?: string,
    refreshToken?: string,
    login?: (username: string, password: string) => void,
    logout?: () => void,
}