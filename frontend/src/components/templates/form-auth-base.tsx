import { ReactNode } from "react"
import { AuthBase } from "../organisms/auth-base"
import { LucideOctagon } from "lucide-react"
import { BrandGoogleSolid, TelephoneSolid } from "@mynaui/icons-react"
import { Button } from "../atoms/button"

interface FormAuthBaseProps {
    title: string
    subtitle: string
    form: ReactNode
    typeForm: "register" | "login" | ""
    greetings?: string
    footerForm?: ReactNode
    loginGoogle?: () => void
    loginPhone?: () => void
}

export function FormAuthBase({
    form,
    footerForm,
    greetings,
    title,
    subtitle,
    typeForm,
    loginPhone,
    loginGoogle,
}: FormAuthBaseProps) {
    const nameForm = {
        register: "Cadastrar com o telefone",
        login: "Entrar com o telefone",
    }

    return (
        <AuthBase>
            <div className="px-24 rounded-l-xl h-full min-w-80 w-[800px] z-50">
                <div className="h-[64px] w-[64px] mb-2">
                    <LucideOctagon width={64} height={64} />
                </div>
                {greetings && (
                    <h1 className="text-3xl font-semibold mb-8">{greetings}</h1>
                )}
                <h1 className="text-2xl font-semibold flex justify-center">
                    {title}
                </h1>
                <h1 className="text-md font-semibold mb-4 flex justify-center text-salmon-950/40">
                    {subtitle}
                </h1>
                {form}
                {typeForm && (
                    <>
                        <div className="flex items-center mt-4 flex-1 space-x-2">
                            <div className="flex-grow h-px bg-salmon-950"></div>
                            <span className="text-md">ou</span>
                            <div className="flex-grow h-px bg-salmon-950"></div>
                        </div>
                        <div className="flex justify-around space-x-4 mt-4">
                            <Button
                                className="w-full"
                                variant="primary"
                                onClick={loginGoogle}
                            >
                                <BrandGoogleSolid />
                                {nameForm[typeForm]}
                            </Button>
                            <Button
                                className="w-full"
                                variant="primary"
                                onClick={loginPhone}
                            >
                                <TelephoneSolid />
                                {nameForm[typeForm]}
                            </Button>
                        </div>
                    </>
                )}
                {footerForm}
            </div>
        </AuthBase>
    )
}
