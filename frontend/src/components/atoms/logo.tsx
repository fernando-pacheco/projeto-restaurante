import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const logoVariants = cva("inline-block transition-all", {
    variants: {
        size: {
            sm: "w-8 h-8",
            md: "w-16 h-16",
            lg: "w-24 h-24",
            xl: "w-32 h-32",
        },
        shape: {
            square: "rounded-none",
            rounded: "rounded-lg",
            circle: "rounded-full",
        },
    },
    defaultVariants: {
        shape: "square",
    },
})

export interface LogoProps
    extends React.ImgHTMLAttributes<HTMLImageElement>,
        VariantProps<typeof logoVariants> {
    asChild?: boolean
}

const Logo = React.forwardRef<HTMLImageElement, LogoProps>(
    ({ className, size, shape, asChild = false, ...props }, ref) => {
        const Comp = asChild ? Slot : "img"
        return (
            <Comp
                className={cn(logoVariants({ size, shape, className }))}
                ref={ref}
                {...props}
            />
        )
    },
)
Logo.displayName = "Logo"

export { Logo, logoVariants }
