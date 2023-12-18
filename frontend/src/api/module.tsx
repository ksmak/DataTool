import { AxiosInstance } from "axios"

export default function datatoolModule(instance: AxiosInstance) {
    return {
        login(username: string, password: string) {
            return instance({
                method: 'post',
                url: 'api/token/',
                data: { username, password },
            })
        },
    }
}

