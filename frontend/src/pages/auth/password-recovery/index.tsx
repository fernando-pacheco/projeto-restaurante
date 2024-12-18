import { useState } from "react"
import { FormAuthBase } from "@/components/templates/form-auth-base"
import { Button } from "@/components/atoms/button"
import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from "@/components/atoms/card"
import { Input } from "@/components/atoms/input"
import { Label } from "@/components/atoms/label"
import {
    Tabs,
    TabsContent,
    TabsList,
    TabsTrigger,
} from "@/components/atoms/tabs"
import {
    CheckCircle,
    CircleAlert,
    CornerUpRight,
    Save,
    Send,
    Undo2,
} from "lucide-react"
import { ConfirmedPassword } from "./confirmed-password"
import { setupToast } from "@/utils/setup-toast"

export function PasswordRecovery() {
    const [currentStep, setCurrentStep] = useState(0)
    const [error, setError] = useState("")
    const steps = ["email", "validacao", "senha"]

    const content = [
        {
            title: "E-mail",
            description:
                "Insira seu email para gerar token de recuperação de senha.",
            form: <FormEmail onNext={() => handleNext()} error={error} />,
        },
        {
            title: "Validação",
            description: "Insira o código de validação recebido por e-mail.",
            form: (
                <FormValidation
                    onNext={() => handleNext()}
                    onBack={() => handleBack()}
                />
            ),
        },
        {
            title: "Senha",
            description:
                "Altere sua senha aqui. Após salvar, você será redirecionado.",
            form: (
                <FormPassword
                    onNext={() => handleNext()}
                    onBack={() => handleBack()}
                />
            ),
        },
    ]

    function handleNext() {
        if (currentStep < steps.length) {
            setCurrentStep((prev) => prev + 1)
            setError("")
        }
    }

    function handleBack() {
        if (currentStep > 0) {
            setCurrentStep((prev) => prev - 1)
            setError("")
        }
    }

    return (
        <FormAuthBase
            title="Recuperação de Senha"
            subtitle="Sessão de recuperação de senha, siga os passos"
            typeForm=""
            form={
                <Tabs value={steps[currentStep]} onValueChange={() => {}}>
                    <TabsList className="grid w-full grid-cols-3">
                        {steps.map((step, index) => (
                            <TabsTrigger key={step} value={step} disabled>
                                {content[index].title}
                                {index < currentStep ? (
                                    <CheckCircle className="ml-2" />
                                ) : (
                                    <CircleAlert className="ml-2" />
                                )}
                            </TabsTrigger>
                        ))}
                    </TabsList>

                    {content.map((item, index) => (
                        <TabsContent key={item.title} value={steps[index]}>
                            <Card>
                                <CardHeader>
                                    <CardTitle>{item.title}</CardTitle>
                                    <CardDescription>
                                        {item.description}
                                    </CardDescription>
                                </CardHeader>
                                {item.form}
                            </Card>
                        </TabsContent>
                    ))}
                    {currentStep === steps.length && <ConfirmedPassword />}
                </Tabs>
            }
        />
    )
}

function FormEmail({ onNext, error }: { onNext: () => void; error: string }) {
    return (
        <>
            <CardContent className="space-y-2">
                <div className="space-y-1">
                    <Label htmlFor="email">E-mail</Label>
                    <Input id="email" />
                </div>
                {error && <p className="text-red-500">{error}</p>}
            </CardContent>
            <CardFooter className="flex justify-between">
                <Button disabled variant="outline">
                    <Undo2 /> Voltar
                </Button>
                <Button onClick={onNext}>
                    <Send /> Enviar e-mail
                </Button>
            </CardFooter>
        </>
    )
}

function FormValidation({
    onNext,
    onBack,
}: {
    onNext: () => void
    onBack: () => void
}) {
    return (
        <>
            <CardContent className="space-y-2">
                <div className="space-y-1">
                    <Label htmlFor="code">Código de validação</Label>
                    <Input id="code" />
                </div>
            </CardContent>
            <CardFooter className="flex justify-between">
                <Button variant="outline" onClick={onBack}>
                    <Undo2 /> Voltar
                </Button>
                <Button onClick={onNext}>
                    <CornerUpRight /> Avançar
                </Button>
            </CardFooter>
        </>
    )
}

function FormPassword({
    onNext,
    onBack,
}: {
    onNext: () => void
    onBack: () => void
}) {
    function validatePassword() {
        const novaSenha = (
            document.getElementById("nova-senha") as HTMLInputElement
        )?.value
        const confirmacaoSenha = (
            document.getElementById("confirmacao-senha") as HTMLInputElement
        )?.value

        if (!novaSenha || !confirmacaoSenha) {
            setupToast({
                id: "error1",
                status: "error",
                title: "Ocorreu um problema!",
                description: "Os campos de senha não podem estar vazios.",
            })
            return
        }

        if (novaSenha !== confirmacaoSenha) {
            setupToast({
                id: "error1",
                status: "error",
                title: "Ocorreu um problema!",
                description: "As senhas não coincidem.",
            })
            return
        }

        onNext()
    }

    return (
        <>
            <CardContent className="space-y-2">
                <div className="space-y-1">
                    <Label htmlFor="nova-senha">Nova senha</Label>
                    <Input id="nova-senha" type="password" />
                </div>
                <div className="space-y-1">
                    <Label htmlFor="confirmacao-senha">Confirmar senha</Label>
                    <Input id="confirmacao-senha" type="password" />
                </div>
            </CardContent>
            <CardFooter className="flex justify-between">
                <Button variant="outline" onClick={onBack}>
                    <Undo2 /> Voltar
                </Button>
                <Button onClick={validatePassword}>
                    <Save /> Salvar
                </Button>
            </CardFooter>
        </>
    )
}
