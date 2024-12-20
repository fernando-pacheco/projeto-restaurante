import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const buttonVariants = cva(
    "inline-flex items-center justify-center gap-2 whitespace-nowrap text-sm font-medium ring-offset-white transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-zinc-950 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 dark:ring-offset-zinc-950 dark:focus-visible:ring-zinc-300",
    {
        variants: {
            variant: {
                default:
                    "bg-salmon-900 text-salmon-50 hover:bg-salmon-900/90 dark:bg-salmon-50 dark:text-salmon-900 dark:hover:bg-salmon-50/90",
                destructive:
                    "bg-salmon-500 text-zinc-50 hover:bg-salmon-500/90 dark:bg-salmon-900 dark:text-zinc-50 dark:hover:bg-salmon-900/90",
                outline:
                    "border border-salmon-400 bg-salmon-50 hover:bg-salmon-100 hover:text-salmon-950 dark:border-salmon-800 dark:bg-salmon-950 dark:hover:bg-salmon-800 dark:hover:text-salmon-50",
                secondary:
                    "bg-gradient-to-b from-zinc-500 to-zinc-700 text-zinc-50 hover:to-zinc-800 active:to-zinc-950 shadow-md dark:bg-zinc-100 dark:text-zinc-800 dark:hover:bg-zinc-100/80 rounded-lg",
                ghost: "hover:bg-salmon-100 hover:text-salmon-900 dark:hover:bg-salmon-800 dark:hover:text-salmon-50",
                link: "text-salmon-600 hover:underline hover:text-salmon-700",
                search: "rounded-l-lg border border-l-salmon-700 border-t-salmon-700 border-b-salmon-700",
                primary:
                    "bg-gradient-to-b from-salmon-500 to-salmon-600 text-zinc-50 py-2 px-4 rounded-lg hover:to-salmon-700 shadow-md active:to-salmon-900",
                flat: "bg-salmon-500 text-salmon-50 rounded-lg hover:bg-salmon-600 active:bg-salmon-700",
            },
            size: {
                default: "h-10 px-4 py-2",
                sm: "h-9 rounded-md px-3",
                xs: "h-6 rounded-md px-1",
                lg: "h-11 rounded-md px-8",
                icon: "h-10 w-10",
                clean: "",
            },
        },
        defaultVariants: {
            variant: "primary",
            size: "default",
        },
    },
)

export interface ButtonProps
    extends React.ButtonHTMLAttributes<HTMLButtonElement>,
        VariantProps<typeof buttonVariants> {
    asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
    ({ className, variant, size, asChild = false, ...props }, ref) => {
        const Comp = asChild ? Slot : "button"
        return (
            <Comp
                className={cn(buttonVariants({ variant, size, className }))}
                ref={ref}
                {...props}
            />
        )
    },
)
Button.displayName = "Button"

export { Button, buttonVariants }
