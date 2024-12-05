import { Routes, Route } from "react-router-dom"
import { Login } from "./pages/login"
import { LandingPage } from "./pages/landing-page"
import { Home } from "./pages/home"

export function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/home" element={<Home />} />
      </Routes>
    </div>
  )
}
