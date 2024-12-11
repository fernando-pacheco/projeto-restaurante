import { LayoutHome } from "@/components/organisms/layout-home"

export function Home() {
    return (
        <LayoutHome>
            <div className="flex flex-col h-screen">
                <div className="flex space-x-4">
                    <div className="flex justify-center items-center w-1/2 h-1/2 bg-zinc-200 rounded-lg">
                        layer1.1
                    </div>
                    <div className="flex justify-center items-center w-1/2 h-1/2 bg-zinc-200 rounded-lg">
                        layer1.2
                    </div>
                </div>
                <div className="flex space-x-2">
                    <div className="flex justify-center items-center w-1/3 h-1/2 bg-zinc-200 rounded-lg">
                        layer2.1
                    </div>
                    <div className="flex justify-center items-center w-1/3 h-1/2 bg-zinc-200 rounded-lg">
                        layer2.2
                    </div>
                    <div className="flex justify-center items-center w-1/3 h-1/2 bg-zinc-200 rounded-lg">
                        layer2.3
                    </div>
                </div>
            </div>
        </LayoutHome>
    )
}
