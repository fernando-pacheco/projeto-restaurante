import { ProductItemProps } from "@/interface/product"

export function ProductDetails({ product }: ProductItemProps) {
    return (
        <div className="flex flex-col gap-8 w-full overflow-y-auto scrollable-div pr-3">
            <span className="font-semibold text-4xl">{product.name}</span>
            <div className="flex min-h-[300px] w-full justify-center items-center bg-salmon-500 text-salmon-50">
                IMAGEM
            </div>
            <span className="text-justify">{product.fullDescription}</span>
            <span className="text-justify">{product.fullDescription}</span>
            <span className="text-justify">{product.fullDescription}</span>
            <span className="text-justify">{product.fullDescription}</span>
            <span className="text-justify">{product.fullDescription}</span>
            <span className="text-justify">{product.fullDescription}</span>
            <span className="text-justify">{product.fullDescription}</span>
            <span className="text-justify">{product.fullDescription}</span>
            <span className="text-justify">{product.fullDescription}</span>
            <span className="text-justify">{product.fullDescription}</span>
            <span className="text-justify">{product.fullDescription}</span>
        </div>
    )
}
