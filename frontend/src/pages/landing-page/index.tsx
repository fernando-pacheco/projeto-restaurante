import { Button } from "@/components/atoms/button"
import { Catalog } from "@/components/organisms/catalog"
import { LogIn, Pencil } from "lucide-react"
import { useNavigate } from "react-router-dom"

export function LandingPage() {
    const navigate = useNavigate()

    return (
        <div className="h-screen flex flex-col px-24">
            <header className="flex justify-between py-6">
                <div className="flex space-x-6">
                    <div>Logo</div>
                    <div>Restaurantes</div>
                    <div>Seja Parceiro</div>
                    <div>Fale conosco</div>
                </div>
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
            <body>
                <Catalog />
            </body>
            <footer className="flex py-6 justify-center">Footer</footer>
        </div>
    )
}
