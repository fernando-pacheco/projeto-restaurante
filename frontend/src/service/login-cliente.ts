import { api } from "@/api/index"
import { LoginProps } from "./interface/login-interface"
import { AxiosError } from "axios"

class LoginCliente {
    async obterToken(corpo: LoginProps) {
        try {
            const response = await api.post("/token-cliente", corpo)
            return response
        } catch (error) {
            if (error instanceof AxiosError) {
                return error.response?.data?.message
            } else {
                return "Erro desconhecido"
            }
        }
    }
}

const loginClienteService = new LoginCliente()
export default loginClienteService
