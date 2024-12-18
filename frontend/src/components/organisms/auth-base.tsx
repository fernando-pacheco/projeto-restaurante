import { ReactNode } from "react"
import { HeaderBase } from "../molecules/header-base"

interface AuthBaseProps {
    children: ReactNode
}

export function AuthBase({ children }: AuthBaseProps) {
    return (
        <div className="relative flex items-center min-h-screen w-screen bg-gradient-to-b from-salmon-50 to bg-salmon-700/15 pl-12 overflow-hidden">
            <div className="absolute left-10 top-6">
                <HeaderBase />
            </div>
            {children}
            <div className="absolute inset-0 -z-10">
                <div className="border-4 border-salmon-900/10 w-[800px] h-[800px] rounded-full absolute bottom-1/2 left-10 z-0" />
                <div className="border-2 border-salmon-950/10 w-[800px] h-[800px] rounded-full absolute bottom-1/2 left-10 z-0" />
                <div className="border-4 border-salmon-900/10 w-[800px] h-[800px] rounded-full absolute top-36 -left-24 z-0" />
                <div className="border-2 border-salmon-950/10 w-[800px] h-[800px] rounded-full absolute top-36 -left-24 z-0" />
                <div className="border-4 border-salmon-900/10 w-[800px] h-[800px] rounded-full absolute top-40 -left-16 z-0" />
                <div className="border-2 border-salmon-950/10 w-[800px] h-[800px] rounded-full absolute top-40 -left-16 z-0" />
                <div className="bg-gradient-to-b from-salmon-700/5 to-salmon-700/15 w-[1000px] h-[1000px] rounded-full absolute bottom-16 -right-40" />
                <div className="bg-gradient-to-t from-salmon-700/5 to-salmon-700/5 w-[2000px] h-[2000px] rounded-full absolute top-96 left-4" />
            </div>
            <div className="flex flex-1 justify-center h-screen w-full items-center">
                <img
                    alt="img-fundo"
                    src="static/fundo-login.png"
                    className="absolute bottom-8 right-[500px] z-10"
                    width={350}
                />
                <img
                    alt="img-fundo1"
                    src="static/fundo-login1.png"
                    className="absolute top-20 right-28"
                    width={800}
                />
            </div>
        </div>
    )
}
