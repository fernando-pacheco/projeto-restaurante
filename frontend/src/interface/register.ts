export interface RegisterClienteProps {
    cpf: string
    email: string
    nome: string
    nome_usuario: string
    senha: string
    sobrenome?: string
}

export interface RegisterFuncionarioProps {
    cpf: string
    email: string
    empresa_id: string
    nome: string
    nome_usuario: string
    senha: string
    sobrenome?: string
}

export interface RegisterEmpresaProps {
    cnpj: string
    nome: string
    razao_social: string
}
