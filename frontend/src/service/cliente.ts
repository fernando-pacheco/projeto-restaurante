import { api } from "@/api"
import { RegisterClienteProps } from "../interface/register"
import { AxiosError } from "axios"

export class ClienteService {
    async clienteRegister(body: RegisterClienteProps) {
        try {
            const response = await api.post("/cliente", body)
            return response
        } catch (error) {
            if (error instanceof AxiosError) {
                return error.response
            }

            return error
        }
    }
}
