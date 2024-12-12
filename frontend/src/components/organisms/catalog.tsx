import { Button } from "../atoms/button"

export function Catalog() {
    const len = Array.from({ length: 15 }, (_, i) => i + 1)

    return (
        <body>
            <div className="flex overflow-x-auto [&::-webkit-scrollbar]:hidden gap-4 pb-4">
                {len.map((item) => (
                    <Button key={item}>Layer {item}</Button>
                ))}
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
        </body>
    )
}
