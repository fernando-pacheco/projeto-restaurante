import { ReactNode } from "react"

interface AuthBaseProps {
    children: ReactNode
}

export function AuthBase({ children }: AuthBaseProps) {
    return (
        <div className="relative flex items-center min-h-screen w-screen bg-gradient-to-b from-salmon-50 to bg-salmon-700/15 pl-12 overflow-hidden">
            <div className="absolute inset-0 -z-10">
                <circle className="border-4 border-salmon-900/10 w-[800px] h-[800px] rounded-full absolute bottom-1/2 -left-16 z-0" />
                <circle className="border-2 border-salmon-950/10 w-[800px] h-[800px] rounded-full absolute bottom-1/2 -left-16 z-0" />
                <circle className="border-4 border-salmon-900/10 w-[800px] h-[800px] rounded-full absolute top-36 -left-24 z-0" />
                <circle className="border-2 border-salmon-950/10 w-[800px] h-[800px] rounded-full absolute top-36 -left-24 z-0" />
                <circle className="border-4 border-salmon-900/10 w-[800px] h-[800px] rounded-full absolute top-40 -left-16 z-0" />
                <circle className="border-2 border-salmon-950/10 w-[800px] h-[800px] rounded-full absolute top-40 -left-16 z-0" />
                <circle className="bg-gradient-to-b from-salmon-700/5 to-salmon-700/15 w-[1000px] h-[1000px] rounded-full absolute bottom-16 -right-40" />
                <circle className="bg-gradient-to-t from-salmon-700/5 to-salmon-700/5 w-[2000px] h-[2000px] rounded-full absolute top-96 left-4" />
            </div>
            {children}
            <div className="flex flex-1 justify-center h-screen w-full items-center">
                <img
                    alt="img-fundo"
                    src="static/fundo-login.png"
                    className="absolute bottom-8 right-[410px] z-10"
                    width={250}
                />
                <img
                    alt="img-fundo1"
                    src="static/fundo-login1.png"
                    className="absolute top-10 right-16"
                    width={650}
                />
            </div>
        </div>
    )
}
