import { toast } from "sonner"

interface SetupToastProps {
    status: "success" | "error" | "info"
    title: string
    description: string
}

export function setupToast({ status, title, description }: SetupToastProps) {
    const baseToastConfig = {
        description,
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
                color: "green",
                border: "1px solid #fbd4c4",
            },
        },
        error: {
            style: {
                backgroundColor: "#f",
                color: "#ed3615",
                border: "1px solid #fbd4c4",
            },
        },
        info: {
            style: {
                backgroundColor: "#e3f2fd",
                color: "#0288d1",
                border: "1px solid #bbdefb",
            },
        },
    }

    return toast[status](title, {
        ...baseToastConfig,
        ...statusStyles[status],
    })
}
