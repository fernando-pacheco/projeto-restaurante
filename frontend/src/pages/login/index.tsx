import React, { useState } from 'react'
import loginClienteService from '@/service/login-cliente'
import Cookies from 'js-cookie'

export function Login() {
    const [nomeUsuario, setNomeUsuario] = useState('')
    const [senha, setSenha] = useState('')
    const [error, setError] = useState<string | null>(null)

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault()
        try {
            const response = await loginClienteService.obterToken(
                { 'nome_usuario': nomeUsuario, 'senha': senha }
            )
            const { access_token } = response?.data

            Cookies.set('jwt_token', access_token, { secure: true, sameSite: 'strict' })

            setError(null)
            alert('Login realizado com sucesso!')
        } catch (err) {
            setError('Credenciais inválidas')
        }
    }

    return (
        <div className="flex justify-center items-center h-screen">
            <form className="bg-zinc-700 p-8 shadow-md rounded" onSubmit={handleSubmit}>
                <h2 className="text-2xl font-bold mb-6">Login</h2>
                <div className="mb-4">
                    <label htmlFor="nome_usuario" className="block text-gray-200">Usuário</label>
                    <input
                        id="nome_usuario"
                        type="text"
                        value={nomeUsuario}
                        onChange={(e) => setNomeUsuario(e.target.value)}
                        className="w-full p-2 border rounded text-black"
                    />
                </div>
                <div className="mb-4">
                    <label htmlFor="senha" className="block text-gray-200">Senha</label>
                    <input
                        id="senha"
                        type="senha"
                        value={senha}
                        onChange={(e) => setSenha(e.target.value)}
                        className="w-full p-2 border rounded text-black"
                    />
                </div>
                {error && <p className="text-red-500 text-sm">{error}</p>}
                <button
                    type="submit"
                    className="w-full bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600"
                >
                    Entrar
                </button>
            </form>
        </div>
    )
}