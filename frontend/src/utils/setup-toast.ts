import { toast } from "sonner"

interface SetupToastProps {
    id: string
    title: string
    description: string
    status: "success" | "error" | "info"
}

export function setupToast({
    id,
    title,
    description,
    status,
}: SetupToastProps) {
    const baseToastConfig = {
        id: id,
        description: description,
        duration: 5000,
        className: "custom-toast",
        action: {
            label: "Fechar",
            onClick: () => {},
        },
    }

    const statusStyles = {
        success: {
            style: {
                backgroundColor: "#f",
                color: "#1f911d",
                border: "3px solid #8fe88d",
            },
        },
        error: {
            style: {
                backgroundColor: "#f",
                color: "#ed3615",
                border: "3px solid #ff7c64",
            },
        },
        info: {
            style: {
                backgroundColor: "#f",
                color: "#0288d1",
                border: "3px solid #bbdefb",
            },
        },
    }

    return toast[status](title, {
        ...baseToastConfig,
        ...statusStyles[status],
    })
}
