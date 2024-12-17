import { productItens } from "@/utils/product-itens"
import { ProductItem } from "./product-item"

interface ProductsProps {
    tag: string
}

export function Products({ tag }: ProductsProps) {
    return (
        <div>
            <div className="grid grid-cols-3 gap-4">
                {productItens.map((product) => (
                    <>
                        {product.tag === tag && (
                            <ProductItem product={product} />
                        )}
                    </>
                ))}
            </div>
        </div>
    )
}
