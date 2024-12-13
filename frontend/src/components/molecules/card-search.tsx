import { ReactNode } from "react"
import { Separator } from "../atoms/separator"
import { ChevronRight } from "lucide-react"
import clsx from "clsx"

interface CardSearchProp {
    icon: ReactNode
    description: string
    variant?: "default" | "selected"
}

export function CardSearch({
    description,
    icon,
    variant = "default",
}: CardSearchProp) {
    const isSelected = variant === "selected"

    return (
        <div
            className={clsx(
                "flex flex-col justify-between items-center flex-1 w-32 h-52 rounded-xl py-6 border-salmon-500 border",
                {
                    "bg-zinc-50": !isSelected,
                    "bg-salmon-600": isSelected,
                },
            )}
        >
            <div className="flex flex-col items-center gap-2">
                <div
                    className={clsx("p-2", {
                        "rounded-full bg-salmon-50 ": isSelected,
                        "": !isSelected,
                    })}
                >
                    {icon}
                </div>
                <span
                    className={clsx("font-semibold", {
                        "text-salmon-50": isSelected,
                        "": !isSelected,
                    })}
                >
                    {description}
                </span>
            </div>
            <div className="flex flex-col gap-6 w-1/2 items-center">
                <Separator
                    className={clsx("border-2 rounded-full", {
                        "bg-salmon-600 border-salmon-600": !isSelected,
                        "bg-salmon-50 border-salmon-50": isSelected,
                    })}
                />
                <ChevronRight
                    className={clsx("rounded-full size-6 p-0.5", {
                        "bg-salmon-600 text-salmon-50": !isSelected,
                        "bg-salmon-50 text-salmon-600": isSelected,
                    })}
                />
            </div>
        </div>
    )
}
