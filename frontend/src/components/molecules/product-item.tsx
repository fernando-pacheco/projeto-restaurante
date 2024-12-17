import { ProductItemProps, ProductProps } from "@/interface/product"
import { cart } from "@/utils/cart"
import { ChevronDownCircle, Minus, Plus, ShoppingCart } from "lucide-react"
import { useState } from "react"
import { Button } from "../atoms/button"
import { priceFormat } from "@/utils/price-format"

export function ProductItem({ product }: ProductItemProps) {
    const [countItem, setCountItem] = useState<number>(0)

    function removeItem() {
        if (countItem === 0) {
            setCountItem(countItem)
        } else {
            setCountItem(countItem - 1)
        }
    }

    function addItem() {
        setCountItem(countItem + 1)
    }

    function addToCart(product: ProductProps) {
        product["amount"] = countItem
        cart.push(product)
    }

    return (
        <div className="flex border border-salmon-600 bg-white rounded-lg h-40 shadow-lg">
            <div className="bg-salmon-300 min-h-28 min-w-40 rounded-lg flex justify-center items-center">
                Imagem
            </div>
            <div className="flex flex-col px-4 py-2 justify-between flex-1">
                <div className="flex gap-4">
                    <div className="flex flex-col">
                        <span className="font-semibold text-base">
                            {product.name}
                        </span>
                        <span className="text-zinc-500 text-xs line-clamp-2">
                            {product.description}
                        </span>
                    </div>
                </div>
                <div className="flex flex-col gap-2">
                    {product.newPrice ? (
                        <div className="flex flex-col">
                            <span className="text-zinc-500 flex gap-4 text-xs">
                                <s>{priceFormat(product.price)}</s>
                                <div className="flex text-green-600 items-center gap-1">
                                    <ChevronDownCircle className="size-3 fill-green-200" />
                                    {(
                                        (1 - product.newPrice / product.price) *
                                        100
                                    ).toFixed(0)}
                                    %
                                </div>
                            </span>
                            <span className="text-sm font-semibold">
                                {priceFormat(product.newPrice)}
                            </span>
                        </div>
                    ) : (
                        <span className="font-semibold text-sm">
                            {priceFormat(product.price)}
                        </span>
                    )}
                    <div className="flex justify-end gap-2">
                        <div className="flex items-center gap-1 text-xs border border-salmon-500 rounded-md">
                            <button
                                onClick={() => removeItem()}
                                className="border border-r-salmon-500 p-1 hover:bg-salmon-100"
                            >
                                <Minus className="text-salmon-600 size-4 border-none" />
                            </button>
                            <div className="p-1">{countItem}</div>
                            <button
                                onClick={() => addItem()}
                                className="border border-l-salmon-500 p-1 hover:bg-salmon-100"
                            >
                                <Plus className="text-green-500 size-4" />
                            </button>
                        </div>
                        <div className="flex justify-end">
                            <Button
                                size={"xs"}
                                onClick={() => addToCart(product)}
                            >
                                <ShoppingCart />
                            </Button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
