import { dataSearch } from "@/utils/label-search"
import { CardSearch } from "../molecules/card-search"
import { Crown } from "lucide-react"
import { useUser } from "@/hooks/use-user"
import { Button } from "../atoms/button"
import { useNavigate } from "react-router-dom"

export function Catalog() {
    const { isAuthenticated, userData } = useUser()
    const navigate = useNavigate()

    return (
        <div className="w-full">
            <div className="flex gap-8 flex-col">
                <div className="grid grid-cols-3 gap-8">
                    <div className="relative flex justify-center col-span-2 items-center bg-zinc-200 rounded-lg overflow-hidden drop-shadow-lg">
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
                                    Olá, {userData.name}{" "}
                                    {userData.surname || ""}!
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
                    <div className="relative flex flex-col items-center bg-gradient-to-b from-transparent via-white to-white rounded-lg drop-shadow-lg p-8">
                        <div className="flex w-full max-w-[350px] flex-1">
                            <img
                                alt="hb"
                                src="static/burger.png"
                                className="relative w-full h-full object-cover pb-10 -top-4"
                            />
                            <div className="absolute inset-4 flex flex-col items-center justify-end gap-4 mb-8">
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
                <div className="flex items-center justify-center px-16 overflow-x-auto [&::-webkit-scrollbar]:hidden gap-8 pb-4">
                    {dataSearch.map((item, index) => {
                        if (index <= 6) {
                            return (
                                <CardSearch
                                    key={item.description}
                                    description={item.description}
                                    icon={<item.icon className="size-10" />}
                                />
                            )
                        }
                    })}
                </div>
                <div className="w-full h-[1000px] bg-black"></div>
            </div>
        </div>
    )
}
