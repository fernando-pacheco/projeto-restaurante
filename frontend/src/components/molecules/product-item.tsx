import { ProductProps } from "@/interface/product"
import { productsList } from "@/utils/products-list"
import {
    ChevronDownCircle,
    MinusCircle,
    PlusCircle,
    ShoppingCart,
} from "lucide-react"
import { useState } from "react"
import { Button } from "../atoms/button"

interface ProductItemProps {
    product: ProductProps
}

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
        productsList.push(product)
    }

    return (
        <div className="flex flex-col border border-salmon-600 bg-white rounded-lg h-52 shadow-lg">
            <div className="flex gap-4">
                <div className="bg-salmon-300 h-28 w-40 rounded-lg" />
                <div className="flex flex-col py-2 pr-2">
                    <span className="font-semibold text-lg">
                        {product.name}
                    </span>
                    <span className="text-zinc-500 text-sm">
                        {product.description}
                    </span>
                </div>
            </div>
            <div className="flex justify-between">
                {product.newPrice ? (
                    <div className="flex flex-col py-4 pl-4">
                        <span className="text-zinc-500 flex gap-4">
                            <s>R$ {product.price},00</s>
                            <div className="flex text-green-600 items-center gap-1">
                                <ChevronDownCircle className="size-4 fill-green-200" />
                                {(
                                    (1 - product.newPrice / product.price) *
                                    100
                                ).toFixed(2)}
                                %
                            </div>
                        </span>
                        <span>R$ {product.newPrice},00</span>
                    </div>
                ) : (
                    <span className="font-semibold">R$ {product.price},00</span>
                )}
                <div className="flex flex-col gap-2 py-4 pr-4">
                    <div className="flex items-center gap-1">
                        <button onClick={() => removeItem()}>
                            <MinusCircle className="fill-red-500 text-white" />
                        </button>
                        {countItem}
                        <button onClick={() => addItem()}>
                            <PlusCircle className="fill-green-500 text-white" />
                        </button>
                    </div>
                    <div className="flex justify-end">
                        <Button size={"sm"} onClick={() => addToCart(product)}>
                            <ShoppingCart />
                        </Button>
                    </div>
                </div>
            </div>
        </div>
    )
}
