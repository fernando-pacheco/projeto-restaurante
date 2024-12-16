import { productsList } from "@/utils/products-list"
import { ProductItem } from "./product-item"
import { ProductProps } from "@/interface/product"

export function Cart() {
    const sum = productsList.reduce(
        (total, item) => conditionalCartSum(total, item),
        0,
    )

    function conditionalCartSum(total: number, item: ProductProps) {
        let productValue = item.price

        if (item.newPrice) {
            productValue = item.newPrice
        }

        if (!item.amount) {
            item.amount = 0
        }

        return total + item.amount * productValue
    }

    return (
        <div className="flex flex-col gap-4">
            <div>
                {productsList.map((product) => (
                    <div>
                        <ProductItem product={product} />
                    </div>
                ))}
            </div>
            <div>
                <div>total: {sum}</div>
            </div>
        </div>
    )
}
