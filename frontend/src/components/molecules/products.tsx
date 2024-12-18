import { productItens } from "@/utils/product-itens"
import { ProductItem } from "./product-item"

interface ProductsProps {
    tag: string
}

export function Products({ tag }: ProductsProps) {
    return (
        <div>
            <div className="grid grid-cols-3 gap-4">
                {productItens
                    .filter((product) => product.tag === tag)
                    .map((product) => (
                        <ProductItem key={product.id} product={product} />
                    ))}
            </div>
        </div>
    )
}
