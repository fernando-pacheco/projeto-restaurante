import * as React from "react"

import { cn } from "@/lib/utils"

const Input = React.forwardRef<HTMLInputElement, React.ComponentProps<"input">>(
    ({ className, type, ...props }, ref) => {
        return (
            <input
                type={type}
                className={cn(
                    "flex h-10 w-full rounded-md border border-salmon-700 bg-white px-3 py-2 text-base ring-offset-white file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-salmon-800 placeholder:text-salmon-900/50 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-salmon-800 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 md:text-sm dark:border-salmon-800 dark:bg-salmon-950 dark:ring-offset-salmon-950 dark:file:text-salmon-50 dark:placeholder:text-salmon-400 dark:focus-visible:ring-salmon-300",
                    className,
                )}
                ref={ref}
                {...props}
            />
        )
    },
)
Input.displayName = "Input"

export { Input }
