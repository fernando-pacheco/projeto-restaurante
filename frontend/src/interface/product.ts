export interface ProductProps {
    id: string
    tag: string
    name: string
    description: string
    fullDescription: string
    price: number
    newPrice?: number
    amount: number
}

export interface ProductItemProps {
    product: ProductProps
}
