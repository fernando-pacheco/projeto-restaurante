import { LayoutHome } from "@/components/organisms/layout-home"

export function Home() {
    return (
        <LayoutHome>
            <div className="grid grid-cols-4 gap-4 h-[1000px]">
                <div className="flex justify-center col-span-2 items-center bg-zinc-200 rounded-lg">
                    layer1.1
                </div>
                <div className="flex justify-center col-span-2 items-center bg-zinc-200 rounded-lg">
                    layer1.2
                </div>
                <div className="flex justify-center items-center bg-zinc-200 rounded-lg">
                    layer2.1
                </div>
                <div className="flex justify-center col-span-2 items-center bg-zinc-200 rounded-lg">
                    layer2.2
                </div>
                <div className="flex justify-center items-center bg-zinc-200 rounded-lg">
                    layer2.3
                </div>
            </div>
            <div className="w-full h-[1000px] bg-black"></div>
        </LayoutHome>
    )
}
