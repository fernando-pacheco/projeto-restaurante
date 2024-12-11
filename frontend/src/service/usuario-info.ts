import { api } from "@/api"
import { AxiosError } from "axios"

export class UsuarioInfoService {
    async getInfoUsuario() {
        try {
            const response = await api.get("/usuario-info")
            return response
        } catch (error) {
            if (error instanceof AxiosError) {
                return error.response
            }

            return error
        }
    }
}
