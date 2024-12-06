import { useState, FormEvent } from "react"
import loginClienteService from "@/service/login-cliente"
import Cookies from "js-cookie"
import { Label } from "@/components/molecules/label"
import { Input } from "@/components/molecules/input"
import { Button } from "@/components/molecules/button"
import { Chrome, Phone } from "lucide-react"
import { useNavigate } from "react-router-dom"
import { toast } from "sonner"
import { Checkbox } from "@/components/molecules/checkbox"
import { AuthBase } from "@/components/organisms/auth-base"

export function Login() {
    const [credencial, setNomeUsuario] = useState("")
    const [senha, setSenha] = useState("")
    const navigate = useNavigate()

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault()

        const response = await loginClienteService.obterToken({
            credencial: credencial,
            senha: senha,
        })

        if (response.status === 201) {
            const { access_token } = response?.data

            Cookies.set("jwt_token", access_token, {
                secure: true,
                sameSite: "strict",
            })

            toast.success("Bem-vindo ao sistema!", {
                description: "Login realizado com sucesso.",
                action: {
                    label: "Fechar",
                    onClick: () => {},
                },
            })
            navigate("/home")
        } else {
            toast.error(response, {
                description: "Verifique os parâmetros de entrada.",
                action: {
                    label: "Fechar",
                    onClick: () => {},
                },
            })
        }
    }

    return (
        <AuthBase>
            <div className="px-16 rounded-l-xl h-full min-w-80 w-[600px] z-50">
                <form onSubmit={handleSubmit}>
                    <h1 className="text-3xl font-semibold mb-8">
                        Seja Bem-Vindo(a)
                    </h1>
                    <h1 className="text-2xl font-semibold flex justify-center">
                        Entrar
                    </h1>
                    <h1 className="text-md font-semibold mb-4 flex justify-center text-salmon-950/40">
                        Entre para ficar conectado
                    </h1>
                    <div className="mb-4 mt-16">
                        <Label
                            htmlFor="nome_usuario"
                            className="block text-salmon-950 mb-2"
                        >
                            Usuário ou e-mail
                        </Label>
                        <Input
                            id="nome_usuario"
                            type="text"
                            value={credencial}
                            onChange={(e) => setNomeUsuario(e.target.value)}
                            className="border-sky-900"
                        />
                    </div>

                    <div className="mb-1">
                        <Label
                            htmlFor="senha"
                            className="block text-salmon-950 mb-2"
                        >
                            Senha
                        </Label>
                        <Input
                            id="senha"
                            type="password"
                            value={senha}
                            onChange={(e) => setSenha(e.target.value)}
                            className="border-sky-900"
                        />
                    </div>

                    <div className="flex justify-between">
                        <div className="flex space-x-2 items-center">
                            <Checkbox />
                            <span>Lembrar de mim?</span>
                        </div>
                        <button
                            type="reset"
                            className="text-salmon-600 hover:underline hover:text-salmon-700"
                            onClick={() => navigate("/password-recovery")}
                        >
                            Esqueci minha senha
                        </button>
                    </div>

                    <Button
                        type="submit"
                        className="w-full mt-8"
                        variant="primary"
                    >
                        Entrar
                    </Button>
                </form>
                <div className="flex items-center mt-4 flex-1 space-x-2">
                    <div className="flex-grow h-px bg-salmon-950"></div>
                    <span className="text-md">ou</span>
                    <div className="flex-grow h-px bg-salmon-950"></div>
                </div>

                <div className="flex justify-around space-x-4 mt-4">
                    <Button className="w-full" variant="primary">
                        <Chrome />
                        Login com o Google
                    </Button>
                    <Button className="w-full" variant="primary">
                        <Phone />
                        Login com o telefone
                    </Button>
                </div>

                <div className="flex justify-center mt-8 space-x-1">
                    <span>Ainda não tem cadastro?</span>
                    <button
                        className="text-salmon-600 hover:underline hover:text-salmon-700"
                        onClick={() => navigate("/register")}
                    >
                        Cadastrar-se
                    </button>
                </div>
            </div>

            <div className="flex flex-1 justify-center h-screen w-full items-center bg-white/10">
                imagem sem fundo
            </div>
        </AuthBase>
    )
}
