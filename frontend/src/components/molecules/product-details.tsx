import { ProductItemProps } from "@/interface/product"

export function ProductDetails({ product }: ProductItemProps) {
    return (
        <div>
            <span>{product.name}</span>
        </div>
    )
}
