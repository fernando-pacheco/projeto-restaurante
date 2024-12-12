import { dataSearch } from "@/utils/label-search"
import { CardSearch } from "../molecules/card-search"

export function Catalog() {
    return (
        <div className="w-full">
            <div className="flex items-center justify-center px-16 overflow-x-auto [&::-webkit-scrollbar]:hidden gap-4 pb-4">
                {dataSearch.map((item, index) => {
                    if (index <= 8) {
                        return (
                            <CardSearch
                                key={item.description}
                                description={item.description}
                                icon={<item.icon className="size-10" />}
                            />
                        )
                    }
                })}
            </div>
            <div className="flex gap-4 flex-col">
                <div className="grid grid-cols-8 gap-4 h-[400px]">
                    <div className="flex justify-center col-span-2 items-center bg-zinc-200 rounded-lg">
                        layer2.1
                    </div>

                    <div className="flex justify-center col-span-4 items-center bg-zinc-200 rounded-lg">
                        layer2.2
                    </div>
                    <div className="flex justify-center col-span-2 items-center bg-zinc-200 rounded-lg">
                        layer2.3
                    </div>
                </div>
                <div className="w-full h-[1000px] bg-black"></div>
            </div>
        </div>
    )
}
