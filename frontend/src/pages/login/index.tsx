import { useState, FormEvent } from "react"
import loginClienteService from "@/service/login-cliente"
import Cookies from "js-cookie"
import { Label } from "@/components/molecules/label"
import { Input } from "@/components/molecules/input"
import { Button } from "@/components/molecules/button"
import { Chrome, Phone } from "lucide-react"
import { useNavigate } from "react-router-dom"
import { toast } from "sonner"

export function Login() {
    const [credencial, setNomeUsuario] = useState("")
    const [senha, setSenha] = useState("")
    const navigate = useNavigate()

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault()

        const response = await loginClienteService.obterToken(
            { "credencial": credencial, "senha": senha }
        )

        if (response.status === 201) {
            const { access_token } = response?.data

            Cookies.set("jwt_token", access_token, { secure: true, sameSite: "strict" })

            toast.success("Login realizado com sucesso.", {
                description: "Bem-vindo ao sistema!",
                action: {
                    label: "Fechar",
                    onClick: () => { },
                },
            })
            navigate('/home')
        } else {
            toast.error(response, {
                description: "Verifique os parâmetros de entrada.",
                action: {
                    label: "Fechar",
                    onClick: () => { },
                },
            })
        }
    }

    return (
        <div className="flex justify-center items-center h-screen">
            <div className="w-[100%] h-[85%] flex bg-white">
                <div className="w-[40%] flex justify-center items-center text-black">
                    Imagem
                </div>
                <div className="bg-sky-900 flex-1 rounded-l-xl">
                    <div className="bg-white/50 p-8 rounded-l-xl h-full px-40">
                        <form onSubmit={handleSubmit}>
                            <h1 className="text-3xl font-semibold mb-16">Seja Bem-Vindo(a)</h1>
                            <h2 className="text-2xl font-semibold mb-4 flex justify-center">Login</h2>

                            <div className="mb-4">
                                <Label htmlFor="nome_usuario" className="block text-white mb-2">Usuário ou e-mail</Label>
                                <Input
                                    id="nome_usuario"
                                    type="text"
                                    value={credencial}
                                    onChange={(e) => setNomeUsuario(e.target.value)}
                                    className="text-black border-sky-900"
                                />
                            </div>

                            <div className="mb-4">
                                <Label htmlFor="senha" className="block text-white mb-2">Senha</Label>
                                <Input
                                    id="senha"
                                    type="password"
                                    value={senha}
                                    onChange={(e) => setSenha(e.target.value)}
                                    className="text-black border-sky-900"
                                />
                            </div>
                            <Button
                                type="submit"
                                className="w-full"
                                variant={"primary"}
                            >
                                Entrar
                            </Button>
                        </form>
                        <div className="flex items-center mt-4 flex-1 space-x-2">
                            <div className="flex-grow h-px bg-gray-300"></div>
                            <span className="text-md">ou</span>
                            <div className="flex-grow h-px bg-gray-300"></div>
                        </div>

                        <div className="flex justify-around space-x-4 mt-2">
                            <Button
                                className="w-full"
                                variant={"primary"}
                            >
                                <Chrome />
                                Login com o Google
                            </Button>
                            <Button
                                className="w-full"
                                variant={"primary"}
                            >
                                <Phone />
                                Login com o telefone
                            </Button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
