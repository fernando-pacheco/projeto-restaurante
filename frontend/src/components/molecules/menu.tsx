import { useRef, useState } from "react"
import { dataSearch } from "@/utils/label-search"
import { CardSearch } from "./card-search"
import { Logo } from "../atoms/logo"
import { Products } from "./products"

export function Menu() {
    const carouselRef = useRef<HTMLDivElement>(null)
    const [isDragging, setIsDragging] = useState(false)
    const [startX, setStartX] = useState(0)
    const [scrollLeft, setScrollLeft] = useState(0)
    const [selectedId, setSelectedId] = useState<string>("promocao")

    const handleMouseDown = (e: React.MouseEvent<HTMLDivElement>) => {
        if (carouselRef.current) {
            setIsDragging(true)
            setStartX(e.pageX - carouselRef.current.offsetLeft)
            setScrollLeft(carouselRef.current.scrollLeft)
        }
    }

    const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
        if (!isDragging || !carouselRef.current) return
        e.preventDefault()
        const x = e.pageX - carouselRef.current.offsetLeft
        const walk = (x - startX) * 2
        carouselRef.current.scrollLeft = scrollLeft - walk
    }

    const handleMouseUpOrLeave = () => {
        setIsDragging(false)
    }

    const handleCardSelect = (id: string) => {
        setSelectedId(id)
    }

    function handleSelected(id: string, selectedId: string) {
        if (id === selectedId) {
            return "selected"
        }

        return "default"
    }

    return (
        <div className="grid grid-cols-3 gap-6">
            <div className="col-span-2 rounded-lg gap-4 flex flex-col">
                <span className="text-4xl font-semibold">Menu</span>
                <div
                    ref={carouselRef}
                    className={`flex overflow-x-auto gap-4 drop-shadow-lg [&::-webkit-scrollbar]:hidden ${
                        isDragging ? "cursor-grabbing" : "cursor-grab"
                    }`}
                    onMouseDown={handleMouseDown}
                    onMouseMove={handleMouseMove}
                    onMouseUp={handleMouseUpOrLeave}
                    onMouseLeave={handleMouseUpOrLeave}
                >
                    {dataSearch.map((item) => (
                        <button
                            key={item.id}
                            onClick={() => handleCardSelect(item.id)}
                        >
                            <CardSearch
                                variant={handleSelected(item.id, selectedId)}
                                description={item.description}
                                icon={
                                    <Logo
                                        alt={item.id}
                                        src={item.icon}
                                        className="size-10"
                                    />
                                }
                            />
                        </button>
                    ))}
                </div>
                <div>
                    <Products tag={selectedId} />
                </div>
            </div>
            <div className="w-full h-[500px] bg-salmon-200 rounded-lg drop-shadow-lg"></div>
        </div>
    )
}
