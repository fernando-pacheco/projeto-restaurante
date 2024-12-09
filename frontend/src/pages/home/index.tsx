import { useState } from "react"
import { InfosUsuarioProps } from "@/service/interface/infos-usuario-interface"
import { UsuarioInfoService } from "@/service/usuario-info"
import { LayoutHome } from "@/components/organisms/layout-home"

export function Home() {
    const [infosUsuario, setInfosUsuario] = useState<InfosUsuarioProps | null>(
        null,
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
        <LayoutHome>
            <div>helloworld</div>
        </LayoutHome>
    )
}
