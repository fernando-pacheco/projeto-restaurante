import { api } from "@/api"

class UsuarioInfo {
    async obterInfoUsuario() {
        try {
            const response = await api.get(
                '/usuario-info'
            )
            return response
        } catch (error) {
            console.error(error)
        }
    }
}

const usuarioInfoService = new UsuarioInfo()
export default usuarioInfoService