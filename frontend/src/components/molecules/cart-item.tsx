import { ProductItemProps, ProductProps } from "@/interface/product"
import { Minus, Plus, X } from "lucide-react"
import { Tooltip, TooltipContent, TooltipTrigger } from "../atoms/tooltip"
import { priceFormat } from "@/utils/price-format"
import { cart } from "@/utils/cart"

export function CartItem({ product }: ProductItemProps) {
    function removeItem(product: ProductProps) {
        if (product.amount === 0) {
            cleanUpItem(product.id)
        } else {
            product.amount = product.amount - 1
            if (product.amount === 0) {
                cleanUpItem(product.id)
            }
        }
    }

    function addItem(product: ProductProps) {
        product.amount = product.amount + 1
    }

    function cleanUpItem(id: string) {
        const index = cart.findIndex((item) => item.id === id)
        if (index !== -1) {
            cart.splice(index, 1)
        }
    }

    return (
        <div className="flex border border-salmon-600 bg-white rounded-lg h-40 shadow-lg">
            <div className="bg-salmon-300 min-h-28 min-w-40 rounded-lg flex justify-center items-center">
                Imagem
            </div>
            <div className="flex flex-col p-4 flex-1">
                <div className="flex gap-4 justify-between flex-1">
                    <div className="flex flex-col justify-between">
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
                    </div>
                    <div>
                        <Tooltip>
                            <TooltipTrigger>
                                <button
                                    className="hover:bg-salmon-100 rounded-full p-1"
                                    onClick={() => cleanUpItem(product.id)}
                                >
                                    <X size={20} />
                                </button>
                            </TooltipTrigger>
                            <TooltipContent className="">
                                <span>Limpar</span>
                            </TooltipContent>
                        </Tooltip>
                    </div>
                </div>
                <div className="flex justify-between pr-2">
                    <div>
                        {product.newPrice ? (
                            <>
                                <s className="text-xs text-zinc-600">
                                    {priceFormat(product.price)}
                                </s>{" "}
                                <span>{priceFormat(product.newPrice)}</span>
                            </>
                        ) : (
                            <span>{priceFormat(product.price)}</span>
                        )}
                    </div>
                    <div className="flex items-center gap-1 text-xs border border-salmon-500 rounded-md">
                        <button
                            onClick={() => removeItem(product)}
                            className="border border-r-salmon-500 p-1 hover:bg-salmon-100"
                        >
                            <Minus className="text-salmon-600 size-4 border-none" />
                        </button>
                        <div className="p-1">{product.amount}</div>
                        <button
                            onClick={() => addItem(product)}
                            className="border border-l-salmon-500 p-1 hover:bg-salmon-100"
                        >
                            <Plus className="text-green-500 size-4" />
                        </button>
                    </div>
                </div>
                <div className="font-semibold">
                    {product.amount &&
                        (product.newPrice
                            ? priceFormat(product.amount * product.newPrice)
                            : priceFormat(product.amount * product.price))}
                </div>
            </div>
        </div>
    )
}
