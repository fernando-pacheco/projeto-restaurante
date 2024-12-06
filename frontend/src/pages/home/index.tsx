import { Button } from "@/components/molecules/button"
import { useState } from "react"
import { InfosUsuarioProps } from "@/service/interface/infos-usuario-interface"
import { UsuarioInfoService } from "@/service/usuario-info"

export function Home() {
    const [infosUsuario, setInfosUsuario] = useState<InfosUsuarioProps | null>(
        null
    )

    async function obterInfosUsuario() {
        const service = new UsuarioInfoService()
        const response = await service.getInfoUsuario()
        if (response && response.data) {
            setInfosUsuario(response.data)
        } else {
            console.error("Nenhum dado retornado.")
        }
    }

    return (
        <div className="space-y-4">
            <h1>Página principal da aplicação</h1>
            <Button onClick={obterInfosUsuario} variant={"primary"}>
                Obter informações do usuário
            </Button>
        </div>
    )
}
