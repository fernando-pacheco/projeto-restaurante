import { ProductItemProps, ProductProps } from "@/interface/product"
import { X } from "lucide-react"
import { Tooltip, TooltipContent, TooltipTrigger } from "../atoms/tooltip"
import { priceFormat } from "@/utils/price-format"
import { cart } from "@/utils/cart"

export function CartItem({ product }: ProductItemProps) {
    function removeItem(product: ProductProps) {
        if (product.amount === 0) {
            cart.remove(product.id)
        } else {
            product.amount = product.amount - 1
        }
    }

    function addItem(product: ProductProps) {
        product.amount = product.amount + 1
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
                                <button className="hover:bg-salmon-100 rounded-full p-1">
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
                                <span className="font-semibold">
                                    {priceFormat(product.newPrice)}
                                </span>
                            </>
                        ) : (
                            <span className="font-semibold">
                                {priceFormat(product.price)}
                            </span>
                        )}
                    </div>
                    <span>Quantidade: {product.amount}</span>
                </div>
                <div>{product.amount * product.price}</div>
            </div>
        </div>
    )
}
