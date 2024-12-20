import { getToken } from "@/utils/token"
import { Navigate } from "react-router-dom"

export function AuthRedirectedRoute({
    children,
}: {
    children: React.ReactNode
}) {
    if (getToken()) {
        return <Navigate to="/home" replace />
    }
    return <>{children}</>
}
