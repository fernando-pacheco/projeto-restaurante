import { Routes, Route } from "react-router-dom"
import { Toaster } from "sonner"
import { LandingPage } from "./pages/landing-page"
import { Login } from "./pages/auth/login"
import { Home } from "./pages/home"
import { RegisterCliente } from "./pages/auth/register/cliente"
import { PasswordRecovery } from "./pages/auth/password-recovery"
import { X } from "lucide-react"

export function App() {
    return (
        <div>
            <Toaster
                icons={{
                    error: (
                        <X className="rounded-full bg-[#ed3615] size-4 text-salmon-50 p-0.5" />
                    ),
                }}
            />
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
