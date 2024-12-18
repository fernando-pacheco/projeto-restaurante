import { UsuarioInfoService } from "@/service/usuario-info"
import { AxiosResponse } from "axios"
import { useEffect, useState } from "react"

const userState = {
    name: "",
    surname: "",
    email: "",
    username: "",
    avatar: "/avatars/shadcn.jpg",
}

export function useUser() {
    const [userData, setUserData] = useState(userState)
    const [isAuthenticated, setIsAuthenticated] = useState(false)

    useEffect(() => {
        const fetchUserData = async () => {
            const service = new UsuarioInfoService()
            try {
                const response = await service.getInfoUsuario()
                const parsedData = handleResponse(response as AxiosResponse)
                setUserData(parsedData)
                setIsAuthenticated(!!parsedData.email || !!parsedData.username)
            } catch (error) {
                console.error("Failed to fetch user data", error)
                setIsAuthenticated(false)
            }
        }

        fetchUserData()
    }, [])

    return { userData, isAuthenticated }
}

function handleResponse(response: AxiosResponse) {
    const retorno = userState

    if (response.status === 200) {
        retorno["name"] = response.data.nome || ""
        retorno["surname"] = response.data.sobrenome || ""
        retorno["username"] = response.data.nome_usuario || ""
        retorno["email"] = response.data.email || ""
    }

    return retorno
}
