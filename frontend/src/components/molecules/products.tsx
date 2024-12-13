import { productItens } from "@/utils/product-itens"
import { ProductItem } from "./product-item"

interface ProductsProps {
    tag: string
}

export function Products({ tag }: ProductsProps) {
    return (
        <div>
            {productItens.map((product) => (
                <div>
                    {product.tag === tag && <ProductItem product={product} />}
                </div>
            ))}
        </div>
    )
}
