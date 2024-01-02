import axios, { AxiosInstance } from "axios"

export default function datatoolModule(instance: AxiosInstance) {
    return {
        getDbList() {
            return axios.get(`${process.env.REACT_APP_HOST_API}api/meta/db/`)
        },

        getDb(id: number, accessToken: string) {
            return axios({
                method: 'get',
                url: `${process.env.REACT_APP_HOST_API}api/meta/db/${id}`,
                headers: {
                    Authorization: `Bearer ${accessToken}`,
                }
            })
        },
    }
}

