import { AxiosInstance } from "axios"

export default function datatoolModule(instance: AxiosInstance) {
    return {
        getStructDb(db_id: number) {
            return instance({
                method: 'get',
                url: `api/databases/${db_id}/`,
            })
        },
    }
}

