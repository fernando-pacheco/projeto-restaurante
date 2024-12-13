interface ProductProps {
    id: string
    tag: string
    name: string
    description: string
    price: number
    newPrice?: number
}

interface ProductItemProps {
    product: ProductProps
}

export function ProductItem({ product }: ProductItemProps) {
    return (
        <div className="flex">
            <span>{product.name}</span>
            <span>{product.tag}</span>
            <span>{product.price}</span>
        </div>
    )
}
