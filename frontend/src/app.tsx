import { Routes, Route } from "react-router-dom"
import { Toaster } from "sonner"
import { LandingPage } from "./pages/landing-page"
import { Login } from "./pages/auth/login"
import { Home } from "./pages/home"
import { RegisterCliente } from "./pages/auth/register/cliente"
import { PasswordRecovery } from "./pages/auth/password-recovery"

export function App() {
    return (
        <div>
            <Toaster />
            <Routes>
                <Route path="/" element={<LandingPage />} />
                <Route path="/login" element={<Login />} />
                <Route path="/home" element={<Home />} />
                <Route path="/register" element={<RegisterCliente />} />
                <Route
                    path="/password-recovery"
                    element={<PasswordRecovery />}
                />
            </Routes>
        </div>
    )
}
