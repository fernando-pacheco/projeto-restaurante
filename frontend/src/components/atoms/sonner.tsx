import { useTheme } from "next-themes"
import { Toaster as Sonner } from "sonner"

type ToasterProps = React.ComponentProps<typeof Sonner>

const Toaster = ({ ...props }: ToasterProps) => {
    const { theme = "system" } = useTheme()

    return (
        <Sonner
            theme={theme as ToasterProps["theme"]}
            className="toaster group"
            toastOptions={{
                classNames: {
                    toast: "group toast group-[.toaster]:bg-white group-[.toaster]:text-salmon-950 group-[.toaster]:border-salmon-200 group-[.toaster]:shadow-lg dark:group-[.toaster]:bg-salmon-950 dark:group-[.toaster]:text-salmon-50 dark:group-[.toaster]:border-salmon-800",
                    description:
                        "group-[.toast]:text-salmon-500 dark:group-[.toast]:text-salmon-400",
                    actionButton:
                        "group-[.toast]:bg-salmon-900 group-[.toast]:text-salmon-50 dark:group-[.toast]:bg-salmon-50 dark:group-[.toast]:text-salmon-900",
                    cancelButton:
                        "group-[.toast]:bg-salmon-100 group-[.toast]:text-salmon-500 dark:group-[.toast]:bg-salmon-800 dark:group-[.toast]:text-salmon-400",
                },
            }}
            {...props}
        />
    )
}

export { Toaster }
