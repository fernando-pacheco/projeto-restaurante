import { MainCard } from "../organisms/main-card"
import { Menu } from "../organisms/menu"

export function Catalog() {
    return (
        <div className="w-full">
            <div className="flex gap-8 flex-col">
                <MainCard />
                <Menu />
            </div>
        </div>
    )
}
