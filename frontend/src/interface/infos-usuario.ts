interface TelefoneUsuarioProps {
    id: number
    numero: string
    principal: boolean
}

interface EmpresaFuncionarioProps {
    cnpj: string
    id: string
    razao_social: string
    status: boolean
}

interface FuncaoFuncionarioProps {
    funcao_id: 0
    id: 0
}

interface EnderecoUsuarioProps {
    id: string
    logradouro: string
    numero: number
    bairro: string
    cidade: string
    estado: string
    cep: string
    complemento: string
    principal: boolean
}

export interface InfosUsuarioProps {
    ativo: boolean
    cpf: string
    email: string
    empresa: EmpresaFuncionarioProps
    funcoes: FuncaoFuncionarioProps[]
    id: string
    nome: string
    nome_usuario: string
    sobrenome: string
    telefones: TelefoneUsuarioProps[]
    enderecos: EnderecoUsuarioProps[]
}

export interface UserDataProps {
    name: string
    surname: string
    email: string
    username: string
    avatar: string
}
