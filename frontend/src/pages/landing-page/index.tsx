import { Button } from "@/components/atoms/button"
import { Catalog } from "@/components/templates/catalog"
import { HeaderBase } from "@/components/molecules/header-base"
import { LogIn, Pencil } from "lucide-react"
import { useNavigate } from "react-router-dom"

export function LandingPage() {
    const navigate = useNavigate()

    return (
        <div className="h-full flex flex-col px-10">
            <header className="flex justify-between py-6">
                <HeaderBase />
                <div className="flex space-x-6 items-center">
                    <Button
                        onClick={() => navigate("/register")}
                        variant="secondary"
                    >
                        <Pencil />
                        Registre-se
                    </Button>
                    <Button
                        onClick={() => navigate("/login")}
                        variant="primary"
                    >
                        <LogIn />
                        Entrar
                    </Button>
                </div>
            </header>
            <div>
                <Catalog />
            </div>
            <footer className="flex py-6 justify-center">Footer</footer>
        </div>
    )
}
