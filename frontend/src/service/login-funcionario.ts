import { api } from '@/api/index'
import { LoginProps } from './interface/login-interface'

class LoginFuncionario {
    async obterToken(corpo: LoginProps) {
        try {
            const response = await api.post(
                '/token-funcionario',
                corpo
            )
            return response
        } catch (error) {
            console.error(error)
        }
    }
}

const loginFuncionarioService = new LoginFuncionario()
export default loginFuncionarioService