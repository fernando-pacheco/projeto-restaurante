import { useUser } from "@/hooks/use-user"
import { Crown } from "lucide-react"
import { useNavigate } from "react-router-dom"
import { Button } from "../atoms/button"

export function MainCard() {
    const navigate = useNavigate()
    const { isAuthenticated, userData } = useUser()

    return (
        <div className="grid grid-cols-3 gap-8 drop-shadow-lg">
            <div className="relative flex justify-center col-span-2 items-center bg-zinc-200 rounded-lg overflow-hidden">
                <img
                    alt="greeting-img"
                    src="static/greetings-bg.png"
                    className="rounded-lg object-cover w-full h-full"
                />
                <div className="absolute inset-16 flex flex-col justify-between items-start">
                    <span className="text-salmon-500 text-md flex gap-2">
                        <Crown className="fill-salmon-400" />
                        Oferta do fim de semana
                    </span>
                    {isAuthenticated ? (
                        <span className="text-salmon-950 text-4xl font-bold">
                            Olá, {userData.name} {userData.surname || ""}!
                        </span>
                    ) : (
                        <div className="flex flex-col">
                            <span className="text-salmon-950 text-4xl font-bold">
                                Seja bem-vindo(a),
                            </span>
                            <span className="text-salmon-950 text-xl font-bold">
                                faça seu cadastro para aproveitar nossas
                                promoções.
                            </span>
                        </div>
                    )}
                    <span className="text-zinc-500">
                        Obtenha{" "}
                        <strong className="text-salmon-500">
                            entrega GRATUITA
                        </strong>{" "}
                        todos os finais de semana.
                    </span>
                    {isAuthenticated ? (
                        <Button variant={"flat"}>Ver menu</Button>
                    ) : (
                        <Button
                            variant={"flat"}
                            onClick={() => navigate("/register")}
                        >
                            Registre-se
                        </Button>
                    )}
                </div>
            </div>
            <div className="relative flex flex-col items-center bg-gradient-to-b from-transparent to-white rounded-lg p-8">
                <div className="flex w-full max-w-[300px] flex-1">
                    <img
                        alt="hb"
                        src="static/burger.png"
                        className="relative w-full h-full object-cover pb-10 -top-4"
                    />
                    <div className="absolute inset-4 flex flex-col items-center justify-end gap-4 mb-6">
                        <span className="text-3xl font-semibold text-salmon-800">
                            30% de desconto
                        </span>
                        <span className="text-xl">
                            Na sua primeira compra no restaurante
                        </span>
                    </div>
                </div>
            </div>
        </div>
    )
}
