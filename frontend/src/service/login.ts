import { api } from "@/api/index"
import { LoginProps } from "../interface/login"
import { AxiosError } from "axios"

export class LoginService {
    async getTokenCliente(body: LoginProps) {
        try {
            const response = await api.post("/token-cliente", body)
            return response
        } catch (error) {
            if (error instanceof AxiosError) {
                return error.response
            }

            return error
        }
    }

    async getTokenFuncionario(body: LoginProps) {
        try {
            const response = await api.post("/token-funcionario", body)
            return response
        } catch (error) {
            if (error instanceof AxiosError) {
                return error.response
            }

            return error
        }
    }
}
