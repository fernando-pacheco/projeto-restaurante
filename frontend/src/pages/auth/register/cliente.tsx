import Cookies from "js-cookie"
import { FormEvent, useState } from "react"
import { Label } from "@/components/atoms/label"
import { Input } from "@/components/atoms/input"
import { Button } from "@/components/atoms/button"
import { useNavigate } from "react-router-dom"
import { FormAuthBase } from "@/components/templates/form-auth-base"
import { setupToast } from "@/utils/setup-toast"
import { AxiosResponse } from "axios"
import { TelefoneService } from "@/service/telefone"
import { ClienteService } from "@/service/cliente"
import { LoginService } from "@/service/login"

export function RegisterCliente() {
    const navigate = useNavigate()
    const [error, setError] = useState("")

    const MESSAGES = {
        success: {
            description: "Cadastro realizado com sucesso.",
        },
        error: {
            title: "Problema ao realizar o cadastro.",
        },
    }

    function passwordValidate(senha: string, confirmacaoSenha: string) {
        if (senha === confirmacaoSenha) {
            return confirmacaoSenha
        } else {
            setError("Senhas não coincidem.")
        }
    }

    function formatBodyCliente(formData: FormData) {
        const senha = passwordValidate(
            formData.get("senha") as string,
            formData.get("confirmacaoSenha") as string,
        )

        return {
            nome_usuario: formData.get("nomeUsuario") as string,
            cpf: formData.get("cpf") as string,
            email: formData.get("email") as string,
            nome: formData.get("nome") as string,
            senha: senha as string,
            sobrenome: formData.get("sobrenome") as string,
        }
    }

    function handleRegisterSuccess(response: AxiosResponse) {
        setupToast({
            id: MESSAGES.success.description,
            status: "success",
            title: `Seja bem-vindo(a) ${response.data.nome}`,
            description: MESSAGES.success.description,
        })

        navigate("/login")
    }

    function handleRegisterResponse(
        formData: FormData,
        response: AxiosResponse,
    ) {
        if (response.status === 201) {
            if (formData.get("numero")) {
                makeAuth(formData)
                registerTelefone(formData, response.data.id)
            }

            handleRegisterSuccess(response)
        } else {
            response.data.messages.map((erro: { message: string }) => {
                setupToast({
                    id: erro.message,
                    status: "error",
                    title: MESSAGES.error.title,
                    description: erro.message,
                })
            })
        }
    }

    async function handleSubmit(e: FormEvent<HTMLFormElement>) {
        e.preventDefault()
        const service = new ClienteService()
        const formData = new FormData(e.currentTarget)
        const bodyCliente = formatBodyCliente(formData)

        if (!error) {
            const response = await service.clienteRegister(bodyCliente)
            handleRegisterResponse(formData, response as AxiosResponse)
        }
    }

    async function registerTelefone(formData: FormData, clienteID: string) {
        const service = new TelefoneService()
        const bodyTelefone = formatBodyTelefone(formData, clienteID)
        await service.telefoneRegister(bodyTelefone)
    }

    function formatBodyTelefone(formData: FormData, clienteID: string) {
        return {
            numero: formData.get("numero") as string,
            cliente_id: clienteID as string,
            principal: true,
        }
    }

    async function makeAuth(formData: FormData) {
        const service = new LoginService()
        const body = formatBodyAuth(formData)
        const response = await service.getTokenCliente(body)
        handleAuthSuccess(response as AxiosResponse)
    }

    function formatBodyAuth(formData: FormData) {
        return {
            credencial: formData.get("nomeUsuario") as string,
            senha: formData.get("senha") as string,
        }
    }

    function handleAuthSuccess(response: AxiosResponse) {
        const { access_token } = response?.data

        Cookies.set("jwt_token", access_token, {
            secure: true,
            sameSite: "strict",
        })
    }

    return (
        <FormAuthBase
            title="Cadastre-se"
            subtitle="Crie sua conta no [.....]"
            form={
                <form onSubmit={handleSubmit}>
                    <div className="flex justify-between space-x-2">
                        <div className="flex-1">
                            <Label>Nome *</Label>
                            <Input id="nome" name="nome" type="text" />
                        </div>
                        <div className="flex-1">
                            <Label>Sobrenome</Label>
                            <Input
                                id="sobrenome"
                                name="sobrenome"
                                type="text"
                                placeholder="Opcional"
                            />
                        </div>
                    </div>
                    <div className="flex justify-between space-x-2">
                        <div className="flex-1">
                            <Label>Nome de usuário *</Label>
                            <Input
                                id="nome_usuario"
                                name="nomeUsuario"
                                type="text"
                            />
                        </div>
                        <div className="flex-1">
                            <Label>E-mail *</Label>
                            <Input id="email" name="email" type="text" />
                        </div>
                    </div>
                    <div className="flex justify-between space-x-2">
                        <div className="flex-1">
                            <Label>CPF *</Label>
                            <Input id="cpf" name="cpf" type="text" />
                        </div>
                        <div className="flex-1">
                            <Label>Telefone</Label>
                            <Input id="numero" name="numero" type="text" />
                        </div>
                    </div>
                    <div className="flex flex-col">
                        <div className="flex-1">
                            <Label>Senha *</Label>
                            <Input id="senha" name="senha" type="password" />
                        </div>
                        <div className="flex-1">
                            <Label>Confirme sua senha *</Label>
                            <Input
                                id="confirmacaoSenha"
                                name="confirmacaoSenha"
                                type="password"
                            />
                        </div>
                    </div>
                    <Button
                        type="submit"
                        className="w-full mt-4"
                        variant="primary"
                    >
                        Cadastrar
                    </Button>
                </form>
            }
            typeForm="register"
            footerForm={
                <div className="flex justify-center mt-4 space-x-1">
                    <span>Já possui cadastro?</span>
                    <button
                        className="text-salmon-600 hover:underline hover:text-salmon-700"
                        onClick={() => navigate("/login")}
                    >
                        Entrar
                    </button>
                </div>
            }
        />
    )
}
