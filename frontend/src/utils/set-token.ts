import Cookies from "js-cookie"

export function setToken(access_token: string) {
    Cookies.set("jwt_token", access_token, {
        secure: true,
        sameSite: "strict",
    })
}