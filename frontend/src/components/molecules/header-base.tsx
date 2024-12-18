import { useNavigate } from "react-router-dom"
import { Logo } from "../atoms/logo"

export function HeaderBase() {
    const navigate = useNavigate()

    return (
        <div className="flex space-x-6 items-center">
            <button onClick={() => navigate("/")}>
                <Logo alt="team-logo" src="static/ks-logo.png" size="md" />
            </button>
            <div>Restaurantes</div>
            <div>Seja Parceiro</div>
            <div>Fale conosco</div>
        </div>
    )
}
