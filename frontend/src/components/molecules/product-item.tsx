import { ChevronDownCircle, MinusCircle, PlusCircle } from "lucide-react"
import { useState } from "react"

interface ProductProps {
    id: string
    tag: string
    name: string
    description: string
    price: number
    newPrice?: number
    amount?: number
}

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

    return (
        <div className="flex flex-col border border-salmon-600 bg-white rounded-lg h-44 shadow-lg">
            <div className="flex gap-4">
                <div className="bg-salmon-300 h-24 w-40 rounded-lg" />
                <div className="flex flex-col py-2 pr-2">
                    <span className="font-semibold text-lg">
                        {product.name}
                    </span>
                    <span className="text-zinc-500 text-sm">
                        {product.description}
                    </span>
                </div>
            </div>
            <div className="flex justify-around">
                {product.newPrice ? (
                    <div className="flex flex-col py-2 pl-2">
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
                <div className="flex items-center gap-1">
                    <button onClick={() => removeItem()}>
                        <MinusCircle className="fill-red-500 text-white" />
                    </button>
                    {countItem}
                    <button onClick={() => addItem()}>
                        <PlusCircle className="fill-green-500 text-white" />
                    </button>
                </div>
            </div>
        </div>
    )
}
