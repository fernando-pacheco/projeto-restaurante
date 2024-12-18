import { cart } from "@/utils/cart"
import { ProductProps } from "@/interface/product"
import { CartItem } from "../molecules/cart-item"
import { priceFormat } from "@/utils/price-format"
import { Separator } from "../atoms/separator"

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
        <div className="flex flex-col gap-8 flex-1">
            <span className="text-4xl font-semibold">Meu Carrinho</span>
            <div className="max-h-[600px] overflow-x-auto">
                {cart.length > 0 && (
                    <>
                        <div className="flex flex-col gap-4">
                            {cart.map((product) => (
                                <div>
                                    <CartItem
                                        key={product.id}
                                        product={product}
                                    />
                                </div>
                            ))}
                        </div>
                        <Separator className="border-2 rounded-full border-salmon-500 mb-4 mt-6" />
                        <div className="flex-1 px-2 font-semibold">
                            <div className="flex justify-between">
                                <div>Subtotal:</div>
                                <div>{priceFormat(sum)}</div>
                            </div>
                            <div className="flex justify-between">
                                <div>Taxa de entrega:</div>
                                <div>{priceFormat(2)}</div>
                            </div>
                            <Separator className="border-2 rounded-full border-salmon-500 my-4" />
                            <div className="flex justify-between">
                                <div className="font-bold text-2xl">Total:</div>
                                <div className="font-bold text-2xl">
                                    {priceFormat(sum + 2)}
                                </div>
                            </div>
                        </div>
                    </>
                )}
            </div>
        </div>
    )
}
