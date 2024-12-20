import { FormEvent } from "react"
import { Label } from "@/components/atoms/label"
import { Input } from "@/components/atoms/input"
import { Button } from "@/components/atoms/button"
import { useNavigate } from "react-router-dom"
import { Checkbox } from "@/components/atoms/checkbox"
import { FormAuthBase } from "@/components/templates/form-auth-base"
import { setupToast } from "@/utils/setup-toast"
import { AxiosResponse } from "axios"
import { LoginService } from "@/service/login"
import { setToken } from "@/utils/token"
import { LogInIcon } from "lucide-react"

export function Login() {
    const navigate = useNavigate()

    const MESSAGES = {
        success: {
            title: "Bem-vindo ao sistema!",
            description: "Login realizado com sucesso.",
        },
        error: {
            title: "Problema ao realizar login.",
        },
    }

    function formatBody(formData: FormData) {
        return {
            credencial: formData.get("credencial") as string,
            senha: formData.get("senha") as string,
        }
    }

    function handleSuccess(response: AxiosResponse) {
        const { access_token } = response?.data

        setToken(access_token, 43200)
        setupToast({
            id: "success",
            status: "success",
            title: MESSAGES.success.title,
            description: MESSAGES.success.description,
        })
        navigate("/home")
    }

    function handleResponse(response: AxiosResponse) {
        if (response.status === 201) {
            handleSuccess(response)
        } else {
            setupToast({
                id: "error",
                status: "error",
                title: MESSAGES.error.title,
                description: response.data.message,
            })
        }
    }

    const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault()
        const service = new LoginService()
        const formData = new FormData(e.currentTarget)
        const body = formatBody(formData)
        const response = await service.getTokenCliente(body)
        handleResponse(response as AxiosResponse)
    }

    return (
        <FormAuthBase
            greetings="Seja Bem-Vindo(a)!"
            title="Entrar"
            subtitle="Entre para se manter conectado."
            typeForm="login"
            form={
                <form onSubmit={handleSubmit}>
                    <div className="mb-4 mt-10">
                        <Label htmlFor="credencial">Usuário ou e-mail</Label>
                        <Input id="credencial" type="text" name="credencial" />
                    </div>
                    <div className="mb-1">
                        <Label htmlFor="senha">Senha</Label>
                        <Input id="senha" type="password" name="senha" />
                    </div>
                    <div className="flex justify-between">
                        <div className="flex space-x-2 items-center">
                            <Checkbox />
                            <span>Lembrar de mim?</span>
                        </div>
                        <Button
                            type="reset"
                            variant="link"
                            size={"clean"}
                            onClick={() => navigate("/password-recovery")}
                        >
                            Esqueci minha senha
                        </Button>
                    </div>
                    <Button type="submit" className="w-full mt-8">
                        <LogInIcon />
                        Entrar
                    </Button>
                </form>
            }
            footerForm={
                <div className="flex justify-center mt-8 space-x-1">
                    <span>Ainda não tem cadastro?</span>
                    <Button
                        variant="link"
                        size={"clean"}
                        onClick={() => navigate("/register")}
                    >
                        Cadastrar-se
                    </Button>
                </div>
            }
        />
    )
}
