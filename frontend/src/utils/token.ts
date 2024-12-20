import Cookies from "js-cookie"

let tokenTimeout: NodeJS.Timeout | null = null

export function setToken(access_token: string, expiresIn: number) {
    Cookies.set("jwt_token", access_token, {
        sameSite: "strict",
        secure: true,
    })

    clearTokenTimeout()

    tokenTimeout = setTimeout(() => {
        revokeToken()
        window.location.reload()
    }, expiresIn * 1000)
}

export function revokeToken() {
    clearTokenTimeout()

    Cookies.remove("jwt_token", {
        sameSite: "strict",
        secure: true,
    })
}

export function getToken() {
    return Cookies.get("jwt_token")
}

function clearTokenTimeout() {
    if (tokenTimeout) {
        clearTimeout(tokenTimeout)
    }
}
