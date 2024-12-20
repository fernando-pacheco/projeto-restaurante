import { ProductItemProps } from "@/interface/product"
import { Dialog, DialogContent, DialogTrigger } from "../atoms/dialog"
import { ProductDetails } from "../molecules/product-details"
import { ProductItem } from "../molecules/product-item"

export function Product({ product }: ProductItemProps) {
    return (
        <Dialog>
            <DialogTrigger asChild>
                <div className="cursor-pointer">
                    <ProductItem product={product} />
                </div>
            </DialogTrigger>
            <DialogContent>
                <ProductDetails product={product} />
            </DialogContent>
        </Dialog>
    )
}
