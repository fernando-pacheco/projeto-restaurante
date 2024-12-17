import { cart } from "@/utils/cart"
import { ProductProps } from "@/interface/product"
import { CartItem } from "./cart-item"

export function Cart() {
    const sum = cart.reduce((total, item) => conditionalCartSum(total, item), 0)

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
        <div className="flex flex-col gap-8">
            <span className="text-4xl font-semibold">Meu Carrinho</span>
            <div className="flex flex-col gap-4">
                {cart.map((product) => (
                    <div>
                        <CartItem product={product} />
                    </div>
                ))}
            </div>
            <div>
                <div>Total: R$ {sum.toFixed(2)}</div>
            </div>
        </div>
    )
}
