import { Button } from "@/components/atoms/button"
import { Card } from "@/components/atoms/card"
import { CheckCircle } from "lucide-react"
import { useNavigate } from "react-router-dom"

export function ConfirmedPassword() {
    const navigate = useNavigate()

    return (
        <Card className="flex flex-col w-full items-center p-10">
            <CheckCircle className="size-28 text-salmon-700" />
            <span className="text-5xl mb-10">Sucesso!</span>
            <span className="text-salmon-950/60">
                Sua senha foi recuperada com sucesso!
            </span>
            <span className="text-salmon-950/60 mb-10">
                Volte para a página de login para entrar na sua conta.
            </span>
            <Button onClick={() => navigate("/login")}>
                Voltar para o início
            </Button>
        </Card>
    )
}
