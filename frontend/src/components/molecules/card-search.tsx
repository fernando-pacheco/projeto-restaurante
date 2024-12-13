import { ReactNode } from "react"
import { Card, CardContent, CardDescription } from "../atoms/card"

interface CardSearchProp {
    icon: ReactNode
    description: string
}

export function CardSearch({ description, icon }: CardSearchProp) {
    return (
        <Card className="bg-zinc-50">
            <button>
                <CardContent className="flex flex-col justify-between items-center flex-1 w-36 h-28 p-5">
                    {icon}
                    <CardDescription>{description}</CardDescription>
                </CardContent>
            </button>
        </Card>
    )
}
