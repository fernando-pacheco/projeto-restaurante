import { Routes, Route } from "react-router-dom"
import { Login } from "./pages/login"
import { LandingPage } from "./pages/landing-page"
import { Home } from "./pages/home"
import { Toaster } from "sonner"
import { RegisterCliente } from "./pages/register/cliente"

export function App() {
    return (
        <div>
            <Toaster />
            <Routes>
                <Route path="/" element={<LandingPage />} />
                <Route path="/login" element={<Login />} />
                <Route path="/home" element={<Home />} />
                <Route path="/register" element={<RegisterCliente />} />
            </Routes>
        </div>
    )
}
