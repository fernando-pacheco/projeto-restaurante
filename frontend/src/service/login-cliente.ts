import { api } from '@/api/index'
import { LoginProps } from './interface/login-interface'

class LoginCliente {
    async obterToken(corpo: LoginProps) {
        try {
            const response = await api.post(
                '/token-cliente',
                corpo
            )
            return response
        } catch (error) {
            console.error(error)
        }
    }
}

const loginClienteService = new LoginCliente()
export default loginClienteService