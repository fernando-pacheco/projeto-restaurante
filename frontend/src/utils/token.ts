import Cookies from "js-cookie"

let tokenTimeout: NodeJS.Timeout | null = null

export function setToken(access_token: string, expiresIn: number) {
    Cookies.set("jwt_token", access_token, {
        sameSite: "strict",
        secure: true,
    })

    if (tokenTimeout) {
        clearTimeout(tokenTimeout)
    }

    tokenTimeout = setTimeout(() => {
        revokeToken()
        window.location.reload()
    }, expiresIn * 1000)
}

export function revokeToken() {
    if (tokenTimeout) {
        clearTimeout(tokenTimeout)
    }
    Cookies.remove("jwt_token", {
        sameSite: "strict",
        secure: true,
    })
}

export function getToken() {
    return Cookies.get("jwt_token")
}
