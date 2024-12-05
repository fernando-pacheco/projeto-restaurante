import { Button } from "@/components/molecules/button";

export function Home() {

    return (
        <div>
            <h1>Página principal da aplicação</h1>
            <Button
                className="bg-sky-800 hover:"
            >
                Obter informações do usuário
            </Button>
        </div>
    )
}