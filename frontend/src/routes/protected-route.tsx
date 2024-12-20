import { getToken } from "@/utils/token"
import { Navigate } from "react-router-dom"

export function ProtectedRoute({ children }: { children: React.ReactNode }) {
    if (!getToken()) {
        return <Navigate to="/" replace />
    }
    return <>{children}</>
}
