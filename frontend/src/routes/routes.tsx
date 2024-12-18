import { Routes, Route } from "react-router-dom"
import { Toaster } from "sonner"
import { X } from "lucide-react"
import { LandingPage } from "@/pages/landing-page"
import { Login } from "@/pages/auth/login"
import { RegisterCliente } from "@/pages/auth/register/cliente"
import { PasswordRecovery } from "@/pages/auth/password-recovery"
import { ProtectedRoute } from "./protected-route"
import { Home } from "@/pages/home"
import { AuthRedirectedRoute } from "./auth-redirected"

export function AppRoutes() {
    return (
        <div>
            <Routes>
                <Route
                    path="/"
                    element={
                        <AuthRedirectedRoute>
                            <LandingPage />
                        </AuthRedirectedRoute>
                    }
                />
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<RegisterCliente />} />
                <Route
                    path="/password-recovery"
                    element={<PasswordRecovery />}
                />
                <Route
                    path="/home"
                    element={
                        <ProtectedRoute>
                            <Home />
                        </ProtectedRoute>
                    }
                />
            </Routes>
        </div>
    )
}
