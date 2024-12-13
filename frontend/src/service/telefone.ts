import { api } from "@/api"
import { TelefoneRegisterProps } from "../interface/telefone"
import { AxiosError } from "axios"

export class TelefoneService {
    async telefoneRegister(body: TelefoneRegisterProps) {
        try {
            const response = api.post("/telefone", body)
            return response
        } catch (error) {
            if (error instanceof AxiosError) {
                return error.response
            }

            return error
        }
    }
}
