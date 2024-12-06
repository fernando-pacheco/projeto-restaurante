import { api } from "@/api"

export class UsuarioInfoService {
    async getInfoUsuario() {
        try {
            const response = await api.get("/usuario-info")
            return response
        } catch (error) {
            console.error(error)
        }
    }
}
