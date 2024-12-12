import { UsuarioInfoService } from "@/service/usuario-info"
import { AxiosResponse } from "axios"
import { useEffect, useState } from "react"

export const useUser = () => {
    const [userData, setUserData] = useState({
        name: "",
        surname: "",
        email: "",
        username: "",
        avatar: "/avatars/shadcn.jpg",
    })

    useEffect(() => {
        const fetchUserData = async () => {
            const service = new UsuarioInfoService()
            try {
                const response = await service.getInfoUsuario()
                const parsedData = handleResponse(response as AxiosResponse)
                setUserData(parsedData)
            } catch (error) {
                console.error("Failed to fetch user data", error)
            }
        }

        fetchUserData()
    }, [])

    return userData
}

function handleResponse(response: AxiosResponse) {
    const retorno = {
        name: "",
        surname: "",
        email: "",
        username: "",
        avatar: "/avatars/shadcn.jpg",
    }

    if (response.status === 200) {
        retorno["name"] = response.data.nome || ""
        retorno["surname"] = response.data.sobrenome || ""
        retorno["username"] = response.data.nome_usuario || ""
        retorno["email"] = response.data.email || ""
    }

    return retorno
}
